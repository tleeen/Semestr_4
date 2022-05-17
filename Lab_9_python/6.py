from time import sleep
from discord.ext import commands
from kemsu_lab_bot_discord import D_TOKEN


class KemSU_Bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='timer')
    async def timer(self, ctx, s):
        sleep(int(s))
        await ctx.send("время X наступило!")


bot = commands.Bot(command_prefix='!#')
bot.add_cog(KemSU_Bot(bot))
bot.run(D_TOKEN)
