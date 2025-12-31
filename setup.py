import time
import datetime
import pygame

AUDIO_FILE = "XENOGENESIS.mp3"
TARGET_TIME = datetime.time(23, 59, 3)

def seconds_until_target(target_time):
    now = datetime.datetime.now()
    target = datetime.datetime.combine(now.date(), target_time)

    if now >= target:
        target += datetime.timedelta(days=1)

    return (target - now).total_seconds()

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)

wait_sec = seconds_until_target(TARGET_TIME)

print(f"Waiting {wait_sec:.3f} seconds until DROP...")
time.sleep(wait_sec)

pygame.mixer.music.play()

print("YepThat's")

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
