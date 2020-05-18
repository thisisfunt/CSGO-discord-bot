import discord
import random
import requests
from bs4 import BeautifulSoup
import os

hltv = "https://www.hltv.org/matches"
user = {"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
maps = ["Mirage", "Overpass", "Inferno", "Dust II"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.split(" ")[0] == "bot":
            if message.content.split(" ")[1] == "map" and len(message.content.split(" ")) == 2:
                map = maps[random.randint(0, len(maps) - 1)]
                await message.channel.send(map)
            elif message.content.split(" ")[1] == "life" and len(message.content.split(" ")) == 2:
                full_page = requests.get(hltv, user)
                soup = BeautifulSoup(full_page.content, "html.parser")
                info = soup.findAll("span", {"class":"team-name"})
                fight1 = info[0].text + " vs " + info[1].text
                fight2 = info[2].text + " vs " + info[3].text
                await message.channel.send("Матчи в эфире:" + "\n" + fight1 + "\n" + fight2 + "\n" + hltv)

            else:
                await message.channel.send("Я твоя не понимать!")
client = MyClient()

token = os.environ.get("token_side")
client.run(str(token))