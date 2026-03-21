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

        #  Main Buttons
        btn_frame = tk.Frame(root, bg="#2c3e50")
        btn_frame.pack(pady=10)

        self.scan_btn = tk.Button(btn_frame, text="Start Deep Scan", command=self.start_scan_thread, bg="#27ae60",
                                  fg="white", width=15)
        self.scan_btn.grid(row=0, column=0, padx=5)

        self.save_btn = tk.Button(btn_frame, text="Save Report", command=self.save_results, bg="#2980b9", fg="white",
                                  width=15)
        self.save_btn.grid(row=0, column=1, padx=5)

        #  Network Utilities Section (NEW)
        util_frame = tk.LabelFrame(root, text="Network Utilities", fg="white", bg="#2c3e50", padx=10, pady=10)
        util_frame.pack(pady=10, padx=20, fill="x")

        tk.Button(util_frame, text="Ping Host", command=self.ping_host, bg="#8e44ad", fg="white", width=12).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        tk.Button(util_frame, text="DNS Lookup", command=self.dns_lookup, bg="#d35400", fg="white", width=12).grid(
            row=0, column=1, padx=5)

        # Results Area
        self.result_area = scrolledtext.ScrolledText(root, width=85, height=25, bg="#1e1e1e", font=("Consolas", 10))
        self.result_area.pack(pady=10, padx=20)

        self.result_area.tag_config("open", foreground="#00ff00")
        self.result_area.tag_config("closed", foreground="#ff4444")
        self.result_area.tag_config("info", foreground="#3498db")
        self.result_area.tag_config("header", foreground="#f1c40f", font=("Consolas", 11, "bold"))

    def log(self, message, tag="info"):
        self.result_area.insert(tk.END, message + "\n", tag)
        self.result_area.see(tk.END)

        # Utility Functions
        def ping_host(self):
            target = self.target_entry.get()
            self.log(f"[*] Pinging {target}...", "info")
            # Determine parameter based on OS
            param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
            response = os.system(f"ping {param} {target}")
            if response == 0:
                self.log(f"[+] {target} is reachable!", "open")
            else:
                self.log(f"[-] {target} is down or blocking ICMP.", "closed")

        def dns_lookup(self):
            target = self.target_entry.get()
            try:
                ip = socket.gethostbyname(target)
                self.log(f"[+] DNS Lookup: {target} -> {ip}", "info")
            except:
                self.log(f"[!] Could not resolve {target}", "closed")

