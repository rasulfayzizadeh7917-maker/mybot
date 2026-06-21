import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# توکن (روی هاست از env استفاده می‌کنیم)
TOKEN = ("8868097103:AAH0xTJ_RSzyLqgpZVDP0NmMvalnq12ZpKg")

# دکمه‌ها
keyboard = ReplyKeyboardMarkup(
    [
        ["💳 خرید اشتراک"],
        ["💰 کیف پول", "➕ شارژ حساب"],
        ["📞 پشتیبانی"]
    ],
    resize_keyboard=True
)

# sub های نمونه
subs = [
    "https://bot.seclink.ir:2096/sub/FI1c2q3Mbg1CqKAM",
    "https://bot.seclink.ir:2096/sub/FI1c2q3Mbg1CqKAM",
    "https://bot.seclink.ir:2096/sub/FI1c2q3Mbg1CqKAM"
]

used = []

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام به ربات WebNet خوش آمدید\n\nاز منو یکی رو انتخاب کن 👇",
        reply_markup=keyboard
    )

# مدیریت پیام‌ها
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == "💳 خرید اشتراک":
        if len(used) < len(subs):
            sub = subs[len(used)]
            used.append(sub)

            await update.message.reply_text(
                f"✅ خرید موفق\n\n🔗 اشتراک شما:\n{sub}"
            )
        else:
            await update.message.reply_text("❌ موجودی اشتراک تمام شده")

    elif text == "💰 کیف پول":
        await update.message.reply_text("💰 موجودی شما: 0 تومان\n(سیستم کیف پول در مرحله بعد اضافه میشه)")

    elif text == "➕ شارژ حساب":
        await update.message.reply_text(
    "💳 برای شارژ حساب:\n\n"
    "به کارت زیر واریز کن:\n"
    "6037-9915-5454-8531\n"
    "رسول فیضی زاده\n\n"
    "بعد عکس رسید رو بفرست 📩"
)

    elif text == "📞 پشتیبانی":
        await update.message.reply_text("@webnet19_Support")

# ساخت ربات
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🤖 Bot is running...")
app.run_polling()
