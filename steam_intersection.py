import json, requests, argparse

url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'

parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str, metavar = "KEY", nargs=1, help='your steam API key')
parser.add_argument('--steamids', type=str, metavar = "ID", nargs=2, help='steamids to compare')
args = parser.parse_args()

params1 = dict(
	key = args.key,
    steamid = args.steamids[0],
    include_appinfo = 1,
    include_played_free_games = 0,
    format = "json"
)

params2 = dict(
	key = args.key,
	steamid = args.steamids[1],
	include_appinfo = 1,
	include_played_free_games = 0,
	format="json"
)

resp1 = requests.get(url=url, params=params1)
resp2 = requests.get(url=url, params=params2)
data1 = json.loads(resp1.text)
data2 = json.loads(resp2.text)
games1 = [x['name'] for x in data1['response']['games']]
games2 = [x['name'] for x in data2['response']['games']]
common_games = set(games1).intersection(set(games2))
print("Games in common:")
for game_title in common_games:
	print game_title