from backend.retriever import (
    retrieve_legal_context
)

from backend.gemini_response import (
    generate_response
)

def legal_chatbot(query):

    context = retrieve_legal_context(
        query
    )

    response = generate_response(

        query,

        context
    )

    return response