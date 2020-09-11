from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
eng_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(eng_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def getbotresponse():
    usertext=request.args.get('msg')
    return str(eng_bot.get_response(usertext))

if __name__ == '__main__':
    app.run()
