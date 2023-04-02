import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll_dice':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`type "roll" for a random number `'

    return 'I didn\'t understand what you wrote. Try typing "!help".'