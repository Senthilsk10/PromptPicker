import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]
st.write("this is my first streamlit app")
prompt = "how are you doing"
response = openai.Completion.create(
  engine='text-davinci-curie',prompt = prompt,
  max_tokens=10)

completion_text = response.choices[0].text.strip()
st.write(completion_text)
