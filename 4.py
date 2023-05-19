import re
import requests

response = requests.get("https://httpbin.org/forms/post")
html_content = response.text

form_fields = {}
input_fields = re.findall(r'<input\s+name="([^"]*)"\s*value="([^"]*)"', html_content)
for field_name, _ in input_fields:
    form_fields[field_name] = input(f"{field_name}: ")

response = requests.post("https://httpbin.org/post", data=form_fields)
print(response.text)
