import requests
import math
api = 'INSERT_KEY_HERE'


def round_decimals_down(number:float, decimals:int=0):
    """
    Returns a value rounded down to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


def formatPercentage(x):
    return "{:.0%}".format(x)


def uuid(ign):
    data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
    return data['id']


def calculateLevel(exp):
    level_requirement_first5 = [0, 1000, 3000, 6000, 9500]
    total_exp_required_first5 = 9500
    experiences_per_lvl = 5000
    if exp > total_exp_required_first5:
        lvl = round_decimals_down((exp - total_exp_required_first5) / experiences_per_lvl)
        lvl += 5
        return lvl
    for i in range(len(level_requirement_first5)):
        if exp < level_requirement_first5[i]:
            return i 
        if exp == level_requirement_first5[i]:
            i += 1
            return i


def stats(ign, key):
    data = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid(ign)}').json()

    winstreak = data['player']['stats']['Bedwars']['winstreak']
    games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
    losses = data['player']['stats']['Bedwars']['losses_bedwars']
    wins = data['player']['stats']['Bedwars']['wins_bedwars']
    beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
    win_rate = round(wins/ (wins + losses), 2)
    

    experience = data['player']['stats']['Bedwars']['Experience']
    lvl = calculateLevel(experience)

    final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
    final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']

    return f'Level: {lvl}\nWins: {wins}\nLosses: {losses}\nWin Rate: {formatPercentage(win_rate)}\nGames Played: {games_played}\n\n' \
           f'Final Kills: {final_kills}\nFinal Deaths: {final_deaths}\n' \
           f'Overall FKDR: {round(final_kills/final_deaths, 2)}\n' \
           f'Win Streak: {winstreak}\nBeds Broken: {beds_broken}'


print(stats('thatbananaking', api))

