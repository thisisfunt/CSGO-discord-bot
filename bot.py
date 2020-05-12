import discord
import random

maps = ["Mirage", "Overpass", "Inferno", "Dust II"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.split(" ")[0] == "bot":
            if message.content.split(" ")[1] == "map":
                map = maps[random.randint(0, len(maps) - 1)]
                await message.channel.send(map)
            
client = MyClient()
client.run('NzA5NDMxMjQyMjY4OTk5ODEx.Xrqmtg.o_yv3z1WVRVuOOboc8ZP5qxHzZw')
