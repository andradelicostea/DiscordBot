import discord
import resp

async def send_message(message, user_message, is_private): #defines an asynchronous function that sends a message to either the channel or the user depending on the is_private argument.
    try:
        response = resp.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = '-add token here-'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
        #intents - defines the bot's intents, which determine what events the bot will listen for.

    @client.event #- a decorator that marks a function as an event listener for the client
    async def on_ready(): # - an event listener that is triggered when the bot connects to Discord.
        print(f'{client.user} is now online!')

    @client.event
    async def on_message(message): # - an event listener that is triggered whenever a message is sent in a channel that the bot can access.
        if message.author == client.user: # - checks if the message was sent by the bot itself
            return

        username = str(message.author) # - gets the username of the user who sent the message
        user_message = str(message.content) # - gets the content of the message.
        channel = str(message.channel) #- gets the channel that the message was sent in.

        print(f'{username} : "{user_message}" ({channel})')

        if user_message[0] == '?': #- checks if the message starts with a question mark
            user_message = user_message[1:] #- removes the question mark from the start of the message.
            await send_message(message, user_message, is_private=True) #- sends a response to the user privately if the message starts with a question mark, or sends a response to the channel otherwise.
        else:
            await send_message(message, user_message, is_private=False) # - sends a response to the channel.

    client.run(TOKEN) # - runs the Discord bot by connecting to Discord using the specified token.




