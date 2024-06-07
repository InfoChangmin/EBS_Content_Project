import pathlib
import textwrap
import PIL.Image
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyA-v85yCnqD8hfAV2cjdFIFscGqXiCbwsM" # 내 API키로 변경
genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open('photo.jpg')
#model = genai.GenerativeModel('gemini-pro-vision') # 2023.12까지의 기억 (이미지 작업에 특화)
#model = genai.GenerativeModel('gemini-1.5-pro-latest') # 2024.4까지의 기억 (코딩, 추천 생성, 정보 추출, AI 에이전트에 특화)
model = genai.GenerativeModel('gemini-1.5-flash') # 소형 모델

response = model.generate_content(img)

print(response.text)