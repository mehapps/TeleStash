from upload import upload_file, client
import asyncio

# with client:
#     client.loop.run_until_complete(upload_file("test4.txt", "It worked!2"))


async def blah():
    await upload_file("test4.txt", "It worked!2")

asyncio.run(blah())