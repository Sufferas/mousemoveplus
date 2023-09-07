import tkinter as tk
from tkinter import Text
import random
import pyautogui
import threading
import time


def ensure_gui_on_top():
    if root.state() == 'iconic':
        root.state('normal')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.focus_force()



def click_within_gui():
    x, y = pyautogui.position()
    if (root.winfo_x() <= x <= root.winfo_x() + root.winfo_width() and
            root.winfo_y() <= y <= root.winfo_y() + root.winfo_height()):
        pyautogui.click()


def random_actions():
    buffer = 50  # Randbreite
    while True:
        # Sicherstellen, dass das GUI immer im Vordergrund ist
        ensure_gui_on_top()
        # Warte 5 Sekunden
        time.sleep(1)

        # Mache 5 Sekunden lang random Maus- und Tasteneingaben
        end_time = time.time() + 5
        while time.time() < end_time:
            # Bewege die Maus an eine zufällige Position innerhalb des GUI-Fensters
            x = random.randint(root.winfo_x() + buffer, root.winfo_x() + root.winfo_width() - buffer)
            y = random.randint(root.winfo_y() + buffer, root.winfo_y() + root.winfo_height() - buffer)
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(0.2)

            # Klickt zufällig
            if random.choice([True, False]):
                click_within_gui()

            # Zufällige Tasteneingabe
            keys = 'abcdefghijklmnopqrstuvwxyz .!?WERTZUIOPASDFGHJKLYXCVBNM123456789'
            for _ in range(30):
                pyautogui.press(random.choice(keys))

            # Pause, um nicht zu schnell zu sein
            time.sleep(0.1)


def main():
    global root
    root = tk.Tk()
    root.title("Random Eingaben GUI")

    # Größe des Fensters auf 3/4 des Bildschirms setzen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.75)
    height = int(screen_height * 0.75)

    root.geometry(f"{width}x{height}")

    # Textfeld, das das gesamte Fenster ausfüllt
    text = Text(root)
    text.pack(expand=1, fill="both")

    # Startet den Thread, der zufällige Eingaben macht
    threading.Thread(target=random_actions, daemon=True).start()

    root.mainloop()


if __name__ == '__main__':
    main()
