import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================
# BOT TOKEN
# =========================
TOKEN = "8823653086:AAFFecnpQ-tTiOQTlrRizihBy7HzfB-LYT8"
import json

# =========================
# ACCESS KEYS
# =========================
try:
    with open("used_keys.json", "r") as f:
        used_keys = json.load(f)
except:
    used_keys = []

bot = telebot.TeleBot(TOKEN)

# =========================
# ACCESS KEYS
# =========================
valid_keys = ["AYUSH123", "VIP2026", "ACCESS777"]
used_keys = []

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    text = """
👋 Welcome to FLASH USDT STORE

⚡ Access premium crypto tools, tutorials, and exclusive services securely in one place.

🔑 Please enter your access key:
"""

    bot.send_message(message.chat.id, text)

# =========================
# KEY VERIFICATION
# =========================
@bot.message_handler(func=lambda message: True, content_types=['text'])
def verify_key(message):

    user_key = message.text.strip()

    if user_key in valid_keys and user_key not in used_keys:

        used_keys.append(user_key)

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "FLASH USDT PURCHASE",
            callback_data="purchase"
        )

        btn2 = InlineKeyboardButton(
            "Crypto Wallet Guide",
            callback_data="wallet"
        )

        btn3 = InlineKeyboardButton(
            "Trading Tutorials",
            callback_data="trade"
        )

        btn4 = InlineKeyboardButton(
            "DARKWEB",
            callback_data="darkweb"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)

        bot.send_message(
            message.chat.id,
            "✅ Access Granted",
            reply_markup=markup
        )

    else:
        bot.send_message(
            message.chat.id,
            "❌ Invalid or Already Used Key"
        )

# =========================
# BUTTON CALLBACKS
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # =========================
    # PURCHASE MENU
    # =========================
    if call.data == "purchase":

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "Starter Pack $30,000",
            callback_data="pack30"
        )

        btn2 = InlineKeyboardButton(
            "Pro Pack $70,000",
            callback_data="pack70"
        )

        btn3 = InlineKeyboardButton(
            "Premium Pack $100,000",
            callback_data="pack100"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.send_message(
            call.message.chat.id,
            "💸 Select Your Package",
            reply_markup=markup
        )

    # =========================
    # PAYMENT GATEWAY
    # =========================
    elif call.data in ["pack30", "pack70", "pack100"]:

        bot.send_message(
            call.message.chat.id,
            """
💳 PAYMENT GATEWAY

📌 Payment Details

USDT BEP20:

0x712707705ec8dcb98c2220e06fd744ba8984991e

✅ Send USDT to this address
✅ Upload payment screenshot for verification
"""
        )

    # =========================
    # WALLET GUIDE
    # =========================
    elif call.data == "wallet":

        bot.send_message(
            call.message.chat.id,
            """
📚 CRYPTO WALLET GUIDE

1. Download Trust Wallet
2. Create Wallet
3. Save Recovery Phrase
4. Add USDT BEP20
5. Start Using Wallet
"""
        )

    # =========================
    # TRADING TUTORIALS
    # =========================
    elif call.data == "trade":

        bot.send_message(
            call.message.chat.id,
            """
📈 TRADING TUTORIALS

• Spot Trading
• Futures Basics
• Risk Management
• Technical Analysis
"""
        )

    # =========================
    # DARKWEB
    # =========================
    elif call.data == "darkweb":

        bot.send_message(
            call.message.chat.id,
            "🌐 Darkweb section coming soon"
        )

# =========================
# SCREENSHOT UPLOAD
# =========================
@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    bot.send_message(
        message.chat.id,
        """
✅ YOUR ORDER HAS BEEN PLACED SUCCESSFULLY

⏳ You will get your FLASH USDT between 1 - 4 hours.

🙏 THANKS FOR VISITING
"""
    )

# =========================
# RUN BOT
# =========================
print("Bot Running...")
bot.remove_webhook()
bot.infinity_polling()