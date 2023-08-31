from telethon.sync import TelegramClient

api_id = '29212374'
api_hash = '4bac9cabf7bf9b9c601374225b8ca206'

with TelegramClient('session2', api_id, api_hash) as client:
    session_file = client.session.save()
    print("Файл сессии сохранен как:", session_file)
