
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import Commands





app = ApplicationBuilder().token("5681380688:AAFNNYX5P0BFtpJQPRSleKI5KN4NNVu2nwE").build()

app.add_handler(CommandHandler("hello", Commands.hello))

app.run_polling()