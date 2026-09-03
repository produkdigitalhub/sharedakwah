from telethon import TelegramClient

# Dapatkan dari my.telegram.org
api_id = 'ISI_API_ID_KAMU'
api_hash = 'ISI_API_HASH_KAMU'

async def get_telegram_posts(channel_username, limit=5):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        posts = []
        async for message in client.iter_messages(channel_username, limit=limit):
            if message.text:
                posts.append({
                    "source": f"Telegram (@{channel_username})",
                    "date": message.date.strftime("%Y-%m-%d %H:%M:%S"),
                    "caption": message.text
                })
        return posts
