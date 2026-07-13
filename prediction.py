import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Cache model agar tidak diload berulang-ulang
@st.cache_resource
def load_model():
    # Pastikan file best_fire_model.h5
    return tf.keras.models.load_model('best_fire_model.h5')

def run():
    st.title("📸 Fire Detection Prediction")
    st.write("Unggah gambar untuk mendeteksi keberadaan api menggunakan model Artificial Neural Network (CNN).")
    
    model = load_model()
    
    # Komponen pengunggah file
    uploaded_file = st.file_uploader("Upload sebuah gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Menampilkan gambar yang diunggah
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar yang diproses', use_column_width=True)
        
        st.write("Menganalisis gambar...")
        
        # Preprocessing gambar 
        img = image.convert('RGB')
        img = img.resize((224, 224))
        
        # Konversi ke array dan normalisasi
        img_array = np.array(img) / 255.0
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Prediksi
        prediction = model.predict(img_batch)
        probabilitas = prediction[0][0]
        
        # Konversi ke label string
        if probabilitas > 0.5:
            hasil_label = "Non-Fire 🌲"
            kepercayaan = probabilitas * 100
        else:
            hasil_label = "Fire 🔥"
            kepercayaan = (1 - probabilitas) * 100
            
        # Menampilkan hasil
        st.markdown("---")
        st.subheader("Hasil Analisis:")
        
        if "Non-Fire" in hasil_label:
            st.success(f"Sistem mendeteksi ini sebagai: **{hasil_label}**")
        else:
            st.error(f"Peringatan! Sistem mendeteksi ini sebagai: **{hasil_label}**")
            
        st.write(f"Tingkat Kepercayaan Model: **{kepercayaan:.2f}%**")
