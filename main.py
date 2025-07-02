import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@lang_box"  # آیدی کانال شما

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not user:
        return

    member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user.id)
    if member.status in ["left", "kicked"]:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_ID[1:]}")],
            [InlineKeyboardButton("✅ بررسی عضویت", callback_data="check_member")]
        ]
        await update.message.reply_text("برای استفاده از ربات ابتدا در کانال عضو شوید 👇", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    keyboard = [
        [InlineKeyboardButton("📥 دانلود از اینستا", callback_data="insta")],
        [InlineKeyboardButton("🎵 دانلود آهنگ", callback_data="music")],
        [InlineKeyboardButton("📹 دانلود تیک‌تاک", callback_data="tiktok")],
        [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
    ]
    await update.message.reply_text("یکی از گزینه‌ها رو انتخاب کن:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "check_member":
        await start(update, context)
    elif data == "insta":
        await query.edit_message_text("لینک پست اینستاگرام رو بفرست 📷")
    elif data == "tiktok":
        await query.edit_message_text("لینک ویدیو تیک‌تاک رو بفرست 🎬")
    elif data == "music":
        await query.edit_message_text("اسم یا لینک آهنگ رو بفرست 🎧")
    elif data == "back":
        await start(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("در حال پردازش لینک... ⏳ (این قسمت باید توسط API خارجی تکمیل شود.)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
