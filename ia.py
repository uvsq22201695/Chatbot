import json
from textblob import TextBlob

with open('data.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)


def get_response(userInput: str) -> str:
    """
    Get the best response from the IA
    :param userInput: String to be analyzed
    :return best_match: Best response from the IA
    """

    user_tokens = tokenize(userInput.lower())

    best_match = None
    best_similarity = 0.0

    for key, value in data.items():
        key_tokens = tokenize(key)

        similarity = len(set(user_tokens).intersection(key_tokens)) / float(len(set(user_tokens).union(key_tokens)))

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = value

    return best_match if best_similarity > 0 else "I don't understand..."


def tokenize(text: str) -> list:
    """
    Tokenize text into sentences and words
    :param text: String to be a tokenized
    :return word_tokens: list of words
    """

    return TextBlob(text).words
