import discord
import random
import requests
from bs4 import BeautifulSoup
import os

hltvstat = "https://www.hltv.org/stats"
hltvlife = "https://www.hltv.org/matches"
hltvplayers = "https://www.hltv.org/stats/players?startDate=2019-05-18&endDate=2020-05-18&rankingFilter=Top20"
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
                full_page = requests.get(hltvlife, user)
                soup = BeautifulSoup(full_page.content, "html.parser")
                info = soup.findAll("span", {"class":"team-name"})
                fight1 = info[0].text + " vs " + info[1].text
                fight2 = info[2].text + " vs " + info[3].text
                await message.channel.send("Матчи в эфире:" + "\n" + fight1 + "\n" + fight2 + "\n" + hltvlife)
            elif message.content.split(" ")[1] == "players" and len(message.content.split(" ")) == 2:
                full_page = requests.get(hltvstat, user)
                soup = BeautifulSoup(full_page.content, "html.parser")
                playerinfo = soup.findAll("a", {"class":"name"})
                kdinfo = soup.findAll("span", {"class":"bold"})
                playertext = "Топ команд:\n"
                for i in range(0, len(playerinfo)):
                    if i == 7:
                        break
                    playertext += playerinfo[i].text + " - " + kdinfo[i * 2].text + "\n"
                await message.channel.send(playertext + hltvstat)
            elif message.content.split(" ")[1] == "teams" and len(message.content.split(" ")) == 2:
                full_page = requests.get(hltvstat, user)
                soup = BeautifulSoup(full_page.content, "html.parser")
                playerinfo = soup.findAll("a", {"class":"name"})
                kdinfo = soup.findAll("span", {"class":"bold"})
                teamtext = "Топ игроков:\n"
                for i in range(8, len(playerinfo)):
                    if i == 7:
                        break
                    teamtext += playerinfo[i].text + " - " + kdinfo[i * 2].text + "\n"
                await message.channel.send(teamtext + hltvstat)
            elif message.content.split(" ")[1] == "phones" and len(message.content.split(" ")) == 2:
                await message.channel.send(os.environ.get("numbers"))
            else:
                await message.channel.send("Я твоя не понимать!")
client = MyClient()

token = os.environ.get("token_side")
client.run(str(token))
