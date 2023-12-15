# Fraud_EMail_Detector
* Achieved **99.86%** Accuracy in Fraud E-Mail Detection using Natural Language Processing (NLP) by Fine Tuning the **RoBERTa LLM Transformer** on a Dataset of 11,928 E-Mails using Python, Pandas, PyTorch, Hugging Face.
* Used **Hugging Face Hub** with **Hugging Face Inference API** for **MLOps / Deploying** the Model.
* Developed an Interactive Web App using Streamlit.
* Tech Used - **Python, Pandas, PyTorch, Hugging Face, Streamlit.**

## How to use it in your projects (2 Ways) -
### Using API Calls with Hugging Face Inference API (Recommended for using it directly in your App)
``` python
import streamlit as st
import joblib
import os 
from dotenv import load_dotenv
import requests

load_dotenv()
huggingface_token = os.environ["HUGGINGFACE_HUB_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/tush9905/email_fraud_detector"
headers = {"Authorization": f"Bearer {huggingface_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
```
### OR
### By Importing the Model Itself
  ``` python
  from transformers import AutoModel
  model = AutoModel.from_pretrained("tush9905/email_fraud_detector")
  ```


