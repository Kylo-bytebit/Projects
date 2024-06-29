import tkinter as tk
from tkinter import filedialog, messagebox


#Functions
#String Processing
def string_check():
    new_window = tk.Toplevel(root)
    new_window.title("String Check")
    new_window.geometry("300x300")

    label = tk.Label(new_window, text="Enter a string:")
    label.pack(pady=10)

    entry = tk.Entry(new_window)
    entry.pack(pady=10)

    def check_string():
        ent = entry.get()
 # Check string length
        length = len(ent)
        messagebox.showinfo("String Length", f"The length of the string is: {length}")

        # Check for alphabetic 
        if ent.isalpha():
            messagebox.showinfo("Alphabetic ", "The string contains alphabets .")
        else:
            messagebox.showinfo("Alphabetic ", "The string contains non alphabetic characters .")

        # Check for digits
        if ent.isdigit():
            messagebox.showinfo("Digits", "The string contains digits.")
        else:
            messagebox.showinfo("Digits", "The string contains no digits .")

        # Check for whitespace
        if ent.isspace():
            messagebox.showinfo("Whitespace", "The string contains whitespace .")
        else:
            messagebox.showinfo("Whitespace", "The string contains non whitespace characters .")

        # Check for prefixes and suffixes
        if ent.startswith("prefix"):
            messagebox.showinfo("Prefix", "The string starts with the prefix 'prefix'.")
        if ent.endswith("suffix"):
            messagebox.showinfo("Suffix", "The string ends with the suffix 'suffix'.")
        new_window.destroy()

    button = tk.Button(new_window, text="Check", command=check_string)
    button.pack(pady=10)


def string_find():
    new_window = tk.Toplevel(root)
    new_window.title("String Find")
    new_window.geometry("300x300")

    label1 = tk.Label(new_window, text="Enter a string:")
    label1.pack(pady=5)
    entry1 = tk.Entry(new_window)
    entry1.pack(pady=5)

    label2 = tk.Label(new_window, text="Find in String:")
    label2.pack(pady=5)
    entry2 = tk.Entry(new_window)
    entry2.pack(pady=5)

    def find_string():
        ent = entry1.get()
        find = entry2.get()

        if find in ent:
            messagebox.showinfo("Find", f"String contains {find}")
        else:
            messagebox.showerror("Error", f"String Does not contain {find}")
        new_window.destroy()

    button = tk.Button(new_window, text="Find", command=find_string)
    button.pack(pady=10)

def string_replace():

    new_window = tk.Toplevel(root)
    new_window.title("String Replace")
    new_window.geometry("300x300")

    label1 = tk.Label(new_window, text="Enter a string:")
    label1.pack(pady=5)
    entry1 = tk.Entry(new_window)
    entry1.pack(pady=5)

    label2 = tk.Label(new_window, text="Replace:")
    label2.pack(pady=5)
    entry2 = tk.Entry(new_window)
    entry2.pack(pady=5)

    label3 = tk.Label(new_window, text="Replace With:")
    label3.pack(pady=5)
    entry3 = tk.Entry(new_window)
    entry3.pack(pady=5)



    def replace_string():
        ent = entry1.get()
        rep = entry2.get()
        repw = entry3.get()

        if rep in ent:
            result= ent.replace(rep,repw)
            messagebox.showinfo("Replace",f"String has replced {rep} with {repw} ({result})")

        else:
            messagebox.showerror("Error",f"String Does not contain {rep}")
    
    button = tk.Button(new_window, text="Replace", command=replace_string)
    button.pack(pady=10)


def string_swap():
    new_window = tk.Toplevel(root)
    new_window.title("String Swap")
    new_window.geometry("300x300")

    label1 = tk.Label(new_window, text="Enter a string:")
    label1.pack(pady=5)
    entry1 = tk.Entry(new_window)
    entry1.pack(pady=5)

    label2 = tk.Label(new_window, text="Swap with:")
    label2.pack(pady=5)
    entry2 = tk.Entry(new_window)
    entry2.pack(pady=5)

    def swap_string():
        ent = entry1.get()
        swap = entry2.get()
        temp = ent
        ent = swap
        swap = temp
        result= ent +swap
        messagebox.showinfo("Replace",f"the Swap of String one is ({ent}) and String two ({swap})         ('{result}') ")
    button = tk.Button(new_window, text="Swap", command=swap_string)
    button.pack(pady=10)

 
