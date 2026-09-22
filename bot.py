import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
WEBHOOK_URL = "https://snaptrend.onrender.com/" + TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك في SnapTrend Morocco! 🇲🇦")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    webhook_url=WEBHOOK_URL,
)
