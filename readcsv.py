import csv
import sqlite3
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Alfred',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///baseconhecimento.sqlite3'
              )


arquivo = open('baseconhecimentoalfred.csv')

linhas = csv.reader(arquivo)

with open('baseconhecimentoalfred.csv') as csvfile:
     reader = csv.DictReader(csvfile, delimiter=',')
     pergunta = []
     resposta = []
     perguntasErespostas = []
     for row in reader:
         pergunta.append(row['body'])
         resposta.append(row['answerbody'])
         perguntasErespostas.append(row['body'])
         perguntasErespostas.append(row['answerbody'])

#print(resposta)


try:


    con = sqlite3.connect('baseconhecimento.sqlite3')
    cursor = con.cursor()

    conversa = ListTrainer(bot)
    conversa.train(perguntasErespostas);



    '''
    total = len(pergunta)
    for i in range(0, 30, 1):
        cursor.executemany("INSERT INTO statement (text) VALUES (?);", pergunta[i])
        cursor.executemany("INSERT INTO statement (text) VALUES (?);", resposta[i])
        con.commit()
        print (pergunta[i])
        print (resposta[i])
        print((i*100)/total)
    
    
    # Show conteudo table
    cursor.execute('select text from statement;')
    result = cursor.fetchall()
    print(result)
    '''



    cursor.close()



except sqlite3.Error as error:
    print('Ocorreu um erro - ', error)
  
finally:
    if con:
        con.close()
        print('SQLite Connection closed')


'''

conversa = ListTrainer(bot)
conversa.train([pergunta, resposta
                
                                
                ])

'''

usuario=input("Bom dia! Qual o seu nome? ")
print("Faça uma pergunta!")
while True:
    try:
        resposta = bot.get_response(input(usuario + ": "))
        if float(resposta.confidence) > 0.5:
            print("Alfred: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

