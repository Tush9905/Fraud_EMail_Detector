# Fraud_EMail_Detector
* Achieved **99.86%** Accuracy in Fraud E-Mail Detection using Natural Language Processing (NLP) by Fine Tuning the **RoBERTa LLM Transformer** on a Dataset of 11,928 E-Mails using Python, Pandas, PyTorch, Hugging Face.

## How to use it in your projects -

### ***Note - Since the actual model size exceeds the Github and Github LFS Free Limit, the model files aren't included. However, you can generate the model by running the Model_Notebook.ipynb.***

* You can load it using joblib -

  ``` python
  import joblib
  joblib.load("Email_Fraud_Detector_Model.pkl")
  ```
  
### **OR**
  
* You can use hugging face pipeline and import the model using the config in the generated folder -

  ``` python
  from transformers import pipeline
  classifier = pipeline("text-classification", model="./email_fraud_detector/")
  ```
