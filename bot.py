import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Read token from environment
BOT_TOKEN = os.getenv("7801001027:AAGyimggZcZmGWRweWDuk3JU5OZ2vzPppks")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Welcome to Sarkari Alert Bot!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
