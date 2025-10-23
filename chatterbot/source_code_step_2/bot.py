from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train(["Hi", "Welcome, friend 🤗"])
trainer.train(["Are you a plant?", "No, I'm the pot below the plant!"])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
