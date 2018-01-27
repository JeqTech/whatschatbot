# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from app.mac import mac, signals
from chatterbot.trainers import ListTrainer


# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.set_trainer(ListTrainer)
chatbot.train(
    "chatterbot.corpus.portuguese"
)

# Get a response to the input text 'How are you?'
#response = chatbot.get_response('Como vc esta?')




#print(response)

        
@signals.message_received.connect
def handle(message):
    response = chatbot.get_response(str(message.text))
    print(str(message.text))
    
    #response = chatbot.get_response('I would like to book a flight.')
        #response = chatbot.get_response(message)
    mac.send_message(str(response), message.conversation)
    print(response)
    #if float(response.confidence) > 0.4:
    #     mac.send_message(str(response), message.conversation)
    #else:
    #    mac.send_message('não entendi', message.conversation)
           
