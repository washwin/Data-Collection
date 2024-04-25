import tkinter as tk
from tkinter import filedialog
import subprocess

class ScriptRunnerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Script Runner")
        self.master.geometry("400x200")  # Setting window size

        # Dropdown menu
        self.script_options = [
            "Sangai Express",
            "Imphal Times",
            "Frontier Manipur",
            "Hueiyenlanpao",
            "Paochelsalaitaret",
            "Twitter",
            "YouTube",
        ]
        self.selected_option = tk.StringVar(master)
        self.selected_option.set(self.script_options[0])  # Set default option

        self.script_dropdown = tk.OptionMenu(self.master, self.selected_option, *self.script_options)
        self.script_dropdown.pack(pady=10)

        # Button to run the selected script
        self.run_button = tk.Button(self.master, text="Run Script", command=self.run_script)
        self.run_button.pack(pady=5)

    def run_script(self):
        selected_script = self.selected_option.get()
        if selected_script:
            script_mapping = {
                "Sangai Express": "Epapers/sangai_express.py",
                "Imphal Times": "Epapers/imphal_times.py",
                "Frontier Manipur": "Epapers/frontier_manipur.py",
                "Hueiyenlanpao": "Epapers/hueiyenlanpao.py",
                "Paochelsalaitaret": "Epapers/paochelsalaitaret.py",
                "Twitter": "Twitter-scraper/manipur_violence_tweets.py",
                "YouTube": "Youtube-scraper/manipur_violence_yt.py"
            }
            script_path = script_mapping.get(selected_script)
            if script_path:
                subprocess.Popen(["python", script_path])

def main():
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
