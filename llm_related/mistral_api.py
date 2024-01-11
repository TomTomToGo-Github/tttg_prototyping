import requests

url = "https://api.mistral.ai/v1/chat/completions"
token = "API_KEY"
model = "mistral-medium"  # mixtral 8x7B is mistral-small -> both open source to host by oneself
# medium might be uncensored!, mixtral is cencored

prompt = """
John and Mark are in a room with a ball, a basket and a box. John puts the ball in the box, then leaves for work. While John is away, Mark puts the ball in the basket, and then leaves for school. They both come back together later in the day, and they do not know what happened in the room after each of them left the room. Where do they think the ball is?
"""

headers = {
    'Authorization': f'Bearer {token}'
}

data = {
    "model": model,
    "messages": [{"role": "user", "content": prompt}]
  }

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    response_json = response.json()
    content = response_json['choices'][0]['message']['content']
    print(content)
else:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)
   