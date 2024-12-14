# Next Fit Memory Allocation

This project implements the *Next Fit Memory Allocation Algorithm* using Python with a graphical user interface (GUI) built using Tkinter. The Next Fit algorithm efficiently manages memory by allocating processes to the next available block and keeping track of the last allocated block to minimize allocation time.

## Features
- Dynamically allocate and deallocate memory blocks.
- View the current memory state in real time.
- Display detailed memory allocation for each process.
- User-friendly GUI for easy interaction.

## Prerequisites
- *Python 3.x*: Ensure Python 3.x is installed on your system.
- *Tkinter*: Tkinter is included with Python by default. If not, install it using your package manager.

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/Malithiit/NextFitAlgorithumMP
   
2. Run the program by clicking the "Run" button in VS Code.

## Usage
1. Run the Python script to start the application:
   bash
   python next_fit_allocator.py
   
2. Interact with the GUI to:
   - Allocate memory to processes.
   - Deallocate memory from processes.
   - View the current memory state and allocation details.

## Code Structure
- *next_fit_allocator.py*: Contains the implementation of the Next Fit memory allocation algorithm along with the GUI.

## GUI Features
- *Allocate Process*: Allocate memory to a process by entering its name and required size.
- *Deallocate Process*: Free memory by entering the name of the allocated process.
- *Memory State*: View the current memory block status (free/allocated).
- *Final Allocation*: Display the final allocation details for all processes.

## Screenshots
- *Memory State*: Displays real-time memory status.
- *Allocation Details*: Shows the process allocations and their sizes.

## Author
Malithi Godakumbura