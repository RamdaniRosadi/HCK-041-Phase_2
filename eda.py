import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def run():
    st.title("🔥 Exploratory Data Analysis (EDA)")
    st.write("Halaman ini menampilkan gambaran umum dari dataset Fire yang digunakan untuk melatih model Computer Vision.")
    
    st.markdown("---")
    
    st.subheader("1. Distribusi Kelas")
    st.write("Dataset ini terdiri dari dua kelas utama: **Fire** dan **Non-Fire**.")
    
    # Membuat plot dummy/representasi (Sesuaikan angkanya dengan jumlah asli dataset Anda)
    labels = ['Fire', 'Non-Fire']
    counts = [755, 244] # Ganti dengan angka asli dari dataset Anda
    
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=labels, y=counts, palette=['#FF5733', '#33FF57'], ax=ax)
    ax.set_title('Distribusi Data Kelas Fire vs Non-Fire')
    ax.set_ylabel('Jumlah Gambar')
    st.pyplot(fig)
    
    st.write("**Insight:** Dataset cenderung imbalanced Dataset cenderung imbalanced karena terdapat gambar fire yang lebih dominan daripada non-fire yang berguna untuk mendeteksi api.")
    
    st.markdown("---")
    
    st.subheader("2. Sampel Gambar")
    st.write("Berikut adalah contoh dari dataset yang digunakan:")
    
    # Anda bisa meletakkan 2 gambar contoh statis (contoh_fire.jpg & contoh_nonfire.jpg) di folder deployment
    # Jika tidak ada, Anda bisa menghapus bagian ini atau berkomentar.
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("Kategori: Fire")
        # st.image("contoh_fire.jpg", use_column_width=True) # Aktifkan dan siapkan file jika ingin pakai gambar
    with col2:
        st.success("Kategori: Non-Fire")
        # st.image("contoh_nonfire.jpg", use_column_width=True) # Aktifkan dan siapkan file jika ingin pakai gambar
