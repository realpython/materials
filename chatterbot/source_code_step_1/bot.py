from chatterbot import ChatBot

chatbot = ChatBot("Chatpot")

exit_conditions = (":q", "quit", "exit")
while (query := input("> ")) not in exit_conditions:
    print(f"🪴 {chatbot.get_response(query)}")
