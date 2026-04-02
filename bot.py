from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("rename-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def rename(client, message):
    file = message.document
    new_name = "Renamed_" + file.file_name
    
    await message.reply_document(
        document=file.file_id,
        file_name=new_name,
        caption="✅ Berhasil di rename"
    )

app.run()
