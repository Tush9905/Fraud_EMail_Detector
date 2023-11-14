# Fraud_EMail_Detector
* Achieved **99.86%** Accuracy in Fraud E-Mail Detection using Natural Language Processing (NLP) by Fine Tuning the **RoBERTa LLM Transformer** on a Dataset of 11,928 E-Mails using Python, Pandas, PyTorch, Hugging Face.
* It is not Overfit

## How to use it in your projects -

* You can load it using joblib -

  ``` python
  import joblib
  joblib.load("Email_Fraud_Detector_Model.pkl")
  ```
  
### **OR**
  
* You can use hugging face pipeline and import the model using the config in the generated folder (Fraud_EMail_Detector) -

  ``` python
  from transformers import pipeline
  classifier = pipeline("text-classification", model="./email_fraud_detector/")
  ```
