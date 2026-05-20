import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Inovara - Teknologi Noesantara",
    layout="wide"
)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title(" MENU")
page = st.sidebar.radio("Pindah ke Halaman:", ["Home", "Profil & Video"])

# --- HALAMAN 1: Home ---
if page == "Home":
    st.title(" PT. Inovara Digital Noesantara")
    st.subheader("INOTEKNO - Inovation For The Future")
    
    col_hero_text, col_hero_img = st.columns([3, 2])
    
    with col_hero_text:
        st.markdown("### **Apa itu Inovara?**")
        st.write("""
        **Inovara** adalah produsen dan penyedia solusi **Interactive Smartboard** premium yang dirancang untuk merevolusi cara Anda berkolaborasi, melakukan presentasi, dan mengajar. 
        Kami menggabungkan perangkat keras layar sentuh 4K *ultra-responsive* dengan ekosistem perangkat lunak cerdas untuk menciptakan ruang kerja dan ruang belajar masa kini yang interaktif dan *paperless*.
        """)
        
        st.markdown("### **Kapan Kami Didirikan?**")
        st.write("""
        Didirikan pada awal tahun **2025**, Inovara lahir dari visi untuk menghapus batasan kolaborasi fisik dan digital. Melihat papan tulis konvensional dan proyektor buram yang sudah tidak relevan dengan era kerja *hybrid*, kami menciptakan hardware pintar yang kini telah dipercaya oleh berbagai korporasi dan institusi pendidikan.
        """)
    
    with col_hero_img:
        st.image(
            "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&q=80&w=600", 
            caption="Smartboard Inovara Mengubah Ruang Rapat Menjadi Lebih Interaktif",
            use_container_width=True
        )

    st.divider()

    # Layer 2: Promosi/Layanan - 3 gambar BERBEDA tapi tema smartboard/presentasi
    st.header(" Kenapa Harus Memilih Smartboard Inovara?")
    st.write("Lebih dari sekadar layar besar, ini adalah pusat kendali ide, kreativitas, dan produktivitas tim Anda.")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?auto=format&fit=crop&q=80&w=400",
            use_container_width=True
        )
        st.markdown("###  Cepat & Responsif")
        st.write("Dengan teknologi *Ultra-Low Latency*, menulis di atas Smartboard Inovara terasa sealami menulis di kertas biasa. Mendukung *multi-touch* hingga 20 titik tanpa ada jeda.")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=400",
            use_container_width=True
        )
        st.markdown("###  Aman & Mudah Berbagi")
        st.write("Hasil rapat atau coretan ide tidak akan hilang. Cukup scan **QR Code** di layar, dan file presentasi yang terenkripsi aman langsung masuk ke smartphone seluruh peserta.")

    with col3:
        st.image(
            "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&q=80&w=400",
            use_container_width=True
        )
        st.markdown("###  Fitur Kustom Berbasis AI")
        st.write("Dilengkapi fitur pintar otomatis seperti *Handwriting-to-Text* (mengubah tulisan tangan jadi teks rapi), penerjemah instan, serta integrasi mulus dengan aplikasi *video conference*.")

    st.divider()

    # Informasi Tambahan
    st.header(" Jangkauan & Dampak Inovara")
    
    col_info1, col_info2, col_info3 = st.columns(3)
    
    with col_info1:
        st.markdown("###  Siapa yang Bisa Membeli Produk Kami?")
        st.write("""
        Produk Smartboard kami dirancang sangat inklusif untuk:
        * **Dunia Korporat & Startup:** Untuk ruang rapat eksekutif (*Boardroom*) dan ruang kolaborasi tim (*Huddle Room*).
        * **Institusi Pendidikan (Sekolah & Kampus):** Menggantikan papan tulis kapur/spidol agar proses belajar-mengajar lebih visual.
        * **Instansi Pemerintah & Command Center:** Untuk pemetaan data secara *real-time* dan diskusi taktis.
        """)
        
    with col_info2:
        st.markdown("###  Di Mana Anda Bisa Mendapatkan Produk Kami?")
        st.write("""
        Kami memiliki *experience zone* (showroom) di beberapa kota besar agar Anda bisa mencoba langsung kehebatan layar kami. Proses pemesanan, pengiriman, instalasi bracket, hingga demo penggunaan dilayani langsung oleh tim teknisi resmi Inovara.
        """)
        
    with col_info3:
        st.markdown("###  Dampak ke Noesantara & Luar Negeri")
        st.write("""
        * **Di Noesantara:** Aktif mendukung program modernisasi ruang kelas di berbagai daerah guna menciptakan pemerataan kualitas edukasi interaktif yang *paperless*.
        * **Di Luar Negeri:** Menjadi produk Smartboard lokal rakitan anak bangsa yang siap bersaing di pasar Asia Tenggara dengan keunggulan harga kompetitif dan fitur AI yang lebih cerdas.
        """)

