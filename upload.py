from telethon import TelegramClient, events
import asyncio
import secrets

# Replace 'session_name' with a unique name for your session file
# This file will store the session data and should be kept secure
client = TelegramClient('session_name', api_id, api_hash)


async def upload_file(file_name, caption):
    try:
        async with client:
            await client.send_file("me", file=file_name, caption=caption)
            print("File sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Replace 'file_name' with the path to the file you want to send
    file_name = "test4.txt"

    # Replace 'caption' with the caption you want to include with the file
    caption = "This is the caption for the file!"

   