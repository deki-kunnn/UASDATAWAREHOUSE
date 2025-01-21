import streamlit as st
import pickle
import numpy as np
import os

# Load the pre-trained model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model_uas.pkl')

model = pickle.load(open(model_path, 'rb'))

# Create a title for the app
st.title("Prediksi Premi Asuransi Kesehatan")

# Create input fields for each attribute
age = st.number_input("Usia", min_value=18)
sex = st.selectbox("Jenis Kelamin", options=["Laki-laki", "Perempuan"])
bmi = st.number_input("BMI")
children = st.number_input("Jumlah Anak", min_value=0)
smoker = st.selectbox("Perokok?", options=["Ya", "Tidak"])

# Convert categorical values to numerical
sex = 1 if sex == "Laki-laki" else 0
smoker = 1 if smoker == "Ya" else 0

# Create a button to trigger prediction
if st.button("Prediksi"):
    # Create a numpy array from the input values
    X = np.array([[age, sex, bmi, children, smoker]])

    # Make prediction using the loaded model
    prediction = model.predict(X)[0]

    # Display the prediction
    st.write("Prediksi Premi Asuransi: Rp.", round(prediction, 2))

    # Tambahkan NIM dan nama Anda di sini (sesuaikan dengan kebutuhan)
    st.write("Dibuat oleh: [2021230045] - [RIZKI ARDI KURNIAWAN KUSWORO]")
