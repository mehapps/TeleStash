from telethon import TelegramClient, events
import asyncio
from secrets import api_hash, api_id

# session.session will store the session data and should be kept secure
client = TelegramClient('session', api_id, api_hash)


async def upload_file_to_telegram(file, caption, file_name):
    try:
        async with client:
            await client.send_file("me", file=file, caption=caption , DocumentAttributeFilename=file_name)
            print("File sent successfully!")
    except Exception as e:
        print(f"Error: {e}")