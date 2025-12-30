import streamlit as st
import requests

API = "http://localhost:8000"

st.title("🚀 AI SaaS Platform")

if "token" not in st.session_state:
    st.session_state.token = None

if not st.session_state.token:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        r = requests.post(f"{API}/auth/login", params={
            "email": email,
            "password": password
        })
        if "access_token" in r.json():
            st.session_state.token = r.json()["access_token"]
            st.success("Logged in")
        else:
            st.error("Login failed")

else:
    prompt = st.text_area("Ask AI")
    if st.button("Run"):
        res = requests.post(
            f"{API}/chat",
            params={"prompt": prompt},
            headers={"Authorization": f"Bearer {st.session_state.token}"}
        )
        st.write(res.json())
