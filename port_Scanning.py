import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import nmap
import threading
import socket
import os
import platform
from datetime import datetime

class AdvancedScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Network Analysis Tool")
        self.root.geometry("750x850")
        self.root.configure(bg="#2c3e50")

        # --- Input Section ---
        input_frame = tk.Frame(root, bg="#2c3e50")
        # FIXED: Changed 'px=20' to 'padx=20'
        input_frame.pack(pady=20, fill="x", padx=20)

        tk.Label(input_frame, text="Target (IP/Domain):", fg="white", bg="#2c3e50").grid(row=0, column=0, sticky="w")
        self.target_entry = tk.Entry(input_frame, width=30)
        self.target_entry.insert(0, "127.0.0.1")
        self.target_entry.grid(row=0, column=1, padx=10)

        tk.Label(input_frame, text="Ports (e.g. 1-1024):", fg="white", bg="#2c3e50").grid(row=1, column=0, sticky="w",
                                                                                          pady=10)
        self.port_entry = tk.Entry(input_frame, width=30)
        self.port_entry.insert(0, "1-1024")
        self.port_entry.grid(row=1, column=1, padx=10)

        # --- Progress Bar ---
        self.progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
        self.progress.pack(pady=5)