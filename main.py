import discord
import random

with open("TOKEN") as token:
    TOKEN = token.readline()

health_range = 100
attack_range = 100
defense_range = 100
types = ["fire", "water", "grass", "presidential", "memelord", "peasant", "deity"]


class Player:

    death = bool(False)
    type = str("")
    health = int(0)
    attack = int(0)
    defense = int(0)
    def __init__(self):
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


@client.event
async def on_message(message):
    if message.author == client.user:
        msg = " Why wud U do that?!1"
        return

    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!battle reset"):
        print("doing the thing")
        player_name = "Asssssh" # TODO: figure out the persons id
        player_name = Player()
        print(player_name.stats())
        msg = str("your stats are: " + str(player_name.stats())).format(message)
        await client.send_message(message.channel, msg)
        print(player_name)

    if message.content.startswith("!battle stats"):
        pass

@client.event
async def on_ready():
    print("Logged in as \n %s \n %s \n", client.user.name, client.user.id)
    msg = "Hello I'm ready"

client.run(TOKEN)

