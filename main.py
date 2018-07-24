import discord
import random

from subprocess import PIPE, run

def r(command):
    return run(command, shell=True, stdout=PIPE, stderr=PIPE).stdout.decode()


with open("TOKEN") as token:
    TOKEN = token.readline()

activator = "!"

health_range = 100
attack_range = 100
defense_range = 100
types = ["fire", "water", "grass", "presidential", "memelord", "peasant", "deity"]


class Player:

    name = ""
    death = bool(False)
    type = str("")
    health = int(0)
    attack = int(0)
    defense = int(0)
    def __init__(self, name):
        self.name = name
        self.type = types[random.randint(0, len(types) - 1)]
        self.health = random.randint(1, health_range)
        self.attack = random.randint(1, attack_range)
        self.defense = random.randint(1, defense_range)

    def reset_stats(self):
        self.__init__()

    def stats(self):
        """just type for now"""
        return ("\n type " + str(self.type)
                +"\n HP = " + str(self.health)
                +"\n Attack " + str(self.attack)
                +"\n defense: " + str(self.defense)
                +"\n ")

    def damage(self, damage):
        if self.health - damage < 1:
            self.death = True
        else:
            self.health = self.health - damage


client = discord.Client()

players = [
]

@client.event
async def on_message(message):
    if message.author == client.user:
        msg = " Why wud U do that?!1"
        return


    if message.content.startswith(activator + "players"):
        return
        if len(players) > 1:
            msg = "There's " + str(len(players)) + " player(s) and they are as followed: \n" +\
                  str([i + "\n" for i in players])
        else:
            msg = "No one's playing yet"

        await  client.send_message(msg.format(message))

    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!battle reset"):
        return
        print("doing the thing")
        player_name = message.author
        if player_name.id in players:
            players.pop(player_name.id)
        players.append(Player(player_name))
        print(player_name.stats())
        msg = str(str(player_name) + " your stats " + str(player_name) + "are: " + str(player_name.stats())).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(activator + "fortune"):
        print(message.author.id)

        if "ˡᶦᵗᵗˡᵉ" in message.author.name:
                msg = "I'm not allowed to talk to you"

        if "Zu" in message.author.name or "awesome" in message.author.name:
            msg = "You're pretty awesome aren't you :-)"
        if message.author.name.startswith("Summer"):
            msg = "ALL HAIL CTHULHU"
        if message.author.name.startswith("Der"):
            msg = "I will never leave again"
        else:
            msg = r("fortune")
        await client.send_message(message.channel, msg)
    if "bong" in message.content:
        msg = "Drugs are bad mmmmkay"
        await client.send_message(message.channel, msg)
    if "Despacito" in message.content or "despacito" in message.content:
        msg = "let's not despacITo"
        await client.send_message(message.channel, msg)

    if message.content.startswith(activator+"Skeet"):
        msg = "i am a robot I have not emotions"
        await client.send_message(message.channel, msg)

    if message.content.startswith(activator+"givemethedrugs"):
        msg = "no"
        await client.send_message(message.channel, msg)

    if message.content.startswith("gibb"):
        banner = message.content.strip("banner")
        msg = r("figlet " + banner).format(message)
        await  client.send_message(message.channel, msg)
    if "identity" in message.content:
        msg = r("rig")
        await client.send_message(message.channel, msg)

    if message.content.startswith("!battle stats"):
        return
        msg = message.author
        print(msg)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!home"):
        msg = ("https://github.com/awesomehaircut/Colleseum")
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print("ready")

client.run(TOKEN)

