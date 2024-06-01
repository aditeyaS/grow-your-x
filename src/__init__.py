from .errors.ApiKeyError import ApiKeyError
from .clients.OpenAI import OpenAI
from .clients.Twitter import Twitter
from .clients.Secret import Secret
from .service.generate_topic import generate_topic
from flask import Flask, request, jsonify

bot = Flask(__name__)

@bot.route("/", methods=["GET"])
def wake_up():
    response_body = {"message": "Yo! What's up?"}
    return jsonify(response_body), 200

@bot.route("/api/tweet", methods=["POST"])
def tweet():
    request_body = request.get_json()
    if "secret" not in request_body:
        response_body = {"message": "Missing secret"}
        return jsonify(response_body), 400
    try:
        secret_client = Secret()
        open_ai_client = OpenAI()
        twitter_client = Twitter()
    except ApiKeyError as e:
        response_body = {"message": f"ApiKeyError: {e}"}
        return jsonify(response_body), 500
    received_secret = request_body["secret"]
    if received_secret != secret_client.get():
        response_body = {"message": "Incorrect secret"}
        return jsonify(response_body), 401
    topic = generate_topic()
    try:
        generated_tweet = open_ai_client.generate_tweet(topic=topic)
        # if length of tweet > 280 -> generate again
        while len(generated_tweet) > 280:
            generated_tweet = open_ai_client.generate_tweet(topic=topic)
    except Exception as e:
        response_body = {"message": "Error in generating tweet", "error": f"{e}"}
        return jsonify(response_body), 500
    try:
        twitter_client.tweet(generated_tweet=generated_tweet)
    except Exception as e:
        response_body = {"message": "Error in posting tweet", "error": f"{e}"}
        return jsonify(response_body), 500
    response_body = {"message": "Tweet success", "tweet": f"{generated_tweet}"}
    return jsonify(response_body), 200