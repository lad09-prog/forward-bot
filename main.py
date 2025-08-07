import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Включаем логгирование (можно оставить как есть)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Получаем токен бота и ID Лады из переменных окружения
TOKEN = os.getenv(7605576059:AAGf-t-zk6uFyDiOodLw-2Fbo8pbx7j-C0A)
LADA_ID = os.getenv(213640467)  # Например: 123456789

# Приветствие при старте
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Приветик!♥️"
        "Я - бот, который проверяет, есть ли у тебя подписка на Boosty."
        "Напиши, пожалуйста, свой ник на Boosty, чтобы получить доступ к закрытому телеграм-каналу с фотоархивом✨"
    )
    await update.message.reply_text(text)

# Обработка сообщений (никнеймов)
async def forward_to_lada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = f"🆕 Пришло сообщение от @{user.username or 'без ника'} (id {user.id}):\n\n{update.message.text}"
    await context.bot.send_message(chat_id=int(LADA_ID), text=text)

# Запуск приложения
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_lada))
    app.run_polling()
