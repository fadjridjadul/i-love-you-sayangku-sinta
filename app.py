import streamlit as st
import random
import time
from PIL import Image

# Daftar Gombalan
gombalan_list = [
    "Sayangku, kalau kamu jadi matahari, aku rela jadi planet yang terus mengelilingimu.",
    "Cintaku, kamu tahu bedanya kamu sama bintang? Bintang bersinar di langit, tapi kamu bersinar di hatiku.",
    "Manisku, kalau kamu senyum, aku lupa semua masalah. Jadi, senyum terus ya!",
    "Sayang wkwkwk, aku gak butuh kompas, karena hatiku selalu tertuju padamu.",
    "Kasihku, kalau cinta adalah bahasa, aku ingin menjadi kata yang selalu kamu ucapkan.",
    "Bidadariku, aku gak butuh Google Maps, karena arah terbaik selalu menuju hatimu.",
    "Sayang, aku rela jadi hujan kalau itu bisa membuatmu tersenyum saat melihat pelangi.",
    "Sayangku tersayang, kalau aku jadi hujan, aku ingin turun di hatimu agar bisa menemanimu setiap saat.",
    "Manisku, seperti WiFi, cintaku ke kamu full bar dan gak bakal putus!",
    "Cintaku, kalau kamu jadi lagu, aku mau jadi liriknya, supaya kita selalu bersama.",
    "Sayangku yang paling cantik, kamu kayak kopi pagi, selalu bikin hariku semangat!",
    "Sayangku, kamu itu seperti password WiFi, tanpa kamu hidupku terasa kosong.",
    "Honey, kamu gak perlu jadi artis, karena di hatiku kamu sudah jadi bintang paling bersinar.",
    "Pelangi hatiku, kalau aku punya satu permintaan, aku ingin habiskan sisa hidup bersamamu.",
    "Cintaku yang paling manis, meskipun jarak memisahkan kita, hatiku selalu dekat sama kamu.",
    "Beb, setiap detik yang aku lewati tanpamu terasa seperti setahun lamanya.",
    "Sayang sayang sayang, aku suka kamu bukan karena kamu sempurna, tapi karena kamu adalah yang terbaik untukku.",
    "Cintaku, kalau aku bisa memilih siapa yang ada di mimpiku setiap malam, aku akan selalu memilih kamu.",
    "Kasihku, kamu tahu bedanya kamu sama es krim? Es krim mencair di mulut, tapi kamu mencairkan hatiku.",
    "Baby, setiap kali aku melihatmu, aku merasa seperti ketemu bintang jatuh.",
    "Cintaku yang tak tergantikan, kalau cinta adalah perjalanan, aku ingin berjalan bersamamu selamanya.",
    "Sayangku yang lucu, kamu kayak film favoritku, selalu ingin aku tonton setiap hari.",
    "Manisku, kalau kamu jadi bunga, aku akan jadi lebah yang selalu mencari madumu.",
    "Cintaku sayang, setiap detak jantungku adalah lagu yang bernada namamu.",
    "Bebeb, kamu itu ibarat udara, aku gak bisa hidup tanpamu.",
    "Bidadariku yang menawan, kalau aku bisa jadi apa saja, aku mau jadi alasan senyummu.",
    "Kesayangan aku, kalau aku adalah pelaut, kamu adalah mercusuar yang selalu menunjukkan jalan pulang.",
    "Cintaku, kalau waktu bisa berhenti, aku ingin menghabiskannya bersamamu selamanya.",
    "Sayang, kalau kamu jadi air, aku rela tenggelam dalam cintamu.",
    "Honey Bunny, setiap kali aku mendengar namamu, hatiku langsung berdebar kayak kembang api",
]

def show_gombalan():
    gombal = random.choice(gombalan_list)
    st.subheader(":heart: Gombalan Spesial untuk Sayangku :heart:")
    st.success(gombal)

def main():
    st.set_page_config(page_title="Gombalan untuk Sayangku", page_icon="💖", layout="centered")
    
    # Background Styling
    st.markdown(
        """
        <style>
            body {
                background-color: #FFC0CB;
            }
            .stApp {
                background: linear-gradient(135deg, #FF69B4, #FFB6C1);
                color: white;
                text-align: center;
            }
            .stButton>button {
                background-color: #FF1493;
                color: white;
                font-size: 18px;
                border-radius: 15px;
                padding: 10px 20px;
            }
            .stButton>button:hover {
                background-color: #FF69B4;
            }
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("💌 Gombalan Manis untuk Sayangku 💌")
    st.write("Selamat datang di aplikasi gombalan spesial buatan aku! wkwkwk\n\nKlik tombol di bawah ya sayang untuk mendapatkan gombalan manis dari aku wkwkwk.")
    
    # Menampilkan gambar romantis dengan ukuran lebih kecil dan posisi tengah
    image = Image.open("love.png")  # Pastikan ada gambar love.png di folder yang sama
    st.markdown("<div class='center'>", unsafe_allow_html=True)
    st.image(image.resize((400, 400)), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Kasih Gombalan ✨"):
            with st.spinner("Mikirin kata-kata paling manis buat Kamu..."):
                time.sleep(1.5)
            show_gombalan()
    
    # Footer
    st.markdown("---")
    st.caption("Dibuat dengan 💖 oleh seseorang yang sangat mencintai Sinta Rona Pratama")
    
if __name__ == "__main__":
    main()
