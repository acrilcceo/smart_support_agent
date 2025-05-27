import openai

openai.api_key = "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"  
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="deepseek-r1:free", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)

print(response["choices"][0]["message"]["content"])
