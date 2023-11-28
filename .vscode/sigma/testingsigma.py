import random

# Initialize variables
total_r = 0
total_g = 0
total_b = 0

# Create a forever loop
while True:
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Add the generated values to the totals
    total_r += r
    total_g += g
    total_b += b

    # Ensure the total values don't exceed 255 (max RGB value)
    total_r = min(total_r, 255)
    total_g = min(total_g, 255)
    total_b = min(total_b, 255)

    # Print the current totals
    print(f"Total RGB: ({total_r}, {total_g}, {total_b})")