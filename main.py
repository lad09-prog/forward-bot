import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Токен бота
BOT_TOKEN = "7605576059:AAGf-t-zk6uFyDiOodLw-2Fbo8pbx7j-C0A"

# Telegram ID владельца (твой)
OWNER_ID = 213640467

# Сообщение при старте
WELCOME_MESSAGE = (
    "Приветик!🧸"
    "Это бот, который поможет получить доступ к закрытому архиву."
    "Напиши, пожалуйста, свой ник на Boosty, чтобы я могла проверить и добавить тебя✨🙂‍↕️"
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

# Обработка текста от пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username or "без username"
    text = update.message.text

    message_to_owner = (
        f"✉️ Новый пользователь написал боту\n"
        f"Username: @{username}\n"
        f"Boosty ник: {text}"
    )

    await context.bot.send_message(chat_id=OWNER_ID, text=message_to_owner)

# Запуск приложения
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
