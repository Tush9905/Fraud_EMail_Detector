# Fraud_EMail_Detector
* Achieved **99.86%** Accuracy in Fraud E-Mail Detection using Natural Language Processing (NLP) by Fine Tuning the **RoBERTa LLM Transformer** on a Dataset of 11,928 E-Mails using Python, Pandas, PyTorch, Hugging Face.

## How to use it in your projects (2 Ways) -
### Using API Calls with Hugging Face Inference API (Recommended for using it directly in your App)
``` python
import requests
from huggingface_token import token
# Use your own token

st.write("# Fake News Detector")
API_URL = "https://api-inference.huggingface.co/models/tush9905/email_fraud_detector"
headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
```
### OR
### By Importing the Model Itself
  ``` python
  from transformers import AutoModel
  model = AutoModel.from_pretrained("tush9905/fake_news_detector")
  ```


