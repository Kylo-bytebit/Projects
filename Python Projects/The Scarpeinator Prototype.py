import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from website
def webscraper(url, tag, attributes):
    scrape_target = requests.get(url)
    soup = BeautifulSoup(scrape_target.content, 'html.parser')
    scrape_tag = soup.find_all(tag, class_=attributes)
    scrape_attrs = soup.find_all(tag, class_=attributes)
    result(scrape_tag, scrape_attrs)

# Function to process and display the scraped data
def result(scrape_tag, scrape_attrs):
    results = []
    for i in range(len(scrape_tag)):
        text = scrape_tag[i].text
        attrs = scrape_attrs[i].text
        results.append((text, attrs))
        text_box.insert(tk.END, f"Tag: {text}\nAttributes: {attrs}\n\n")
    return results

# Function to save results to a CSV file
def save_to_csv():
    data = text_box.get("1.0", tk.END).strip().split("\n\n")
    rows = [row.split("\n") for row in data]
    df = pd.DataFrame(rows, columns=["Tag", "Attributes"])
    df.to_csv("scraped_data.csv", index=False)

# Function to add new entries and labels
def add_entries():
    row = frame.grid_size()[1]  # Get the current number of rows in the grid

    label_url = ttk.Label(frame, text="Enter a URL:")
    label_url.grid(row=row, column=0, padx=5, pady=5, sticky="ew")

    entry_url = ttk.Entry(frame, width=20)
    entry_url.grid(row=row + 1, column=0, padx=5, pady=5, sticky="ew")

    label_tag = ttk.Label(frame, text="Enter Tag:")
    label_tag.grid(row=row + 2, column=0, padx=5, pady=5, sticky="ew")

    entry_tag = ttk.Entry(frame, width=20)
    entry_tag.grid(row=row + 3, column=0, padx=5, pady=5, sticky="ew")

    label_attr = ttk.Label(frame, text="Enter Attributes/Class:")
    label_attr.grid(row=row + 4, column=0, padx=5, pady=5, sticky="ew")

    entry_attr = ttk.Entry(frame, width=20)
    entry_attr.grid(row=row + 5, column=0, padx=5, pady=5, sticky="ew")

# Function to add only the "Enter Tag" and "Enter Attributes/Class" sections
def add_tag_and_attr():
    row = frame.grid_size()[1]  # Get the current number of rows in the grid

    label_tag = ttk.Label(frame, text="Enter Tag:")
    label_tag.grid(row=row, column=0, padx=5, pady=5, sticky="ew")

    entry_tag = ttk.Entry(frame, width=20)
    entry_tag.grid(row=row + 1, column=0, padx=5, pady=5, sticky="ew")

    label_attr = ttk.Label(frame, text="Enter Attributes/Class:")
    label_attr.grid(row=row + 2, column=0, padx=5, pady=5, sticky="ew")

    entry_attr = ttk.Entry(frame, width=20)
    entry_attr.grid(row=row + 3, column=0, padx=5, pady=5, sticky="ew")

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter Layout")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the widgets
frame = ttk.Frame(scrollable_frame, padding="10", width=1280, height=720)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a label
label = ttk.Label(frame, text="Enter a URL:")
label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Add an entry widget
entry = ttk.Entry(frame, width=20)
entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Add a label
label2 = ttk.Label(frame, text="Enter Tag:")
label2.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

# Add an entry widget
entry2 = ttk.Entry(frame, width=20)
entry2.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# Add a label
label3 = ttk.Label(frame, text="Enter Attributes/Class:")
label3.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# Add an entry widget
entry3 = ttk.Entry(frame, width=20)
entry3.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# Add a button to scrape data
button = ttk.Button(frame, text="Scrape", command=lambda: webscraper(entry.get(), entry2.get(), entry3.get()))
button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.S)

# Add a button to add new entries and labels
add_button = ttk.Button(frame, text="Add Entries", command=add_entries)
add_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.S)

# Add a button to add only the "Enter Tag" and "Enter Attributes/Class" sections
add_tag_attr_button = ttk.Button(frame, text="Add Tag and Attributes", command=add_tag_and_attr)
add_tag_attr_button.grid(row=8, column=0, padx=5, pady=5, sticky=tk.S)

# Add a text box to display results
text_box = tk.Text(frame, height=10, width=50)
text_box.grid(row=9, column=0, padx=5, pady=5, sticky="ew")

# Add a button to save results to a CSV file
save_button = ttk.Button(frame, text="Save to CSV", command=save_to_csv)
save_button.grid(row=10, column=0, padx=5, pady=5, sticky=tk.S)

# Configure the grid to expand
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start the Tkinter event loop
root.mainloop()