import random
from HLTV import *

hltvteams = "https://www.hltv.org/stats/teams"
hltvlife = "https://www.hltv.org/matches"
hltvplayers = "https://www.hltv.org/stats/players?startDate=2019-05-18&endDate=2020-05-18&rankingFilter=Top20"
user = {"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
maps = ["Mirage", "Overpass", "Inferno", "Dust II"]

def helped_message():
    return """
    help      - информация
    random... - случайное значение
    matches   - матчи
    teams     - команды
    players   - игроки
    """

def random_choice(choiseList : list):
    return "Случайный выбор : " + random.choice(choiseList)

def best_match():
    result = "Матчи : \n"
    for match in get_live_matches():
        result += match['teams'][0] + " -vs- " + match['teams'][0] + "\n"
    result += hltvlife
    return result

def best_teams():
    best_10_teams = get_top_teams()[:10]
    result = "Лучшие команды:\n"
    for team_id in range(len(best_10_teams)):
        result += str(team_id + 1) + ". " + best_10_teams[team_id] + "\n"
    result += hltvteams
    return result

def best_players():
    top_10_players = get_best_players()[:10]
    result = "Лучшие игроки:\n"
    for player_data_id in range(len(top_10_players)):
        result += str(player_data_id + 1) + ". " + top_10_players[player_data_id]['player'] + " - " + top_10_players[player_data_id]['team'] + " - " + top_10_players[player_data_id]['rating'] + "\n"
    result += hltvplayers
    return result
