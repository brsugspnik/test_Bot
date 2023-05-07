import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

class React(Cog_Extension):
    

def setup(bot):
#傳入bot.py的資料->main.py bot就會被找到
    bot.add_cog(React(bot))