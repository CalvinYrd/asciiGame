import asyncio
import msvcrt

key = ""

async def key_capture():
    global key

    # while True:
    # await asyncio.sleep(0.1) # on attend 100ms entre chaque vérification
    if msvcrt.kbhit(): # si une touche a été pressée
        key = msvcrt.getch().decode() # on récupère la touche

async def main():
    while True: #####
        task1 = asyncio.create_task(key_capture()) # on lance la fonction key_capture en asynchrone
        await task1 # on attend la fin de la tâche
        print(f"Touche pressée: {key}") # on l'affiche

asyncio.run(main()) # on lance la boucle d'événements asyncio
