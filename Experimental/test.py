import requests, json
query = "Round-robin scheduling allows interactive tasks quicker access to the processor"
query = query.replace(" ","+")
print(query)
answer = requests.get(f"http://duckduckgo.com/?q={query}&t=h_&ia=web")
print(answer.content)
print(answer)
"""formated_reponse = json.dumps(json.loads(answer.text), indent=4, sort_keys=True)
with open("test.json","w",encoding='utf8') as f:
    f.writelines(formated_reponse)"""