# --- HALAMAN 2: PROFIL & VIDEO ---
else:
    st.title("Profil Perusahaan")
    
    # st.header(" Demo Produk & Cara Kerja Smartboard")
    # st.write("Lihat bagaimana Smartboard Inovara mengubah ruang presentasi yang membosankan menjadi sangat interaktif.")
    video_url = "https://www.youtube.com/watch?v=aS38b4CbOEg" 
    st.video(video_url)
    
    st.divider()

    st.header(" Visi & Misi")
    
    tab1, tab2 = st.tabs(["Visi Utama", "Misi Perusahaan"])
    
    with tab1:
        st.subheader("Visi")
        st.info("""
        "Menjadi penyedia teknologi papan tulis interaktif nomor satu di Asia Tenggara yang menghubungkan manusia, ide, dan teknologi tanpa sekat pembatas."
        """)
        
    with tab2:
        st.subheader("Misi")
        st.info("""
        - Inovasi Produk Lokal Berstandar Global: Mengembangkan teknologi smartboard yang canggih namun relevan dengan kebutuhan spesifik institusi pendidikan dan perkantoran di Indonesia.
        - Aksesibilitas Teknologi: Mempercepat pemerataan teknologi interaktif di seluruh penjuru Nusantara untuk mempersempit kesenjangan digital.
        - Pemberdayaan Pengguna: Memberikan pengalaman kolaborasi yang mulus dan intuitif guna meningkatkan kreativitas serta produktivitas penggunanya.
        - Keunggulan Operasional & Layanan: Memberikan dukungan teknis dan layanan purna jual yang prima sebagai perusahaan yang berakar di Jakarta untuk seluruh konsumen Indonesia.
        - Kolaborasi Strategis: Membangun kemitraan yang kuat dengan pemerintah dan sektor swasta dalam menciptakan ekosistem digital yang tangguh.
        - Standar Kualitas Kebanggaan: Menjamin setiap produk yang lahir dari Jakarta memiliki ketahanan dan performa kelas dunia sehingga menjadi standar baru perangkat teknologi nasional.
        """)

# --- FOOTER & HUBUNGI KAMI ---
st.divider()
st.header("📞 Hubungi Inovara")
col_foot1, col_foot2, col_foot3 = st.columns(3)

with col_foot1:
    st.markdown("🏢 **Showroom & Kantor Pusat:**")
    st.write("""
    PT. Inovara Digital Noesantara  
    Jl. Apron, Kb. Kosong, Kemayoran, Jakarta Pusat, 10630
    """)

with col_foot2:
    st.markdown("✉️ **Email Penjualan & Dukungan:**")
    st.write("""
    * Layanan: `inotekno@inovaratekno.com`
    """)

with col_foot3:
    st.markdown("📱 **Hotline CS & Demo Request:**")
    st.write("""
    * WhatsApp / Telepon: `+62 895-0776-5859`  
    * Hubungi kami untuk menjadwalkan **Demo Unit Gratis** langsung di kantor atau sekolah Anda!
    """)

st.sidebar.markdown("---")
st.sidebar.write("© 2026 PT. Inovara Digital Noesantara")