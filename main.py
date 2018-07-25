import discord
import random

from subprocess import PIPE, run
from time import sleep


def r(command):
    return run(command, shell=True, stdout=PIPE, stderr=PIPE).stdout.decode()


with open("TOKEN") as token:
    TOKEN = token.readline()

activator = "!"

health_range = 100
attack_range = 100
defense_range = 100
types = ["fire", "water", "grass", "presidential", "memelord", "peasant", "deity"]

client = discord.Client()


@client.event
async def on_message(message):
    content = message.content.lower()  # This makes the bot ignore case
    if message.author == client.user:
        return
    if "yler" in message.author.name: #  This makes the bot ignore Tyler. or anyone with yler in their name
        msg = "I'm not gonna talk to you"  # Freakin tyler
        client.send_message(message.channel, msg)
        return

    if content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message) # I have no idea what the heck is up with those curly brackets
        await client.send_message(message.channel, msg)  # This bit is just part of the tutorial I followed
                                                         # But it literally didn't explain anything
    if content.startswith(activator + "fortune"):
        print(message.author.id)

        msg = r("fortune")  # The r function is just a wrapper to the run function in subprocess
                                # Basically it runs a command line program and spits back the result
        await client.send_message(message.channel, msg)
    # the rest is sort of self explanatory
    if "bong" in content:
        msg = "Drugs are bad mmmmkay"
        await client.send_message(message.channel, msg)
    if "despacito" in content:
        msg = "let's not despacITo"
        await client.send_message(message.channel, msg)

    if message.content.startswith(activator + "Skeet"):
        msg = "i am a robot I have not emotions"
        await client.send_message(message.channel, msg)

    if message.content.startswith(activator + "givemethedrugs"):
        msg = "no"
        await client.send_message(message.channel, msg)

    if content.startswith("banner"): #This bit of code is proned to bugs
        print(message.content)
        banner = message.content[6:]
        if len(banner) < 2: # This is onlt needed because banner will hang if you don't give it anything
            msg = "the message is too short"
        elif len(banner) > 140: # This is because discord hates long messages
            msg = "Shut up"
        else:
            try:
                msg = "```\n" + r("figlet -w 55 " + banner) + "\n```" # The ``` is what lets discord display it right
            except:
                msg = "ok I give up" # This is just in case something, anything breaks (bad design fight me)
        print(msg)
        await  client.send_message(message.channel, msg)

    if "identity" in message.content:
        msg = r("rig")
        await client.send_message(message.channel, msg)

    if message.content.startswith("!home"):
        msg = "https://github.com/awesomehaircut/Colleseum"
        await client.send_message(message.channel, msg)

    if "shush" in content:
        msg = "I'll be quiet for for a little bit"
        await client.send_message(message.channel, msg)
        sleep(360)
        await client.send_message(message, "I'm not grouned anymore hehe")

    if "colleseum" in content:
        msg = "I love when people talk about me"
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print("ready")


client.run(TOKEN)
