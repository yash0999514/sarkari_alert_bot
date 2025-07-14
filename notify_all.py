from telegram import Bot
import time

BOT_TOKEN = "7801001027:AAGyimggZcZmGWRweWDuk3JU5OZ2vzPppks"  # Same token as in bot.py
bot = Bot(token=BOT_TOKEN)

message = """
📢 *New Job Alert!*

🔹 MPSC Group C 2025
📅 Notification Date: 1 August
🔗 https://mpsc.gov.in/
"""

# Send to all subscribers
with open("subscribers.txt", "r") as file:
    chat_ids = set(file.read().splitlines())

for chat_id in chat_ids:
    try:
        bot.send_message(chat_id=int(chat_id), text=message, parse_mode="Markdown")
        print(f"✅ Sent to {chat_id}")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Failed for {chat_id}: {e}")
