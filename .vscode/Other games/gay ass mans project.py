import tkinter as tk

score = 0
multiplier = 1
multiplier_costs = [100, 200, 500, 1000, 2500, 5000, 50000,100000,1000000,100000000000,1,1,1,1,1,1,1,1,1,1,1,1]

# Function to handle the click event
def click_button():
    global score
    score += 1 * multiplier
    update_score_label()

# Function to handle the buy multiplier event
def buy_multiplier(index):
    global score, multiplier
    cost = multiplier_costs[index]
    
    if score >= cost:
        score -= cost
        multiplier *= 2
        update_score_label()
        update_multiplier_label()

# Function to update the score label
def update_score_label():
    score_label.config(text="Score: " + str(score))

# Function to update the multiplier label
def update_multiplier_label():
    multiplier_label.config(text="Multiplier: x" + str(multiplier))

# Create the main window
window = tk.Tk()
window.title("Point Game")

# Create the score label
score_label = tk.Label(window, text="Score: " + str(score))
score_label.pack()

# Create the click button
click_button = tk.Button(window, text="Click", command=click_button)
click_button.pack()

# Create the multiplier label
multiplier_label = tk.Label(window, text="Multiplier: x" + str(multiplier))
multiplier_label.pack()

# Create the multiplier buttons
multiplier_frame = tk.Frame(window)
multiplier_frame.pack()

multiplier_labels = []
multiplier_buttons = []

for i, cost in enumerate(multiplier_costs):
    multiplier_labels.append(tk.Label(multiplier_frame, text="x" + str(2 ** (i+1)) + " - Cost: " + str(cost)))
    multiplier_labels[i].grid(row=i, column=0, padx=5, pady=5)
    
    multiplier_buttons.append(tk.Button(multiplier_frame, text="Buy", command=lambda index=i: buy_multiplier(index)))
    multiplier_buttons[i].grid(row=i, column=1, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()