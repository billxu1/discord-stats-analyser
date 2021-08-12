import discord
from sql_admin import update_authors, update_words, create_connection, select_stats, select_words
client = discord.Client()

connection = create_connection("pythonsqlite.db")


COUNTER = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith("!"):
        update_authors(connection, message.author.display_name)
        if len(message.content) < 500:
            tmpList = message.content.split()
            for word in tmpList:
                if len(word) < 50:
                    update_words(connection, word)

    if message.content.startswith('!help'):
        await message.channel.send('Type !stats for most active users, !words for list of most used words')

    # For special messages perhaps I should remove await. E.g. !stats should not count as "usage"
    if message.content.startswith('!stats'):
        payload = sorted(select_stats(connection), key=lambda tup:(-tup[1], tup[0]))
        if len(payload) == 0:
            await message.channel.send("There are no current records.")
        else:
            outputString = "\n"
            for idx, (username, messagesSent) in enumerate(payload):
                outputString += f"{idx + 1}. {username} has sent {messagesSent} messages.\n"
            await message.channel.send(outputString)
        
    if message.content.startswith('!words'):
        payload = sorted(select_words(connection), key=lambda tup:(-tup[1], tup[0]))
        if len(payload) == 0:
            await message.channel.send("There are no current records.")
        else:
            outputString = "\n"
            for idx, (username, messagesSent) in enumerate(payload):
                outputString += f"{idx + 1}. {username} has been sent {messagesSent} times.\n"
            await message.channel.send(outputString)
    
    if message.content.count("gei") > 0:
        global COUNTER
        COUNTER += message.content.count("gei")
        await message.channel.send(f"gei has been said {COUNTER} times")
    
    # Keeps track of number of messages sent

    # Keep track of now
    # print(message.author.display_name)
    # print(message.content)

# 
client.run('<copy paste token here>')