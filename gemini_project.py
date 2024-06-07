import google.generativeai as genai

#GOOGLE_API_KEY="YOUR-API-KEY" # 내 API키로 변경
GOOGLE_API_KEY="AIzaSyA-v85yCnqD8hfAV2cjdFIFscGqXiCbwsM" # 내 API키로 변경

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
#model = genai.GenerativeModel('gemini-1.5-pro-latest') # 2024.4까지의 기억 (코딩, 추천 생성, 정보 추출, AI 에이전트에 특화)

response = model.generate_content("오늘 저녁 메뉴 추천 10개 가즈아!, 참고로 나는 한식과 일식을 좋아하니까 관련해서 추천해줘!")

print(response.text)