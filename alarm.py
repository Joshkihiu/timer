import time
import os
from datetime import datetime

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")
    play_alarm()

def alarm_clock(target_time):
    print(f"Alarm set for {target_time.strftime('%H:%M:%S')}")
    while True:
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        if now >= target_time:
            print("\nAlarm time reached!")
            play_alarm()
            break
        print(f"Current time: {current_time}", end="\r")
        time.sleep(1)

def play_alarm():
    os.system('ffplay -nodisp -autoexit "Alarm.mp3"')

def main():
    print("Select mode:")
    print("1. Countdown Timer")
    print("2. Alarm Clock")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        try:
            mins_input = input("Enter minutes (optional, press Enter to skip): ")
            mins = int(mins_input) if mins_input.strip() else 0
            secs = int(input("Enter seconds: "))
            countdown(mins, secs)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == "2":
        try:
            time_input = input("Set alarm time (HH:MM:SS, 24-hr format): ")
            target_time = datetime.strptime(time_input, "%H:%M:%S")
            now = datetime.now()
            target_time = now.replace(hour=target_time.hour, minute=target_time.minute, second=target_time.second)
            if target_time < now:
                target_time = target_time.replace(day=now.day + 1)  # Schedule for next day if time already passed
            alarm_clock(target_time)
        except ValueError:
            print("Invalid time format. Use HH:MM:SS.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
