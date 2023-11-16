import streamlit as st
import joblib

st.title("Fraud E-Mail Detector")
with st.form("my_form"):
   email = st.text_input("Copy and Paste the E-Mail Content")
   submit = st.form_submit_button('Check')

   if submit:
      model = joblib.load("Email_Fraud_Detector_Model.pkl")
      model_output = model(email)
      label = model_output[0]["label"]
      score = model_output[0]["score"]
      st.write(f"The E-Mail looks {int(score*100)}% {label}")