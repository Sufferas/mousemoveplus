import tkinter as tk
from datetime import datetime
from pynput.keyboard import Listener

class KeyCounter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Key Counter")
        self.geometry("400x200")

        self.start_time = datetime.now()
        self.keypress_count = 0

        self.label = tk.Label(self, text="Tastenanschlag-Zähler läuft...")
        self.label.pack(pady=20)

        self.count_label = tk.Label(self, text="Tastenanschläge: 0\nTastenanschläge/Minute: 0\nTastenanschläge/Stunde: 0")
        self.count_label.pack(pady=20)

        self.update_rate = 5000  # Aktualisiert alle 5 Sekunden
        self.after(self.update_rate, self.update_stats)

        self.listener = Listener(on_press=self.on_keypress)
        self.listener.start()

    def on_keypress(self, key):
        self.keypress_count += 1

    def update_stats(self):
        elapsed_time = datetime.now() - self.start_time
        elapsed_minutes = elapsed_time.total_seconds() / 60
        elapsed_hours = elapsed_time.total_seconds() / 3600

        keys_per_minute = self.keypress_count / elapsed_minutes if elapsed_minutes else 0
        keys_per_hour = self.keypress_count / elapsed_hours if elapsed_hours else 0

        self.count_label.config(text=f"Tastenanschläge: {self.keypress_count}\nTastenanschläge/Minute: {keys_per_minute:.2f}\nTastenanschläge/Stunde: {keys_per_hour:.2f}")
        self.after(self.update_rate, self.update_stats)

if __name__ == "__main__":
    app = KeyCounter()
    app.mainloop()
