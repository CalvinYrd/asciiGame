import pynput, asyncio, time, os, colorama, sys, random

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

def getGame():
	global world, player

	w = world
	w = w.split("\n")

	try:
		w[player["y"]] = list(w[player["y"]])

		if (w[player["y"]][player["x"]] == "x"):
			raise ValueError

		w[player["y"]][player["x"]] = "p"
		w[player["y"]] = "".join(w[player["y"]])

	except IndexError:
		return "player_off_world"
	except ValueError:
		return "player_in_wall"

	w = "\n".join(w)

	w = w.replace("x", colorama.Back.BLUE+" "+colorama.Back.RESET)
	w = w.replace(",", colorama.Back.WHITE+" "+colorama.Back.RESET)
	w = w.replace("p", colorama.Back.WHITE+colorama.Fore.BLACK+"p"+colorama.Back.RESET+colorama.Fore.RESET)
	return w

def playerIsInvalid():
	return getGame().startswith("player_")

def movePlayer(direction):
	global player

	if (direction in ("t","r","b","l")):
		playerSave = player.copy()
		player["direction"] = direction

		if (direction == "t"): player["y"] -= 1
		elif (direction == "b"): player["y"] += 1
		elif (direction == "r"): player["x"] += 1
		elif (direction == "l"): player["x"] -= 1

		if (playerIsInvalid()): player = playerSave

FPS = 15
player = {
	"x": 47,
	"y": 3,
	"lives": 3,
	"score": 0,
	"direction": None
}
world = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxx,,xxxxxxxxxxx,,xxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxx,,xxxxxxxxxxx,,xxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,xxxxxxxxxxxxxxxxxxx,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,xxxxxxxxxxxxxxxxxxx,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,xxxxxxxxxxxxxxxxxxx,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,xxxxxxxxxxxxxxxxxxx,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx,,xxxx,,xxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxx,,xxxx,,xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxx,,xxxxxxxxxxx,,xxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxx,,xxxxxxxxxxx,,xxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,xxxxxxxxxxxx,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,,,,,,,,,,,,,,,,xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
clear()

if (playerIsInvalid()):
	print("Les coordonnées de départ sont incorrectes ("+getGame()+")")
else:
	while True:
		clear()
		print(getGame())
		movePlayer(random.choice(("t","r","b","l")))
		time.sleep(1 / FPS)

