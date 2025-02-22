import streamlit as st
from PIL import Image
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")
st.title("GenAI - Image Tags , Title , Alt generator")
st.markdown("---")
st.subheader("Upload your image")
system_prompts = '''generate  five to six TAGs WHICH SUITS THE IMAGE and a title for the image and one alternative text only and only in this particluar format "ALT : -   , TITLE : -   , TAGS :- " remeber that both the information is for the html alt and title tags for seo ranking it as to be short and precise and not too long just short just the out put of the tags and the title and the alt text  and no other information and no unwanted text   '''
file = st.file_uploader("Upload an image", type=["jpg", "png"])
if st.button("Generate"):
  image = Image.open(file)
  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=[image, system_prompts])
  st.subheader("response : ")
  print(response.text)
  st.write(response.text)
