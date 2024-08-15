import streamlit as st
from send_email import send_email

st.header('Contact us ...!')


if 'user_email' not in st.session_state:
    st.session_state.user_email = ''
if 'user_message' not in st.session_state:
    st.session_state.user_message = ''

with st.form(key='email_forms'):
    user_email = st.text_input("Enter your email:", value=st.session_state.user_email)
    user_message = st.text_area("Please enter your message:", value=st.session_state.user_message)
    message = f"""\
Subject : New person contacted us - {user_email}

From : {user_email}

{user_message}

Regrads,
email_Bot

"""
    button = st.form_submit_button("Submit")
    if button :
        send_email(message)
        st.session_state.user_email = ''
        st.session_state.user_message = ''
        st.success("Message sent successfully!")
        

