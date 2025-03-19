import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import joblib
import pandas as pd
from io import BytesIO

# **Fungsi untuk memuat model deep learning**
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("osteoporosis_dual_target_model.h5")

# **Fungsi untuk memuat preprocessor tabular**
@st.cache_resource
def load_preprocessor():
    return joblib.load("tabular_preprocessor_dual_target.pkl")

# **Fungsi untuk mengklasifikasikan T-score**
def classify_t_score(t_score):
    if t_score <= -2.5:
        return "Osteoporosis", "#e74c3c"  # Merah
    elif -2.5 < t_score <= -1.0:
        return "Osteopenia", "#f1c40f"  # Kuning
    else:
        return "Normal", "#2ecc71"  # Hijau

# **Fungsi untuk memproses data tabular**
def process_tabular_data(input_data, preprocessor):
    df = pd.DataFrame([input_data])
    try:
        transformed_data = preprocessor.transform(df)
    except Exception as e:
        st.error(f"Error preprocessing data: {e}")
        return None
    return transformed_data

# **Fungsi untuk memproses gambar**
def process_image(image):
    try:
        img = load_img(BytesIO(image.read()), target_size=(224, 224))  # Menggunakan BytesIO untuk streamlit uploader
        img_array = img_to_array(img) / 255.0  # Normalisasi
        return np.expand_dims(img_array, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# **Tampilan Streamlit**
st.set_page_config(page_title="Osteoporosis Diagnosis", page_icon="🦴", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #ffffff;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
            padding-bottom: 20px;
        }
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #7f8c8d;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>Osteoporosis Diagnosis App 🦴</h1>", unsafe_allow_html=True)

# **Tampilan utama dalam tiga kolom**
col1, col2, col3 = st.columns([1, 1, 1])

# **Kolom 1: Informasi Pasien**
with col1:
    st.subheader("Patient Information")
    col1a, col1b = st.columns(2)
    with col1a:
        age = st.number_input("Age", min_value=0, max_value=120, value=50)
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5)
        gender = st.selectbox("Gender", ["Pilih", "Male", "Female"], index=0)
        history_fracture = st.selectbox("History of Fracture", ["Pilih", "Yes", "No"], index=0)
        family_history = st.selectbox("Family History of Osteoporosis", ["Pilih", "Yes", "No"], index=0)
    with col1b:
        smoker = st.selectbox("Smoker", ["Pilih", "Yes", "No"], index=0)
        alcoholic = st.selectbox("Alcoholic", ["Pilih", "Yes", "No"], index=0)
        estrogen_use = st.selectbox("Estrogen Use", ["Pilih", "Yes", "No"], index=0)
        diabetic = st.selectbox("Diabetic", ["Pilih", "Yes", "No"], index=0)
        hypothyroidism = st.selectbox("Hypothyroidism", ["Pilih", "Yes", "No"], index=0)

# **Kolom 2: Upload X-ray Image**
with col2:
    st.subheader("Upload X-ray Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded X-ray", width=250)

# **Kolom 3: Hasil Prediksi**
with col3:
    st.subheader("Prediction Result")
    if st.button("Predict"):
        if uploaded_image is not None:
            with st.spinner("Loading model & preprocessing..."):
                model = load_model()
                preprocessor = load_preprocessor()

            # **Cek apakah semua opsi telah dipilih**
            if "Pilih" in [gender, history_fracture, family_history, smoker, alcoholic, estrogen_use, diabetic, hypothyroidism]:
                st.warning("⚠️ Please select all options in the sidebar.")
            else:
                tabular_data = {
                    "Age": age,
                    "BMI": bmi,
                    "Gender": gender,
                    "History of Fracture": history_fracture,
                    "Family History of Osteoporosis": family_history,
                    "Smoker": smoker,
                    "Alcoholic": alcoholic,
                    "Estrogen Use": estrogen_use,
                    "Diabetic": diabetic,
                    "Hypothyroidism": hypothyroidism,
                }
                processed_tabular = process_tabular_data(tabular_data, preprocessor)
                processed_image = process_image(uploaded_image)

                if processed_tabular is not None and processed_image is not None:
                    with st.spinner("Predicting..."):
                        y_pred_reg, y_pred_cls_prob = model.predict([processed_image, processed_tabular])
                        predicted_t_score = y_pred_reg[0][0]
                        predicted_diagnosis, diagnosis_color = classify_t_score(predicted_t_score)

                        st.success("✅ Prediction Completed!")
                        st.markdown(f"<h3 style='color:#2c3e50;'>Predicted T-score: {predicted_t_score:.2f}</h3>", unsafe_allow_html=True)
                        st.markdown(f"<h2 style='color:black;'>Predicted Diagnosis: <span style='color:{diagnosis_color};'>{predicted_diagnosis}</span></h2>", unsafe_allow_html=True)
                else:
                    st.warning("⚠️ Failed to process image or tabular data. Please check inputs.")
        else:
            st.warning("⚠️ Please upload an image before predicting.")
