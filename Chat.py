from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
	"Tuesday",
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.sqlite3'
)


chatbot.set_trainer(ListTrainer)

chatbot.train([
    "Hi there!",
    "Hello",
])

chatbot.train([
    "Greetings!",
    "Hello",
])

#chatbot.train([
#    'How are you?',
#    'I am good.',
#    'That is good to hear.',
#    'Thank you',
#    'You are welcome.',
#])

while True:
    try:
     bot_input = chatbot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

