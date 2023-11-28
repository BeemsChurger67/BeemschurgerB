import tkinter as tk
from tkinter import ttk
import time

multiplier = 1
class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")

        self.clicks = 0
        self.upgrades = {
            'Upgrade 1': {'cost': 10, 'multiplier': 2},
            'Upgrade 2': {'cost': 50, 'multiplier': 3},
            'Upgrade 3': {'cost': 100, 'multiplier': 4},
            'Upgrade 4': {'cost': 200, 'multiplier': 5},
            'Upgrade 5': {'cost': 500, 'multiplier': 10},
        }

        self.click_label = ttk.Label(root, text=f'Clicks: {self.clicks}')
        self.click_label.grid(row=0, column=0, pady=10)

        self.upgrades_frame = ttk.Frame(root)
        self.upgrades_frame.grid(row=1, column=0, pady=10)

        ttk.Label(self.upgrades_frame, text='Upgrades:').grid(row=0, column=0, columnspan=2)

        self.upgrade_buttons = []
        for i, (upgrade, details) in enumerate(self.upgrades.items()):
            ttk.Label(self.upgrades_frame, text=f'{upgrade}: Cost - {details["cost"]}, Multiplier - {details["multiplier"]}').grid(row=i + 1, column=0, columnspan=2)
            button = ttk.Button(self.upgrades_frame, text=f'Buy {upgrade}', command=lambda u=upgrade: self.purchase_upgrade(u))
            button.grid(row=i + 1, column=2)
            self.upgrade_buttons.append(button)

        self.root.after(1000, self.update)

    def click(self):
        self.clicks += 1 * multiplier^2
        print(multiplier^2)

    def purchase_upgrade(self, upgrade):
        global multiplier
        if upgrade in self.upgrades:
            cost = self.upgrades[upgrade]['cost']
            if self.clicks >= cost:
                self.clicks -= cost
                self.upgrades[upgrade]['cost'] *= 2
                self.upgrades[upgrade]['multiplier'] += 1
                print(f'Purchased {upgrade}!')
                multiplier += 1
            else:
                print(f'Not enough clicks to purchase {upgrade}.')

    def update(self):
        self.click()
        self.click_label.config(text=f'Clicks: {self.clicks}')

        for i, (upgrade, details) in enumerate(self.upgrades.items()):
            self.upgrade_buttons[i].config(text=f'Buy {upgrade} ({details["cost"]} clicks)')

        self.root.after(1000, self.update)


if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()