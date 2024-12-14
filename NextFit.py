import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

#Represents a memory block with size, free space, and allocation
class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.free = size
        self.allocated_to = None
#Allocates memory using Next Fit strategy, starting from last index
class NextFitAllocator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.last_allocated_index = -1

    def allocate(self, nameofprocess, size):
        n = len(self.blocks)
        startindex = (self.last_allocated_index + 1) % n
        index = startindex

        while True:
            block = self.blocks[index]

            if block.free >= size:
                block.allocated_to = nameofprocess
                block.free -= size
                self.last_allocated_index = index
                return True

            index = (index + 1) % n
            if index == startindex:
                return False
#Deallocates memory for process, resetting allocated space to free
    def deallocate(self, nameofprocess):
        for block in self.blocks:
            if block.allocated_to == nameofprocess:
                block.free += (block.size - block.free)
                block.allocated_to = None
                return True
        return False
#Displays memory status of blocks, showing allocation and free space
    def DisplayMemoryStatus(self):
        MemoryStatus = []
        for i, block in enumerate(self.blocks):
            status = f"Allocated to {block.allocated_to}" if block.allocated_to else "Free"
            MemoryStatus.append(f"Block {i + 1}: {block.free} KB free ({status}).")
        return MemoryStatus

# Displays allocation details, showing allocated size and corresponding process
    def display_allocation_details(self):
        allocation_details = []
        for i, block in enumerate(self.blocks):
            if block.allocated_to:
                allocated_size = block.size - block.free
                allocation_details.append(f"Process {block.allocated_to}: Allocated {allocated_size} KB in Block {i + 1}.")
        return allocation_details
#GUI for memory management with allocation, deallocation, and status display
class MemoryManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Manager")

        self.block_sizes = [200, 300, 100, 500, 50,]
        self.blocks = [MemoryBlock(size) for size in self.block_sizes]
        self.allocator = NextFitAllocator(self.blocks)

        self.create_widgets()

    def create_widgets(self):
        self.memory_label = tk.Label(self.master, text="Memory State:", font=("Arial", 12, "bold"))
        self.memory_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.state_text = tk.Text(self.master, width=50, height=10, wrap=tk.WORD, state=tk.DISABLED)
        self.state_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.update_memory_state()

        self.allocate_button = tk.Button(self.master, text="Allocate Process", command=self.allocate_process, width=20)
        self.allocate_button.grid(row=2, column=0, padx=5, pady=5)

        self.deallocate_button = tk.Button(self.master, text="Deallocate Process", command=self.deallocate_process, width=20)
        self.deallocate_button.grid(row=2, column=1, padx=5, pady=5)

        self.final_allocation_button = tk.Button(self.master, text="Final Memory Allocation", command=self.show_final_allocation, width=20)
        self.final_allocation_button.grid(row=3, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit, width=20)
        self.exit_button.grid(row=3, column=1, padx=5, pady=5)

    def update_memory_state(self):
        self.state_text.config(state=tk.NORMAL)
        self.state_text.delete(1.0, tk.END)
        self.state_text.insert(tk.END, "\n".join(self.allocator.DisplayMemoryStatus()))
        self.state_text.config(state=tk.DISABLED)

    def allocate_process(self):
        nameofprocess = simpledialog.askstring("Allocate Process", "Enter the name of the process:")
        if not nameofprocess:
            return

        size_input = simpledialog.askinteger("Allocate Process", "Enter the size of the process (in KB):", minvalue=1)
        if size_input is None:
            return

        success = self.allocator.allocate(nameofprocess, size_input)
        if success:
            messagebox.showinfo("Success", f"Process '{nameofprocess}' allocated successfully.")
        else:
            messagebox.showerror("Error", f"Not enough memory to allocate '{nameofprocess}'.")
        self.update_memory_state()

    def deallocate_process(self):
        nameofprocess = simpledialog.askstring("Deallocate Process", "Enter the name of the process to deallocate:")
        if not nameofprocess:
            return

        success = self.allocator.deallocate(nameofprocess)
        if success:
            messagebox.showinfo("Success", f"Process '{nameofprocess}' deallocated successfully.")
        else:
            messagebox.showerror("Error", f"Process '{nameofprocess}' not found.")
        self.update_memory_state()

    def show_final_allocation(self):
        allocation_details = self.allocator.display_allocation_details()
        if allocation_details:
            final_state = "\n".join(allocation_details)
        else:
            final_state = "No processes are currently allocated."
        messagebox.showinfo("Final Memory Allocation", final_state)
        
#Runs the Memory Manager GUI application using Tkinter main event loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryManagerGUI(root)
    root.mainloop()
