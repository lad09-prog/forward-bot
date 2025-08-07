from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes

YOUR_ID = 213640467  # замени на свой Telegram ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Приветик, напиши, пожалуйста,свой ник на Boosty♥️")

async def forward_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    message = f"💬 Новый пользователь:\nID: {user_id}\nUsername: @{username}\n\nСообщение: {user_text}"
    await context.bot.send_message(chat_id=YOUR_ID, text=message)

app = ApplicationBuilder().token("7605576059:AAGf-t-zk6uFyDiOodLw-2Fbo8pbx7j-C0A").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_me))

app.run_polling()
