import requests

params = {"q":"pizza"}
r = requests.get("https://www.bing.com/search", params=params)

print("Status:",r.status_code)
code = r.text
print(r.url)

file_html = open("./index.html","w+")
file_html.write(code)