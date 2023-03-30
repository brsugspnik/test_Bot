import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents=intents)
#建做了一個bot 在變數bot中
#在()中 discord呼叫bot時,會用的指令,如:  [send 123

@bot.event
#bot的事件
async def on_ready():
#async def funcname(parameter_list): (async是一個協程名) 
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
#加入群組的成員 member只能放一個(不能多放)
    #print(f'{member} join!')
    #會在終端機印出成員加入(XXXjoin)字
    channel = bot.get_channel(1090206193785507860)
    await channel.send(f'{member} join!')
    #如discord.py網頁上 指令為this function could be a coroutine = 他是協程 要用await指令

@bot.event
async def on_member_remove(member):
    #print(f'{member} leave!')
    channel = bot.get_channel(1090206193785507860)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
#ctx = context = 上下文 
#A: 123 (上文) (使用者,id,所在伺服器,所在頻道(所以不用多設定回訊息位置)
#B: 321 (下文)
    await ctx.send(f'{bot.latency*1000} (ms)')
    #bot.latency = bot 延遲


@bot.command()
async def mange(ctx):
    pic = discord.Flie(jdata['pic'])
    await ctx.send(f'you say {file = pic} ?)'
//"pic": 'D\\where\\where\\123.jpg' (json)
    
    
bot.run('MTA5MDQ3NzYzMzA1MTA0MTg2Mg.GyC6LF.8LWaEfQqNAMNfBT0QrCmbefkyKHfrjORAIGLE8')
#token必為字串

