import discord
import random
import os
import model as model

hltvstat = "https://www.hltv.org/stats"
hltvlife = "https://www.hltv.org/matches"
hltvplayers = "https://www.hltv.org/stats/players?startDate=2019-05-18&endDate=2020-05-18&rankingFilter=Top20"
user = {"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
maps = ["Mirage", "Overpass", "Inferno", "Dust II"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        try:
            if message.author == self.user:
                return
            splited_message = message.content.split(" ")
            if splited_message[0] == "bot":
                if splited_message[1] == "help" and len(splited_message) == 2:
                    await message.channel.send(model.helped_message())
                elif splited_message[1] == "random":
                    await message.channel.send(model.random_choice(splited_message[2:]))
                elif splited_message[1] == "matches" and len(splited_message) == 2:
                    await message.channel.send(model.best_match())
                elif splited_message[1] == "teams" and len(splited_message) == 2:
                    await message.channel.send(model.best_teams())
                elif splited_message[1] == "players" and len(splited_message) == 2:
                    await message.channel.send(model.best_players())
        except:
            message.channel.send("error")
client = MyClient()

token = os.environ.get("token")

client.run(str(token))

client.run(str(token))
