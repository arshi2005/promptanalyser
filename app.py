import streamlit as st
import anthropic

st.title("My AI App")

api_key = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=api_key)

user_input = st.text_input("Ask something:")

if user_input:
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.content[0].text)
