from telethon import TelegramClient, utils
import os

app_id = app id here
app_hash = "app hash here"

base_folder = "Folder Path"  # Replace this with the base folder path
file_path = "full path here"
file_caption = "caption here"  # Set this to the desired subfolder and file name

def callback(current, total):
    print('Uploaded', current, 'out of', total, 'bytes: {:.2%}'.format(current / total))


with TelegramClient('anon', app_id, app_hash) as client:
    client.loop.run_until_complete(
        client.send_file("me", file_path, caption=file_caption, progress_callback=callback, force_document=True)
    )

