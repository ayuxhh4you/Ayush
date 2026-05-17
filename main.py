import telebot
import os
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================
# BOT TOKEN
# =========================
TOKEN = "8823653086:AAFFecnpQ-tTiOQTlrRizihBy7HzfB-LYT8"

HF_TOKEN = os.getenv("HF_TOKEN")
ADMIN_ID = 5529660709

bot = telebot.TeleBot(TOKEN)

# =========================
# LOAD USED KEYS
# =========================
try:
    with open("used_keys.json", "r") as f:
        used_keys = json.load(f)
        if not isinstance(used_keys, list):
            used_keys = []
except:
    used_keys = []

# =========================
# VALID KEYS
# =========================
valid_keys = [
"GTA1029","GTA2048","GTA3091","GTA4182","GTA5203","GTA6371","GTA7482","GTA8593","GTA9604",
"VIP1120","VIP2231","VIP3342","VIP4453","VIP5564","VIP6675","VIP7786","VIP8897","VIP9908",
"PRO1001","PRO2002","PRO3003","PRO4004","PRO5005","PRO6006","PRO7007","PRO8008","PRO9009",
"ULTRA1111","ULTRA2222","ULTRA3333","ULTRA4444","ULTRA5555","ULTRA6666","ULTRA7777","ULTRA8888","ULTRA9999",
"BOOST1010","BOOST2020","BOOST3030","BOOST4040","BOOST5050","BOOST6060","BOOST7070","BOOST8080","BOOST9090",
"MOD1100","MOD2200","MOD3300","MOD4400","MOD5500","MOD6600","MOD7700","MOD8800","MOD9900",
"FLASH1234","FLASH2345","FLASH3456","FLASH4567","FLASH5678","FLASH6789","FLASH7890","FLASH8901","FLASH9012",
"ROCK1110","ROCK2220","ROCK3330","ROCK4440","ROCK5550","ROCK6660","ROCK7770","ROCK8880","ROCK9990",
"GAME1000","GAME2000","GAME3000","GAME4000","GAME5000","GAME6000","GAME7000","GAME8000","GAME9000",
"XTRA1112","XTRA2223","XTRA3334","XTRA4445","XTRA5556","XTRA6667","XTRA7778","XTRA8889","XTRA9991",
"GTA1111","GTA2222","GTA3333","GTA4444","GTA5555","GTA6666","GTA7777","GTA8888","GTA9999",

"VIP1011","VIP2022","VIP3033","VIP4044","VIP5055","VIP6066","VIP7077","VIP8088","VIP9099",
"PRO1110","PRO2220","PRO3330","PRO4440","PRO5550","PRO6660","PRO7770","PRO8880","PRO9990",
"ULTRA1201","ULTRA2302","ULTRA3403","ULTRA4504","ULTRA5605","ULTRA6706","ULTRA7807","ULTRA8908","ULTRA9009",
"BOOST1212","BOOST2323","BOOST3434","BOOST4545","BOOST5656","BOOST6767","BOOST7878","BOOST8989","BOOST9091",
"MOD1230","MOD2340","MOD3450","MOD4560","MOD5670","MOD6780","MOD7890","MOD8900","MOD9010",

"FLASH1001","FLASH2002","FLASH3003","FLASH4004","FLASH5005","FLASH6006","FLASH7007","FLASH8008","FLASH9009",
"ROCK1010","ROCK2020","ROCK3030","ROCK4040","ROCK5050","ROCK6060","ROCK7070","ROCK8080","ROCK9090",
"GAME1111","GAME2222","GAME3333","GAME4444","GAME5555","GAME6666","GAME7777","GAME8888","GAME9999",
"XTRA1000","XTRA2000","XTRA3000","XTRA4000","XTRA5000","XTRA6000","XTRA7000","XTRA8000","XTRA9000",

"KEY1001","KEY1002","KEY1003","KEY1004","KEY1005","KEY1006","KEY1007","KEY1008","KEY1009",
"KEY2001","KEY2002","KEY2003","KEY2004","KEY2005","KEY2006","KEY2007","KEY2008","KEY2009",
"KEY3001","KEY3002","KEY3003","KEY3004","KEY3005","KEY3006","KEY3007","KEY3008","KEY3009",
"KEY4001","KEY4002","KEY4003","KEY4004","KEY4005","KEY4006","KEY4007","KEY4008","KEY4009",
"KEY5001","KEY5002","KEY5003","KEY5004","KEY5005","KEY5006","KEY5007","KEY5008","KEY5009",

"ACCESS111","ACCESS222","ACCESS333","ACCESS444","ACCESS555","ACCESS666","ACCESS777","ACCESS888","ACCESS999",
"POWER111","POWER222","POWER333","POWER444","POWER555","POWER666","POWER777","POWER888","POWER999"
]

