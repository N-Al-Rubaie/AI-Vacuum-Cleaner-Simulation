import random  # Importing the random module for random choice functionality
import tkinter as tk  # Importing tkinter for creating GUI elements
import time  # Importing time module to add delays

# Class for creating a vacuum cleaner object which can clean a given grid environment
class VacuumCleaner:
    # Initialiser function to set up the vacuum cleaner's environment and initial state
    def __init__(self, width, height, dirt_locations, start_location):
        # Setting the environment width and height
        self.width = width
        self.height = height
        # Initialising dirt locations grid, where 1 represents dirt and 0 is clean
        self.dirt_locations = dirt_locations
        # Setting the initial position of the vacuum cleaner
        self.current_location = start_location

    # Method to clean the environment when the "Clean" button is clicked
    def clean(self):
        # Loop to keep cleaning until no dirt is found in the environment
        while True:
            # Check if any dirt (1) remains in the environment
            if not any(1 in row for row in self.dirt_locations):
                # Update message to indicate cleaning is complete
                self.message_var.set('All clean!')
                break  # Exit the cleaning loop

            # Display the current state of the environment
            self.print_environment()

            # Get the current coordinates of the vacuum cleaner
            x, y = self.current_location

            # If there is dirt at the current location, clean it (set to 0)
            if self.dirt_locations[y][x] == 1:
                self.dirt_locations[y][x] = 0

            # List of possible movement directions
            options = []
            # Check for possible moves (left, right, up, down) and add to options if valid
            if x > 0:
                # If the vacuum cleaner is not at the leftmost edge, add 'left' move option
                options.append(('left', (x - 1, y)))
            if x < self.width - 1:
                # If the vacuum cleaner is not at the rightmost edge, add 'right' move option
                options.append(('right', (x + 1, y)))
            if y > 0:
                # If the vacuum cleaner is not at the top edge, add 'up' move option
                options.append(('up', (x, y - 1)))
            if y < self.height - 1:
                # If the vacuum cleaner is not at the bottom edge, add 'down' move option
                options.append(('down', (x, y + 1)))

            # Choose a random direction from available options
            direction, new_location = random.choice(options)

            # Update the message to indicate the move direction
            self.message_var.set(f'Moved {direction}')

            # Pause for 4 seconds before the next move
            time.sleep(4)

            # Update the current location to the new location
            self.current_location = new_location

            # Update the display to reflect new state
            self.print_environment()
            # Refresh the root window to show changes
            self.root.update()

        # Final display update and message when cleaning is done
        self.print_environment()
        self.message_var.set('Done!')

    # Method to update the display to show the environment's current state
    def print_environment(self):
        # Loop through each cell in the grid
        for row in range(self.height):
            for col in range(self.width):
                # Check if the current cell is the vacuum cleaner's location
                if (col, row) == self.current_location:
                    # Set vacuum cleaner's cell with label 'V' and light blue background
                    self.labels[row][col].configure(text='V', bg='lightblue')
                else:
                    # Set dirt value and colour for other cells (1 for dirt, 0 for clean)
                    dirt = self.dirt_locations[row][col]
                    self.labels[row][col].configure(text=dirt, bg='white')

    # Method to create the GUI for the vacuum cleaner simulation
    def create_gui(self):
        # Initialise the root window
        self.root = tk.Tk()
        # Set the window title
        self.root.title('Vacuum Cleaner')
        # Initialise an empty list to hold the labels for each grid cell
        self.labels = []

        # Create a grid of labels representing the environment cells
        for row in range(self.height):
            # Initialise a list to hold each row's labels
            label_row = []
            for col in range(self.width):
                # Get the dirt value for each cell
                dirt = self.dirt_locations[row][col]
                # Create a label for the cell with specified font, size, and border
                label = tk.Label(self.root, text=dirt, font=('Arial', 20), width=3, height=2, bd=1, relief='solid')
                # Place the label on the grid
                label.grid(row=row, column=col)
                # Append the label to the current row's list
                label_row.append(label)
            # Append the row to the labels grid
            self.labels.append(label_row)

        # Create a "Clean" button that calls the clean method when clicked
        button = tk.Button(self.root, text='Clean', font=('Arial', 16), command=self.clean)
        # Place the button at the bottom of the grid, spanning all columns
        button.grid(row=self.height, column=0, columnspan=self.width)

        # Initialise a StringVar for displaying messages
        self.message_var = tk.StringVar()
        # Create a label to display messages, linked to message_var
        message_label = tk.Label(self.root, textvariable=self.message_var, font=('Arial', 16), height=2)
        # Place the message label below the "Clean" button, spanning all columns
        message_label.grid(row=self.height + 1, column=0, columnspan=self.width)

        # Start the main GUI loop, waiting for events and user interactions
        self.root.mainloop()

# Loop to get user input for environment size (width and height)
while True:
    try:
        # Prompt user to input the environment size in "WxH" format
        width, height = input('Enter the environment size (e.g. 3x2): ').split('x')
        width = int(width)
        height = int(height)
        break  # Exit loop if input is valid
    except ValueError:
        print('Invalid input. Please enter two integers separated by "x".')

# Loop to get user input for dirt locations for each row in the grid
dirt_locations = []
for row in range(height):
    while True:
        try:
            # Prompt user for dirt locations, using 0 for clean and 1 for dirt
            row_input = input(f'Enter dirt locations for row {row + 1} (use 0 for clean and 1 for dirty): ')
            # Convert input to a list of integers
            row_locations = [int(loc) for loc in row_input.split()]
            # Check if the row length matches width and all values are either 0 or 1
            if len(row_locations) != width or any(loc not in [0, 1] for loc in row_locations):
                print(f'Invalid input. Please enter {width} integers separated by spaces, with 0 for clean and 1 for dirty.')
                continue  # Repeat the prompt if invalid
            # Append the validated row to dirt_locations
            dirt_locations.append(row_locations)
            break  # Exit loop if row input is valid
        except ValueError:
            print(f'Invalid input. Please enter {width} integers separated by spaces, with 0 for clean and 1 for dirty.')

# Loop to get user input for vacuum cleaner's starting location
while True:
    try:
        # Prompt user to enter start location as "x y"
        start_x, start_y = input('Enter the start location of the vacuum (e.g. 0 0): ').split()
        start_x = int(start_x)
        start_y = int(start_y)
        # Ensure start location is within grid boundaries
        if start_x < 0 or start_x >= width or start_y < 0 or start_y >= height:
            print(f'Start location must be within the {width}x{height} environment.')
            continue  # Repeat the prompt if invalid
        break  # Exit loop if input is valid
    except ValueError:
        print('Invalid input. Please enter two integers separated by a space.')

# Create a VacuumCleaner object with user input parameters
start_location = (start_x, start_y)
vc = VacuumCleaner(width, height, dirt_locations, start_location)
# Initialise and display the GUI for the vacuum cleaner simulation
vc.create_gui()
