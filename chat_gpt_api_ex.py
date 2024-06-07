# 본 코드는 2023 DevDay 이후 변경된 최신 문법을 따릅니다.
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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", # 본인의 API KEY로 교체해야합니다.
)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "우울증에 걸린 친구가 있어. 이 친구에게 도움을 줄 수 있는 방법을 10가지 제시해줘",
        }
    ],
    model="gpt-4o",
)
print(completion.choices[0].message.content)