import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '8654991406:AAE8srdYpBo45rjez_iN39ihWGtlXdB1xXo'

JAKE = [
    "يا صاح، الفشل هو أول خطوة لتبدأ في أن تكون بارعاً! 🎸",
    "اممم... هل قال أحدهم شطيرة؟ 🥪 أنا مستعد دائماً للأكل والنوم.",
    "أوه يا صاح، استرخِ ودع جسدك يتمدد مثل المعكرونة! 🧘‍♂️",
    "فين؟! أين فين؟ أوه، أنت لست فين... لكنك تبدو رائعاً!",
    "تذكر دائماً: القوانين مثل المطاط، يمكننا تمطيطها قليلاً! 🤫"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً يا صاح! 🐾 أنا جيك.. ما هي المغامرة اليوم؟ 🥪✨")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if any(w in text for w in ["جوعان", "أكل", "شطيرة"]):
        res = "أوه! الأكل لغتي المفضلة! 😋 سأصنع لك شطيرة سحرية!"
    elif any(w in text for w in ["حزين", "تعبان", "ضوجة"]):
        res = "هون عليك يا صاح.. 🎸 خذ نفساً عميقاً، وتذكر أن المغامرة مستمرة."
    else:
        res = random.choice(JAKE)
    await update.message.reply_text(res)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("جيك جاهز...")
    app.run_polling()

if __name__ == '__main__':
    main()
