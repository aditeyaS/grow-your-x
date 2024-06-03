import random

'''
selects and returns a random topic from the topics array
'''
def generate_topic() -> str:
    topics = [
        "Technology",
        "Programming/Coding",
        "Anime",
        "Nature",
        "Travel"
    ]
    return random.choice(topics)