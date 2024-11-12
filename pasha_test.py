from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция, которая будет отправлять сообщение при старте
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я запущен и готов работать.')

def main():
    # Вставьте сюда ваш токен, который вы получили от BotFather
    token = '1960203476:AAH6Uu-ND22H3TecmlGXXox1icnBJamrkGw'

    # Создаём объект Application с токеном
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
