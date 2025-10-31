async def run_chat(handler) -> None:
    """Run an AI-handled chat session."""
    print("\nMCP Client's Chat Started!")
    print("Type your queries or 'quit' to exit.")

    while True:
        try:
            if not (query := input("\nYou: ").strip()):
                continue
            if query.lower() == "quit":
                break

            print("\n" + await handler.process_query(query))
        except Exception as e:
            print(f"\nError: {str(e)}")

    print("\nGoodbye!")
