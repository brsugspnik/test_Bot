import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')
#建做了一個bot 在變數bot中
#在()中 discord呼叫bot時,會用的指令,如:  [send 123

@bot.event
#bot的事件
async def on_ready():
#async def funcname(parameter_list): (async是一個協程名) 
    print(">> Bot is online <<")

bot.run('MTA5MDQ3NzYzMzA1MTA0MTg2Mg.GyC6LF.8LWaEfQqNAMNfBT0QrCmbefkyKHfrjORAIGLE8')
#token必為字串

