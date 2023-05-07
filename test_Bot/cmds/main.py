import discord
from discord.ext import commands
from core.classes import Cog_Extension



class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
    #ctx = context = 上下文 
    #A: 123 (上文) (使用者,id,所在伺服器,所在頻道(所以不用多設定回訊息位置)
    #B: 321 (下文)
        await self.ctx.send(f'{round(self.bot.latency*1000)} (ms)')
        #bot.latency = bot 延遲     round = 4捨5入

def setup(bot):
#傳入bot.py的資料->main.py bot就會被找到
    bot.add_cog(Main(bot))
    #bot會直接傳入class Main