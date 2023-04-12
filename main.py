import pynput, asyncio, time, os, colorama, sys

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
			print("Le joueur ne peut pas être placé dans un mur !")
			sys.exit(0)

		w[player["y"]][player["x"]] = "p"

		w[player["y"]] = "".join(w[player["y"]])

	except IndexError:
		print("coordonnées du joueur incorrect !")
		sys.exit(0)

	w = "\n".join(w)

	w = w.replace("x", colorama.Back.BLUE+" "+colorama.Back.RESET)
	w = w.replace(",", colorama.Back.WHITE+" "+colorama.Back.RESET)
	w = w.replace("p", colorama.Back.WHITE+colorama.Fore.BLACK+"p"+colorama.Back.RESET+colorama.Fore.RESET)
	return w

FPS = 2
player = {
	"x": 47,
	"y": 3,
	"lives": 3,
	"score": 0
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

while True:
	clear()
	print(getGame())
	time.sleep(1 / FPS)

