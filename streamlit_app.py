import streamlit as st
import eda
import prediction

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Fire Detection App",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Membuat Sidebar untuk navigasi
st.sidebar.title("Navigasi")
st.sidebar.write("Pilih halaman yang ingin ditampilkan:")
page = st.sidebar.selectbox("Halaman:", ("Exploratory Data Analysis (EDA)", "Model Prediction"))

st.sidebar.markdown("---")
st.sidebar.write("Graded Challenge 7")
st.sidebar.write("Dibuat oleh: [Nama Anda]")

# Logika perpindahan halaman
if page == "Exploratory Data Analysis (EDA)":
    eda.run()
else:
    prediction.run()