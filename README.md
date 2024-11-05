# AI Vacuum Cleaner Simulation



https://github.com/user-attachments/assets/8644c473-aadd-42cc-a8af-5b61cd4ad8be





This project simulates a basic vacuum cleaner using Python's `tkinter` library for a graphical user interface (GUI) and `random` for movement functionality. The simulation represents a grid-based environment where the vacuum cleaner moves to clean predefined dirt spots. It is an interactive application that allows the user to set the environment size, define dirt locations, and specify the vacuum cleaner's starting position.

## Usage Instructions

1. Clone the repository and run the script using Python.
2. Follow the prompts to:
   - Enter the environment size (e.g., `3x3` for a grid with 3 columns and 3 rows).
   - Define each row's dirt status (e.g., `1 1 0`).
   - Specify the vacuum cleaner's starting location (e.g., `0 0` for the top-left corner).
3. Click "Clean" in the GUI to start the simulation.


## Features

- **Interactive GUI**: Uses `tkinter` to create a visually intuitive grid layout of the environment. The user can view the vacuum cleaner's movements and current dirt status in real time.
- **Random Movement Logic**: The vacuum cleaner follows a random movement pattern within the grid, navigating in all valid directions (left, right, up, down) to locate and clean dirt.
- **User Input for Setup**: Prompts the user to define the environment size, dirt locations, and initial position for flexible simulation settings.
- **Real-Time Cleaning Process**: The application displays each step of the cleaning process with a delay, allowing users to follow the vacuum cleaner's progress until the environment is entirely clean.
- **Status Updates**: Provides status messages, such as movement direction and cleaning completion, enhancing user engagement and clarity.

## How It Works

1. **Environment Setup**: Users define the environment size (width and height) and specify dirt locations by entering a grid configuration where `1` represents dirt and `0` represents a clean space.
2. **Start Position**: Users set the initial position of the vacuum cleaner on the grid.
3. **Cleaning Process**: Once the simulation starts, the vacuum cleaner moves to clean each dirt spot:
   - The program randomly chooses a valid direction to move within the grid.
   - If dirt is present at the current location, the vacuum cleaner cleans it.
   - A `tkinter` GUI displays each move and dirt removal, providing a visual of the cleaning process.
4. **Completion Notification**: When all dirt spots are cleaned, a message confirms that the environment is entirely clean.

## Code Structure

- **VacuumCleaner Class**: The main class responsible for setting up and running the simulation.
  - `__init__`: Initialises the environment grid, starting location, and dirt locations.
  - `clean`: Main logic loop for moving the vacuum cleaner and cleaning the grid.
  - `print_environment`: Updates the grid's visual state in the GUI to reflect the vacuum cleaner's position and dirt status.
  - `create_gui`: Sets up the GUI components, including the grid, status messages, and "Clean" button.




