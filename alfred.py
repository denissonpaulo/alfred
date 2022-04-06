import csv
import sqlite3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

alfred = ChatBot('Alfred',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///baseconhecimento.sqlite3'
              )

with open('baseconhecimentoalfred.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    perguntasErespostas = []
    for row in reader:
        perguntasErespostas.append(row['title'])
        perguntasErespostas.append(row['answerbody'])

try:

    # Teste conexão com o banco
    con = sqlite3.connect('baseconhecimento.sqlite3')
    cursor = con.cursor()
    print("Conexão ao banco ok!")
    cursor.close()

    '''
    conversa = ListTrainer(bot)
    conversa.train(perguntasErespostas)
    
    conversa.train([
        'Alfred?',
        'Bom dia senhor!',
        'O que é python?',
        'Desculpe a ignorância, mas não seria uma cobra senhor!',
        'Vou lhe treinar melhor Alfred!',
        'Fico feliz em ser util!',])

    '''

except sqlite3.Error as error:
    print('Ocorreu um erro - ', error)

finally:
    if con:
        con.close()
        print('SQLite Conexão Encerrada!')



usuario=input("Bom dia! Eu sou Alfred, serei seu par no desenvolvimento do seu software. Qual o seu nome? ")
print("Faça uma pergunta!")

while True:
    try:
        resposta = alfred.get_response(input(usuario + ": "))
        if float(resposta.confidence) > 0.5:
            print("Alfred: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
