#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
import os

os.system('cls')

def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musicOnLoop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterSeconds = 40*60
    exerciseSeconds = 60*60
    eyeSeconds = 45*60

    while True:
        if time() - init_water > waterSeconds:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musicOnLoop('mp3/water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyeSeconds:
            print("Eye exercise time. Enter 'eyes relaxed' to stop the alarm.")
            musicOnLoop('mp3/eyes.mp3', 'eyes relaxed')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exerciseSeconds:
            print("Physical Activity Time. Enter 'exercise done' to stop the alarm.")
            musicOnLoop('mp3/physical.mp3', 'exercise done')
            init_exercise = time()
            log_now("Physical Activity done at")


