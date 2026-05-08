from chatterbot import ChatBot

chatbot = ChatBot(
    "Chatpot",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
        },
        {
            "import_path": "chatterbot.logic.OllamaLogicAdapter",
            "model": "llama3.2:latest",
            "host": "http://localhost:11434",
        },
    ],
)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
