#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 00:10:33 2018

@author: macbook
"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

from app.mac import mac, signals

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.set_trainer(ListTrainer)
# Train based on the english corpus
chatbot.train("chatterbot.corpus.portuguese")

# Get a response to an input statement
#chatbot.get_response("Oi, como vc esta?")
'''while True:
    quest = input('Voce: ')
    
    response = chatbot.get_response(quest)
    if float(response.confidence) > 0.4:
        print('Bot: ', response)
    else:
        print('não entendi')'''

        
@signals.message_received.connect
def handle(message):
    if message.text == "ok":
        
        response = chatbot.get_response(message)
        mac.send_message(str(response), message.conversation)
    #if float(response.confidence) > 0.4:
    #    mac.send_message(response, message.conversation)
    #else:
    #    print(response, message.conversation)
           
