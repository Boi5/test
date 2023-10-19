import requests
import json
from googletrans import Translator #googletrans-4.0.0rc1

url = "https://api.ai21.com/studio/v1/paraphrase"


def paraphrase(text) -> str:
    payload = {
    "style": "general",
    "text": f"{text}"
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer  pdvno5sjFBbj5O3bNMmnQCHPUXQBDiDT"
    }
    response = requests.post(url, json=payload, headers=headers)
    #print(json.loads(response.text)["suggestions"][0]['text'])
    return json.loads(response.text)["suggestions"][0]['text']

def translate(text) -> str:
    translator = Translator()
    PText = translator.translate(text, src='en', dest='ar')
    return PText.text

def remove_debris(text) -> str:
    PText =str.replace(text, '/n', '.')
    PText =str.replace(text, 'Subscribe to RT', '')
    PText =str.replace(text, '[ Categories / Add folder ]', '')

    return PText

