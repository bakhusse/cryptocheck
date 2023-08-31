from telethon.sync import TelegramClient

api_id = '22934263'
api_hash = '2cb5519ade6554f94a54a251f08ba09a'

with TelegramClient('session_name', api_id, api_hash) as client:
    session_file = client.session.save()
    print("Файл сессии сохранен как:", session_file)
