import discord
from kemsu_lab_bot_discord import D_TOKEN


class KemSU_Bot(discord.Client):
    async def on_ready(self):
        a = client.get_channel(975958490805837827)
        await a.send("Я подключился и готов показать котика или пёсика!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "собака" in message.content.lower():
            with open('dog.jpg', 'rb') as file:
                dog = discord.File(file)
                await message.channel.send(file=dog)
        elif "кот" in message.content.lower():
            with open('cat.jpg', 'rb') as file:
                cat = discord.File(file)
                await message.channel.send(file=cat)


client = KemSU_Bot()
client.run(D_TOKEN)
