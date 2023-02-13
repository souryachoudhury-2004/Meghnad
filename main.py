import streamlit as st
from email_sender import mail

st.title("Meghnad: A Simple Email Assistant.")

with st.form(key="email_editor"):
    email_address = st.text_input("Enter your email address.")
    receiver_email = st.text_input("Enter email address of receiver.")
    subject = st.text_input("Enter subject...")
    raw_message = st.text_area("Write your email here...")
    message = f"Subject:{subject}\n\n From: {email_address} \n\n {raw_message}"
    submit_button = st.form_submit_button("Send!")
    try:
        if submit_button:
            if email_address == "":
                st.info("Please enter your email address!")
            elif receiver_email == "":
                st.info("Please enter the receiver's email address!")
            else:
                mail(receiver_email, message)
                st.info("Email sent successfully!")
    except:
        st.info("There was an error in sending the email!")



