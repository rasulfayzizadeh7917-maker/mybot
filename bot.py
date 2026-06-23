import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
TOKEN = os.getenv("8868097103:AAHTUjAuYRnmLX7imVoGLJs5znt_7XTvbSY") 

ADMIN_ID = 6248357302

CARD_NUMBER = "6037-9915-5454-8531"
CARD_OWNER = "رسول فیضی زاده"

# کیبورد اصلی
main_keyboard = ReplyKeyboardMarkup(
    [
        ["💳 خرید اشتراک"],
        ["💰 کیف پول", "➕ شارژ حساب"],
        ["📞 پشتیبانی"],
    ],
    resize_keyboard=True,
)

# کیبورد خرید
buy_keyboard = ReplyKeyboardMarkup(
    [
        ["🔹 10 گیگ - 180 هزار"],
        ["🔹 20 گیگ - 300 هزار"],
        ["🔹 30 گیگ - 400 هزار"],
        ["🔹 40 گیگ - 500 هزار"],
        ["🔹 50 گیگ - 600 هزار"],
        ["🔙 بازگشت"],
    ],
    resize_keyboard=True,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 به WebNet خوش آمدید\n\nلطفاً از منو انتخاب کنید.",
        reply_markup=main_keyboard,
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💳 خرید اشتراک":
        await update.message.reply_text(
            "📦 پلن موردنظر را انتخاب کنید:",
            reply_markup=buy_keyboard,
        )

    elif text == "🔹 10 گیگ - 180 هزار":
        context.user_data["plan"] = "10 گیگ"
        await update.message.reply_text(
            f"📦 پلن: 10 گیگ\n\n"
            f"💰 مبلغ: 180,000 تومان\n\n"
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            f"📸 بعد از پرداخت، عکس رسید را ارسال کنید."
        )

    elif text == "🔹 20 گیگ - 300 هزار":
        context.user_data["plan"] = "20 گیگ"
        await update.message.reply_text(
            f"📦 پلن: 20 گیگ\n\n"
            f"💰 مبلغ: 300,000 تومان\n\n"
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            f"📸 بعد از پرداخت، عکس رسید را ارسال کنید."
        )

    elif text == "🔹 30 گیگ - 400 هزار":
        context.user_data["plan"] = "30 گیگ"
        await update.message.reply_text(
            f"📦 پلن: 30 گیگ\n\n"
            f"💰 مبلغ: 400,000 تومان\n\n"
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            f"📸 بعد از پرداخت، عکس رسید را ارسال کنید."
        )

    elif text == "🔹 40 گیگ - 500 هزار":
        context.user_data["plan"] = "40 گیگ"
        await update.message.reply_text(
            f"📦 پلن: 40 گیگ\n\n"
            f"💰 مبلغ: 500,000 تومان\n\n"
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            f"📸 بعد از پرداخت، عکس رسید را ارسال کنید."
        )

    elif text == "🔹 50 گیگ - 600 هزار":
        context.user_data["plan"] = "50 گیگ"
        await update.message.reply_text(
            f"📦 پلن: 50 گیگ\n\n"
            f"💰 مبلغ: 600,000 تومان\n\n"
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            f"📸 بعد از پرداخت، عکس رسید را ارسال کنید."
        )

    elif text == "💰 کیف پول":
        await update.message.reply_text("💰 موجودی شما: 0 تومان")

    elif text == "➕ شارژ حساب":
        await update.message.reply_text(
            f"💳 شماره کارت:\n{CARD_NUMBER}\n\n"
            f"👤 صاحب حساب:\n{CARD_OWNER}\n\n"
            "📸 بعد از واریز رسید را ارسال کنید."
        )

    elif text == "📞 پشتیبانی":
        await update.message.reply_text("@webnet19_Support")

    elif text == "🔙 بازگشت":
        await update.message.reply_text(
            "🏠 منوی اصلی",
            reply_markup=main_keyboard,
        )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    plan = context.user_data.get("plan", "نامشخص")

    await update.message.reply_text(
        "✅ رسید شما دریافت شد.\n\n"
        "پس از بررسی، اشتراک برای شما ارسال خواهد شد."
    )

    caption = (
        f"🧾 رسید جدید\n\n"
        f"👤 کاربر: {user.first_name}\n"
        f"🆔 {user.id}\n"
        f"📦 پلن: {plan}"
    )

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=update.message.photo[-1].file_id,
        caption=caption,
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()