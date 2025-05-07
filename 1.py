from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Используй команду /play для игры!")

# Обработчик команды /play
async def play(update: Update, context: CallbackContext) -> None:
    # Ссылка на Web App (GitHub Pages, Vercel или другой хостинг)
    keyboard = [
        [InlineKeyboardButton("🎰 Играть в слот", web_app=WebAppInfo(url="https://username.github.io/game-web-app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Запускай свою удачу!", reply_markup=reply_markup)

# Основной запуск
def main():
    TOKEN = 'YOUR_BOT_TOKEN'  # Замените на ваш токен

    # Создаем приложение для бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))  # Команда для игры

    # Начинаем работу бота
    application.run_polling()

if __name__ == '__main__':
    main()
