import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler

from whisper_service import transcribe_audio
from gpt_service import translate_to_official_speech

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я тут подбираю слова. Напиши мне или скажи как есть, а я переведу это на корпоративный язык"
    )

app.add_handler(CommandHandler("start", handle_start))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.voice:
            voice = await update.message.voice.get_file()
            file_path = await voice.download_as_bytearray()
            input_text = transcribe_audio(file_path)
        else:
            input_text = update.message.text

        reply = await translate_to_official_speech(input_text)
        await update.message.reply_text(reply)

    except Exception:
        await update.message.reply_text("⚠️ Что-то пошло не так. Попробуй снова позже.")

app.add_handler(MessageHandler(filters.TEXT | filters.VOICE, handle_message))

if __name__ == "__main__":
    app.run_polling()