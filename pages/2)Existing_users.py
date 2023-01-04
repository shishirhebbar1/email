import os
import openai
import streamlit as st
from Google import Create_Service
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
st.title("Ez-mail")
# Load your API key from an environment variable or secret management service
openai.api_key = "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"
prompt = ("write an email about" +
          st.text_input("DESCRIBE EMAIL IN ONE LINE : "))
if st.button('SEND TO DRAFTS'):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
    a = response["choices"]
    b = a[0]
    CLIENT_SECRET_FILE = "client.json"
    API_NAME = "gmail"
    API_VERSION = "v1"
    SCOPES = ["https://mail.google.com/"]
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    mimeMessage = MIMEMultipart()
    mimeMessage["subject"] = "SAMPLE EMAIL"
    msg_body = b["text"]
    mimeMessage.attach(MIMEText(msg_body, "plain"))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    response = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw_string}}).execute()
    os.remove("token_gmail_v1.pickle")
