from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

API_TOKEN = 'TOKEN'  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Я загадал число от 1 до 1000. Попробуй угадать!")
    number_to_guess = random.randint(1, 1000)
    context.user_data['number_to_guess'] = number_to_guess

async def guess_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number_to_guess = context.user_data.get('number_to_guess')

    if number_to_guess is None:
        await update.message.reply_text("Сначала начните игру с командой /start.")
        return

    try:
        guess = int(update.message.text)
        if guess < number_to_guess:
            await update.message.reply_text("Слишком маленькое число! Попробуйте снова.")
        elif guess > number_to_guess:
            await update.message.reply_text("Слишком большое число! Попробуйте снова.")
        else:
            await update.message.reply_text("Поздравляю! Вы угадали число!")
            context.user_data['number_to_guess'] = None  # Сбросить игру
    except ValueError:
        await update.message.reply_text("Пожалуйста, вводите только числа.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess_number))

    application.run_polling()