import time
import os

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")
    os.system('ffplay -nodisp -autoexit "Akatsuki.mp3"')

try:
    mins_input = input("Enter minutes (optional, press Enter to skip): ")
    mins = int(mins_input) if mins_input.strip() else 0

    secs = int(input("Enter seconds: "))
    countdown(mins, secs)
except ValueError:
    print("Please enter valid numbers.")
