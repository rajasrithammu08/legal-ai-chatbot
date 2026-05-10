from chatbot_pipeline import (
    legal_chatbot
)

query = input(
    "Ask legal question: "
)

response = legal_chatbot(query)

print("\nLegal Answer:\n")

print(response)