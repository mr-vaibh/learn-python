#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from datetime import datetime
from time import time
from pygame import mixer


def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('mylogs.txt', 'a') as file:
        file.write(f'{msg} {datetime.now()}')

if __name__ == "__main__":
    # musicOnLoop('mp3/water.mp3', 'stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterSeconds = 5
    exerciseSeconds = 10
    eyesSeconds = 20

    while True:
        if time() - init_water > waterSeconds:
            print('Water drinking time. Enter `drank` to stop the alarm: ')
            musicOnLoop('mp3/water.mp3', 'drank')
            init_water = time()
            log_now('Drank water -')