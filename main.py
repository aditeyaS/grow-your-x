from src import bot
from dotenv import load_dotenv

# load environment variables
load_dotenv()

if __name__ == '__main__':
    bot.run(debug=True, port=5000)