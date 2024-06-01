import random

'''
selects and returns a random topic from the topics array
'''
def generate_topic():
    topics = [
        "Technology",
        "Programming/Coding",
        "Anime",
        "Nature",
        "Travel"
    ]
    return random.choice(topics)