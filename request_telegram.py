import requests

TOKEN = '5720568741:AAH1BDlfTDlliDQM24gs-Xom9Pq6lrnlryo'
CHANNEL_ID = 5321351707


def send_photo_telegram(token: int, chat_id: int, name_photo: str):
    files = {'photo': open('sity.jpg', 'rb')}
    r = requests.post("https://api.telegram.org/bot" + token + "/sendPhoto?chat_id=" + chat_id, files=files)
    if r.status_code != 200:
        raise Exception("post_text error")


def send_text_telegram(text: str, channel_id: int):
    url = "https://api.telegram.org/bot"
    url += TOKEN
    method = url + "/sendMessage"
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })
    if r.status_code != 200:
        raise Exception("post_text error")

print('Привет мир!')