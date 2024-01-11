
import json

with open('marketing_cynthia.json') as f:
    chat_data = json.load(f)

data_extracted = {chat['title']: None for chat in chat_data}
for chat in chat_data:
    title = chat['title']
    for response_id, response in chat['mapping'].items():
        if data_extracted[title] is None:
            data_extracted[title] = []
        if response.get('message'):
            data_extracted[title].extend(response.get('message').get('content', {}).get('parts', []))


for num, item in enumerate(data_extracted[title]):
    person = 'Cynthia' if not (num % 2) else 'ChatGPT'
    print(f"\n\n\n##################### {person} Anfang ############################\n")  # Print a blank line
    print(item)
    print(f"\n##################### {person} Ende ############################\n")  # Print a blank line


len(data_extracted)