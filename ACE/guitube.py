import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube

def show_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    p = (int)(bytes_downloaded * 100 / stream.filesize)
    progress_var.set(p)
    progress_bar.update()

def download_video():
    link = url_entry.get()
    resolution = resolution_var.get()

    try:
        video = YouTube(link, on_progress_callback=show_progress)
        stream = video.streams.filter(res=resolution).first()

        if stream:
            messagebox.showinfo("Download Started", f"Downloading {video.title} in {resolution} resolution...")
            stream.download()
            messagebox.showinfo("Download Complete", "Download completed!")
            progress_var.set(0)  # Reset progress bar after download
        else:
            messagebox.showerror("Error", f"Sorry, {resolution} resolution is not available for this video.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x250")
root.resizable(False, False)
root.configure(background="#f0f0f0")

# Title Label
title_label = ttk.Label(root, text="YouTube Video Downloader", font=("Arial", 16), background="#f0f0f0")
title_label.pack(pady=(10, 20))

# URL Entry
url_label = ttk.Label(root, text="Enter the URL of the video:", background="#f0f0f0")
url_label.pack(pady=(0, 5))
url_entry = ttk.Entry(root, width=40)
url_entry.pack()

# Resolution Selection
resolution_label = ttk.Label(root, text="Select the resolution:", background="#f0f0f0")
resolution_label.pack(pady=(10, 5))
resolution_var = tk.StringVar()
resolution_var.set("720p")  # Default resolution
resolutions = ["1080p", "720p", "480p", "360p"]
resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=resolutions, state="readonly", width=37)
resolution_menu.pack()

# Download Button
download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack(pady=(20, 10))

# Progress Frame
progress_frame = ttk.Frame(root)
progress_frame.pack(pady=(0, 10))

progress_label = ttk.Label(progress_frame, text="Download Progress:", background="#f0f0f0")
progress_label.pack(side="left")

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=200, mode="determinate", variable=progress_var)
progress_bar.pack(side="left", padx=10)

# Start the Tkinter event loop
root.mainloop()
