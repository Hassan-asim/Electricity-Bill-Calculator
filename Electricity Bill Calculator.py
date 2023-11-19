import tkinter as tk

# Source data
source_matrix = [
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240]
]

# Declare result_text as a global variable
result_text = None

# Function to handle button 1 click
def display_slab1_and_slab2():
    result_text.config(state=tk.NORMAL)  # Enable text box for editing
    result_text.delete(1.0, tk.END)  # Clear existing text
    result_text.insert(tk.END,
                                f'The bill for Slab 1 is\n{source_matrix[0][0]*10} {source_matrix[0][1]*10} {source_matrix[0][2]*10}\n'
                                f'The bill for Slab 2 is\n{source_matrix[1][0]*15} {source_matrix[1][1]*15} {source_matrix[1][2]*15}')
    result_text.config(state=tk.DISABLED)  # Disable text box for editing

# Function to handle button 2 click
def display_slab3():
    result_text.config(state=tk.NORMAL)  # Enable text box for editing
    result_text.delete(1.0, tk.END)  # Clear existing text
    result_text.insert(tk.END, f'The bill for Slab 3 is\n{source_matrix[2][0]*20} {source_matrix[2][1]*20} {source_matrix[2][2]*20}')
    result_text.config(state=tk.DISABLED)  # Disable text box for editing

# Function to close the current window and open the matrix window
def open_matrix_window():
    student_id = entry_student_id.get()
    main_window.destroy()  # Close the student ID window

    # Create a new window for displaying the matrix and calculating the bill
    matrix_window = tk.Tk()
    matrix_window.title("Electricity Bill Calculator")
    matrix_window.geometry("500x300")  # Set window size

    # Display student's ID at the top
    student_id_label = tk.Label(matrix_window, text=f"Student ID: {student_id}")
    student_id_label.pack()

    # Display the source matrix
    matrix_label = tk.Label(matrix_window, text="Source Matrix:")
    matrix_label.pack()

    for i, row in enumerate(source_matrix, start=1):
        slab_label = tk.Label(matrix_window, text=f'slab {i} : {row[0]}  {row[1]}  {row[2]}')
        slab_label.pack()
        
    
    
    # Buttons for options 1 and 2
    button_slab12 = tk.Button(matrix_window, text="BUTTON 1", command=display_slab1_and_slab2)
    button_slab12.pack(pady=5)  

    button_slab3 = tk.Button(matrix_window, text="BUTTON 2", command=display_slab3)
    button_slab3.pack(pady=10)

    # Text box to display the result
    global result_text
    result_text = tk.Text(matrix_window, height=5, width=40, state=tk.DISABLED)
    result_text.pack()
    result_text.config(state=tk.NORMAL)  # Enable text box for editing
    result_text.delete(1.0, tk.END)  # Clear existing text
    result_text.insert(tk.END, f'press BUTTON 1 for BILL of slab 1 & 2\n'
                        f'press BUTTON 2 for BILL of slab 3\n')
    result_text.config(state=tk.DISABLED)  # Disable text box for editing

    matrix_window.mainloop()

# GUI setup for student ID window
main_window = tk.Tk()
main_window.title("Electricity Bill Calculator")
main_window.geometry("500x300")  # Set window size

# Entry for entering student ID
student_id_label = tk.Label(main_window, text="Enter Student ID:")
student_id_label.pack()

entry_student_id = tk.Entry(main_window)
entry_student_id.pack()

# Center the entry and label horizontally and vertically
student_id_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
entry_student_id.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Bind the Enter key to open_matrix_window function
entry_student_id.bind('<Return>', lambda event=None: open_matrix_window())

main_window.mainloop()
