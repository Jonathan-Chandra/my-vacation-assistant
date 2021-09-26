
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jonathan Chandra"
__copyright__ = "None"
__credits__ = ["Jonathan Chandra"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Jonathan Chandra"
__email__ = "chandra.jonathan@gmail.com"
__status__ = "Prototype"

import os
import time

import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from replit import db
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import models
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

client_string = os.getenv("MONGODB_CONNECTION")
    
mongo_client = MongoClient(client_string)
try:
  # The ping command is cheap and does not require auth.
  mongo_client.admin.command('ping')
  print(mongo_client['vacation-bot'])
except ConnectionFailure:
  print("Error: Database Server not available")

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"
    pass

@client.command()
async def add(ctx, arg1, arg2):
  await ctx.send("Would you like to add {} {}?".format(arg1,arg2)) 
  pass

@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.command()
async def addContact(ctx, arg1, arg2, arg3, arg4):
  contact = models.contact()
  try:
    pass
  except:
    await ctx.send("Unable to add contact information to database. Please try again later.")
  pass


client.run(os.getenv("DISCORD_TOKEN")) #get your bot token and make a file called ".env" then inside the file write TOKEN=put your api key here example in env.txt
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!