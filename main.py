import msvcrt, asyncio, time, os, colorama, random

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

def getGame():
	global world, player

	w = world.copy()

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
	w = w.replace(".", colorama.Back.YELLOW+" "+colorama.Back.RESET)
	w = w.replace("p", colorama.Back.GREEN+colorama.Fore.BLACK+"p"+colorama.Back.RESET+colorama.Fore.RESET)

	details = "SCORE : "+str(player["score"])+" VIES : "+str(player["lives"])
	# details = colorama.Back.BLUE+details+colorama.Back.RESET
	w = w.replace("$DETAILS$", details)
	return w

def playerIsInvalid():
	return (getGame() in ("player_off_world","player_in_wall"))

def movePlayer(direction):
	global player, world

	if (direction in ("z","d","s","q")):
		playerSave = player.copy()
		player["direction"] = direction

		if (direction == "z"): player["y"] -= 1
		elif (direction == "s"): player["y"] += 1
		elif (direction == "d"): player["x"] += 2
		elif (direction == "q"): player["x"] -= 2
		line = list(world[player["y"]])

		if (line[player["x"]] == ","):
			player["score"] += random.randint(5, 15)

		if (playerIsInvalid()):
			player = playerSave
		else:
			line[player["x"]] = "."
			if (line[player["x"]-1] == ","): line[player["x"]-1] = "."
			if (line[player["x"]+1] == ","): line[player["x"]+1] = "."
			line = "".join(line)
			world[player["y"]] = line

async def setDirection():
	global player

	if msvcrt.kbhit():
		direction = msvcrt.getch()

		if (direction in (b"z",b"d",b"s",b"q")):
			player["direction"] = direction.decode()

def gameIsUndone():
	global world
	w = world.copy()
	w = "\n".join(w)
	res = ("," in w)
	return res

FPS = 30
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
$DETAILS$
"""
world = world.split("\n")
clear()

async def main():
	if (playerIsInvalid()):
		print("Les coordonnées de départ sont incorrectes ("+getGame()+")")
	else:
		while gameIsUndone():
			await asyncio.create_task(setDirection())
			clear()
			print(getGame())
			movePlayer(player["direction"])
			time.sleep(1 / FPS)

		clear()
		print(getGame())

asyncio.run(main())
