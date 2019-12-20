import requests

url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

querystring = {"source":"en","target":"es","input":"This is nice."}

headers = {
    'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
    'x-rapidapi-key': "2159163aa6mshffb1e66316df886p15215ajsnea800f3221a0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
