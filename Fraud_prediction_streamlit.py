import pandas as pd
import joblib
import streamlit as st

model = joblib.load("fraud_cb.pkl")

steps = st.number_input('Time (1 signifying 1 hr)', min_value=1, max_value=744)
type = st.selectbox("Payment Type", options=['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount = st.number_input("Amount", min_value=0, max_value=5000000)
transaction_type = st.selectbox("Kind of transaction", options=['CM', 'CC'])
net_sender = st.number_input("Net amount sent", min_value=0, max_value=5000000)
net_receiver = st.number_input("Net amount received", min_value=0, max_value=30000000)

input_data = {
    "step": "steps",
    "type": "types",
    "amount": "amount",
    "transaction_type": "transaction_type",
    "net_sender": "net_sender",
    "net_receiver": "net_sender"
}

def predict_fraud(input_data):
    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)
    return prediction

if st.button("Predict Fraud"):
    prediction = predict_fraud(input_data)

    if prediction == 0:
        st.info("Transaction Status: NOT FRAUD")
    else:
        st.info("Transaction Status: FRAUD")
    