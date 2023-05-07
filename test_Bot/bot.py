import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json',mode='r',encoding='utf8') as jfile:
#開一個setting的檔,mode是模式,r=read(讀取),encoding=解碼為utf8(如有中文), 放在jfile
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[', intents = discord.Intents.default() )
#建做了一個bot 在變數bot中
#在()中 discord呼叫bot時,會用的指令,如:  [send 123

@bot.event
#bot的事件
async def on_ready():
#async def funcname(parameter_list): (async是一個協程名) 
    print(">> Bot is online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')
    
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'./cmds.{filename[:-3]}')
#檔cmds中的所有py檔 讀取    filename[:-3] = 把py檔的.py去掉 如main.py -> main 打指令就不用打main.py了 .txt為 [:-4]






#bot.run('token數字')
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
    #token必為字串
