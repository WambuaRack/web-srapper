import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def scrape_website():
    url = url_entry.get()
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Clear previous results
        result_text.delete('1.0', tk.END)

        # Scraping logic example: find all <h2> tags with class 'title'
        titles = soup.find_all('h2', class_='title')

        # Display titles in the GUI
        for index, title in enumerate(titles):
            result_text.insert(tk.END, f"Article {index + 1}: {title.get_text()}\n")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch URL: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
app = tk.Tk()
app.title("Web Scraper with GUI")

# URL Input
url_label = tk.Label(app, text="Enter your URL:")
url_label.pack()

url_entry = tk.Entry(app, width=50)
url_entry.pack()

# Scrape Button
scrape_button = tk.Button(app, text="Scrape", command=scrape_website)
scrape_button.pack()

# Result Display
result_label = tk.Label(app, text="Scraped Titles:")
result_label.pack()

result_text = scrolledtext.ScrolledText(app, width=60, height=10)
result_text.pack()

# Start the GUI main loop
app.mainloop()