# =========================
# START
# =========================
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        """👋 Welcome to FLASH USDT STORE

⚡️ Access premium crypto tools, tutorials, and exclusive services securely in one place.

🔑 Please enter your access key:\n"""
    )

# =========================
# KEY CHECK
# =========================
@bot.message_handler(func=lambda message: True, content_types=['text'])
def verify_key(message):

    user_key = message.text.strip()

    if user_key in valid_keys and user_key not in used_keys:

        used_keys.append(user_key)

        with open("used_keys.json", "w") as f:
            json.dump(used_keys, f)

        markup = InlineKeyboardMarkup()

        markup.add(
            InlineKeyboardButton("FLASH USDT PURCHASE", callback_data="purchase"),
            InlineKeyboardButton("Crypto Wallet", callback_data="wallet"),
            InlineKeyboardButton("Trading Tutorials", callback_data="trade"),
            InlineKeyboardButton("DARKWEB", callback_data="darkweb")
        )

        bot.send_message(message.chat.id, "✅ Access Granted", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "❌ Invalid or Already Used Key")

# =========================
# CALLBACKS
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "purchase":

        markup = InlineKeyboardMarkup()

        markup.add(
            InlineKeyboardButton("Starter $120 / $30K", callback_data="pack30"),
            InlineKeyboardButton("Pro $220 / $70K", callback_data="pack70"),
            InlineKeyboardButton("Premium $320 / $100K", callback_data="pack100")
        )

        bot.send_message(call.message.chat.id, "💸 Select Package", reply_markup=markup)

    elif call.data in ["pack30", "pack70", "pack100"]:

        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("✅ DONE", callback_data="done")
        )

        bot.send_message(
            call.message.chat.id,
            """💳 PAYMENT GATEWAY

USDT BEP20:
0x712707705ec8dcb98c2220e06fd744ba8984991e

📩 Send screenshot + ERC20 address to:
tokenshop9999@gmail.com

After sending, click DONE button below.
""",
            reply_markup=markup
        )

    elif call.data == "wallet":
        bot.send_message(call.message.chat.id,
        "📚 CRYPTO WALLET GUIDE\n\n1. Trust Wallet\n2. Create Wallet\n3. Save Recovery Phrase\n4. Add USDT BEP20\n5. Start Using")

    elif call.data == "trade":
        bot.send_message(call.message.chat.id,
        "📈 Trading Tutorials\n• Spot Trading\n• Futures\n• Risk Management")

    elif call.data == "darkweb":
        bot.send_message(call.message.chat.id, "🌐 Coming Soon")

    elif call.data == "done":
        bot.send_message(
            call.message.chat.id,
            """Token Shop💲: ✅ YOUR ORDER HAS BEEN PLACED SUCCESSFULLY

⏳ Processing Time: 1 - 4 Hours

🙏 Thanks for visiting"""
        )

# =========================
# RUN BOT
# =========================
print("Bot Running...")
bot.infinity_polling()