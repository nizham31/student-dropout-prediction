import streamlit as st
import pandas as pd
import joblib

# Setup Halaman
st.set_page_config(page_title="Jaya Jaya Institut - Dropout Prediction", page_icon="🎓", layout="wide")

# Load Semua Model dan Scaler
@st.cache_resource
def load_models():
    # Model 6 Fitur (Untuk Input Manual)
    model_lite = joblib.load('model/rf_model_deploy.joblib')
    scaler_lite = joblib.load('model/scaler_deploy.joblib')
    
    # Model 36 Fitur (Untuk Upload CSV)
    model_full = joblib.load('model/random_forest_model.joblib')
    scaler_full = joblib.load('model/scaler.joblib')
    
    # Label Encoder
    le = joblib.load('model/label_encoder_deploy.joblib') # Bisa pakai yang mana aja karena isinya sama
    
    return model_lite, scaler_lite, model_full, scaler_full, le

model_lite, scaler_lite, model_full, scaler_full, le = load_models()

# Header Utama
st.title("🎓 Jaya Jaya Institut: Student Dropout Prediction")
st.write("Sistem Deteksi Dini Status Mahasiswa (Dropout / Enrolled / Graduate)")
st.markdown("---")

# BIKIN DUA TAB
tab1, tab2 = st.tabs(["👤 Prediksi Tunggal (Input Manual)", "📂 Prediksi Massal (Upload CSV)"])

# ==========================================
# TAB 1: PREDIKSI TUNGGAL (6 FITUR)
# ==========================================
with tab1:
    st.header("Prediksi Status Satu Mahasiswa")
    st.write("Masukkan data akademik dan finansial mahasiswa pada form di bawah ini.")
    
    col1, col2 = st.columns(2)
    with col1:
        tuition = st.selectbox("Status Pembayaran Uang Kuliah", ["Menunggak", "Lunas"])
        scholarship = st.selectbox("Status Beasiswa", ["Tidak Punya", "Punya Beasiswa"])
        sem1_appr = st.number_input("Jumlah SKS Lulus (Semester 1)", min_value=0, max_value=20, value=5)

    with col2:
        sem1_grade = st.number_input("Nilai IP Semester 1 (0-20)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        sem2_appr = st.number_input("Jumlah SKS Lulus (Semester 2)", min_value=0, max_value=20, value=5)
        sem2_grade = st.number_input("Nilai IP Semester 2 (0-20)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)

    tuition_val = 1 if tuition == "Lunas" else 0
    scholarship_val = 1 if scholarship == "Punya Beasiswa" else 0

    if st.button("Prediksi Sekarang 🚀"):
        input_data = pd.DataFrame({
            'Tuition_fees_up_to_date': [tuition_val],
            'Scholarship_holder': [scholarship_val],
            'Curricular_units_1st_sem_approved': [sem1_appr],
            'Curricular_units_1st_sem_grade': [sem1_grade],
            'Curricular_units_2nd_sem_approved': [sem2_appr],
            'Curricular_units_2nd_sem_grade': [sem2_grade]
        })
        
        input_scaled = scaler_lite.transform(input_data)
        pred_encoded = model_lite.predict(input_scaled)
        pred_label = le.inverse_transform(pred_encoded)[0]
        
        st.markdown("---")
        if pred_label == 'Dropout':
            st.error(f"⚠️ Prediksi: Mahasiswa berpotensi **DROPOUT**. Segera lakukan intervensi!")
        elif pred_label == 'Graduate':
            st.success(f"🎉 Prediksi: Mahasiswa berpotensi **GRADUATE** (Lulus).")
        else:
            st.warning(f"⏳ Prediksi: Mahasiswa berstatus **ENROLLED** (Masih aktif, pantau terus).")

# ==========================================
# TAB 2: PREDIKSI MASSAL (UPLOAD CSV 36 FITUR)
# ==========================================
with tab2:
    st.header("Prediksi Banyak Mahasiswa Sekaligus")
    st.write("Upload file CSV yang berisi 36 kolom fitur mahasiswa (seperti format dataset asli tanpa kolom Status).")
    
    uploaded_file = st.file_uploader("Upload File CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Baca data
            df_upload = pd.read_csv(uploaded_file, sep=';') # Asumsi sep=';' menyesuaikan format awal
            st.write("Preview Data yang Diupload:")
            st.dataframe(df_upload.head())
            
            if st.button("Mulai Prediksi Massal 🔍"):
                # Pastikan kolom sesuai dengan fitur asli
                # Scaling menggunakan scaler 36 fitur
                scaled_upload = scaler_full.transform(df_upload)
                
                # Prediksi
                predictions = model_full.predict(scaled_upload)
                predicted_labels = le.inverse_transform(predictions)
                
                # Tambahkan hasil ke dataframe
                df_upload['Prediksi_Status'] = predicted_labels
                
                st.success("Prediksi Selesai!")
                
                # Tampilkan hasil
                st.write("Hasil Prediksi:")
                st.dataframe(df_upload[['Tuition_fees_up_to_date', 'Curricular_units_1st_sem_grade', 'Prediksi_Status']].head(10)) # Nampilin cuplikan aja
                
                # Fitur Download Hasil
                csv_hasil = df_upload.to_csv(index=False, sep=';').encode('utf-8')
                st.download_button(
                    label="Download Hasil Prediksi (CSV) 📥",
                    data=csv_hasil,
                    file_name='hasil_prediksi_mahasiswa.csv',
                    mime='text/csv',
                )
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses file. Pastikan format kolom sesuai dengan dataset asli. Error: {e}")