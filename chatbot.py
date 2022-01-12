from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Alfred',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///baseconhecimento.sqlite3'
              )

conversa = ListTrainer(bot)
conversa.train([
    'Alfred?',
    'Bom dia senhor!',
    'O que é python?',
    'Desculpe a ignorância, mas não seria uma cobra senhor!',
    'Vou lhe treinar melhor Alfred!',
    'Fico feliz em ser util!',
])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Alfred: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break