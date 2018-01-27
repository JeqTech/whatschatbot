from app.mac import mac, signals
#from chatterbot.trainers import ListTrainer



@signals.message_received.connect
def handle(message):
    #message.log() to see message object properties
    if message.text == "hi":
        mac.send_message("Hello", message.conversation)
        mac.send_message("Qual o teu nome? Meu nome é sei lá", message.conversation)
        #mac.send_image("path/to/image.png", message.conversation)
        #mac.send_video("path/to/video.mp4", message.conversation)
    elif message.text == "Eduardo":
        mac.send_message("prazer, Eduardo", message.conversation)