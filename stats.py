import requests
api = 'API_KEY_HERE'


def formatPercentage(x):
    return "{:.0%}".format(x)


def uuid(ign):
    data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
    return data['id']


def stats(ign, key):
    data = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid(ign)}').json()

    winstreak = data['player']['stats']['Bedwars']['winstreak']
    games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
    losses = data['player']['stats']['Bedwars']['losses_bedwars']
    wins = data['player']['stats']['Bedwars']['wins_bedwars']
    beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
    win_rate = round(wins/ (wins + losses), 2)
    
    "#Like Catacombs levels, it's inaccurate"
    experience = data['player']['stats']['Bedwars']['Experience']
    total_xp_per_level = 5000
    current_level = experience / total_xp_per_level

    final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
    final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']

    return f'Level: {round(current_level)}\nWins: {wins}\nLosses: {losses}\nWin Rate: {formatPercentage(win_rate)}\nGames Played: {games_played}\n\n' \
           f'Final Kills: {final_kills}\nFinal Deaths: {final_deaths}\n' \
           f'Overall FKDR: {round(final_kills/final_deaths)}\n' \
           f'Win Streak: {winstreak}\nBeds Broken: {beds_broken}'


print(stats('thatbananaking', api))