def string_con():

    new_window = tk.Toplevel(root)
    new_window.title("String Concatenation")
    new_window.geometry("300x300")

    label1 = tk.Label(new_window, text="Enter a string:")
    label1.pack(pady=5)
    entry1 = tk.Entry(new_window)
    entry1.pack(pady=5)

    label2 = tk.Label(new_window, text="Enter Second String")
    label2.pack(pady=5)
    entry2 = tk.Entry(new_window)
    entry2.pack(pady=5)

    def con_string():
        vara = entry1.get()
        varb = entry2.get()
 
        result = vara + varb
        messagebox.showinfo("Result",f"Your Combined String is ({result})")
    button = tk.Button(new_window, text="Combine", command=con_string)
    button.pack(pady=10)

def string_comp():
    new_window = tk.Toplevel(root)
    new_window.title("String Comparison")
    new_window.geometry("300x300")

    label1 = tk.Label(new_window, text="Enter a string:")
    label1.pack(pady=5)
    entry1 = tk.Entry(new_window)
    entry1.pack(pady=5)

    label2 = tk.Label(new_window, text="Find in String:")
    label2.pack(pady=5)
    entry2 = tk.Entry(new_window)
    entry2.pack(pady=5)

    def comp_string():

        strnga = entry1.get()
        strngb = entry2.get()

        if strnga == strngb:
            messagebox.showinfo("Result",f"String a ({strnga}) is equal to String b ({strngb})")
        else:
            messagebox.showerror("Result",f"String a ({strnga}) is not equal to String b ({strngb})")

        if len(strnga) == len(strngb):
            messagebox.showinfo("Result",f"String a ({strnga}) is equal in lenght with String b ({strngb})")
        else:
            messagebox.showinfo("Result",f"String a ({strnga}) is not equal in lenght with String b ({strngb}) ")
     
    button = tk.Button(new_window, text="Compare", command=comp_string)
    button.pack(pady=10)


#File Handling

def open_file():
    # Define the file operations functions
    def read_text_file(filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filename}' not found.")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file '{filename}': {e}")
            return None

    def write_text_file(filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            messagebox.showinfo("Success", f"Data written to '{filename}' successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to file '{filename}': {e}")

    def read_file():
        filename = filedialog.askopenfilename(title="Select a file to read")
        if filename:
            content = read_text_file(filename)
            if content:
                text_widget.delete("1.0", tk.END)  # Clear previous content
                text_widget.insert(tk.END, content)

    def write_file():
        content = text_widget.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(title="Save as")
        if filename:
            write_text_file(filename, content)

    # Create the Tkinter window
    window = tk.Tk()
    window.title("File Reader/Writer")

    # Create the text widget to display file content
    text_widget = tk.Text(window, height=10, width=50)
    text_widget.pack()

    # Create buttons to trigger file operations
    read_button = tk.Button(window, text="Read File", command=read_file)
    read_button.pack(pady=5)

    write_button = tk.Button(window, text="Write File", command=write_file)
    write_button.pack(pady=5)

    # Start the Tkinter event loop
    window.mainloop()


# Create the main window
root = tk.Tk()
root.title("String Manipulator")
root.geometry("400x300")

# Buttons
button_row = 0
button_col = 0

button = tk.Button(root, text="Check String ", command=string_check)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button = tk.Button(root, text="Swap String ", command=string_swap)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button = tk.Button(root, text="Find in String", command=string_find)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button_row += 5
button_col = 0

button = tk.Button(root, text="Replace in String", command=string_replace)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button = tk.Button(root, text="String Concatenation", command=string_con)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button = tk.Button(root, text="String Comparison", command=string_comp)
button.grid(row=button_row, column=button_col, padx=10, pady=10)
button_col += 1

button_row += 5
button_col = 0

button = tk.Button(root, text="Open file", command=open_file)
button.grid(row=button_row, column=button_col, padx=10, pady=10)




#OOP Module

class File:
    def __init__(self, fname):
        self.__filename = fname

    def read(self):
        with open(self.__filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.__filename, 'w') as file:
            file.write(data)

class StringProcessor:
    def __init__(self, sdata):  # Customizable variable
        self.__data = sdata  # Private attribute

    def reverse(self):
        return self.__data[::-1]

    def capitalize(self):
        return self.__data.capitalize()


# inheritance
class CustomStringProcessor(StringProcessor):
    def split(self, deli=' '):
        return self._StringProcessor__data.split(delimiter)
    
# overloading operator
class CustomString:
    def __init__(self, value):  # Customizable variable
        self.value = value  # Customizable variable

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, n):
        return self.value * n

    def __str__(self):
        return f"CustomString('{self.value}')"




# Run the main loop
root.mainloop()