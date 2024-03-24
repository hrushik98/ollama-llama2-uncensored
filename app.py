import streamlit as st
import requests

def send_api_request(api_url, payload):
    response = requests.post(api_url, json=payload)
    return response.json()

def main():
    st.title("API Request App")

    st.subheader("Enter API details")
    api_url = st.text_input("API URL", value="http://64.227.165.237:11434/api/generate")
    model = st.text_input("Model", value="llama2-uncensored")
    prompt = st.text_area("Prompt", value="Why is the sky blue?")
    stream = st.checkbox("Stream", value=False)

    if st.button("Send Request"):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        try:
            response = send_api_request(api_url, payload)
            st.subheader("Response")
            st.json(response)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
