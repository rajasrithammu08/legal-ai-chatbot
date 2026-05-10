from flask import (

    Flask,

    render_template,

    request,

    session,

    redirect
)

import markdown

from backend.chatbot_pipeline import (

    legal_chatbot
)

app = Flask(__name__)

app.secret_key = "legalchatbot"


@app.route(

    "/",

    methods=["GET", "POST"]
)

def home():

    # Create chat history only once
    if "chat_history" not in session:

        session["chat_history"] = []

    # When user sends message
    if request.method == "POST":

        query = request.form["query"]

        response = legal_chatbot(query)

        response = markdown.markdown(response)

        chat_history = session["chat_history"]

        chat_history.append({

            "user": query,

            "bot": response
        })

        session["chat_history"] = chat_history

    return render_template(

        "index.html",

        chat_history=session["chat_history"]
    )


# CLEAR CHAT ROUTE
@app.route("/clear", methods=["GET"])

def clear_chat():

    session["chat_history"] = []

    return redirect("/")


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True
    )