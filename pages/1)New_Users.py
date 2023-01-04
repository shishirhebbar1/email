import streamlit as st
from datetime import datetime
st.header("SCAN THE QR CODE TO PROCEED WITH PAYMENT:")
st.image(
    "https://drive.google.com/file/d/1i7k-5t3-Xln8thczboyFrikljJZcpp8_/view?usp=share_link",
    # Manually Adjust the width of the image as per requirement
)
f = open("test3.txt", "a")
d = st.text_input("ENTER YOUR EMAIL ID TO ENTER WAIT LIST: ")
st.write("YOUR MAIL ID WILL BE ADDED TO THE USER LIST AT 12AM IST")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
f.write("\n")
f.write(d)
f.write("\t")
f.write(dt_string)
f.close()
