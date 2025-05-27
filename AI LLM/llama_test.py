import requests

API_KEY = "92269fefcc8df100e2d395daab78ba62c0f3b64dbd477227020dce924e7821fe"  

url = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain how airplanes fly in simple terms."}
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    reply = result['choices'][0]['message']['content']
    print("AI Response:", reply)
else:
    print("Error:", response.status_code, response.text)
