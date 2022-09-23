from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train(["Hi", "Welcome, friend 🤗"])
trainer.train(["Are you a plant?", "No, I'm the pot below the plant!"])

exit_conditions = (":q", "quit", "exit")
while (query := input("> ")) not in exit_conditions:
    print(f"🪴 {chatbot.get_response(query)}")
