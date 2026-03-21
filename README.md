Advanced Port Scanner Tool
A sophisticated graphical port scanning utility built with Python and Tkinter that leverages the power of Nmap to provide detailed network reconnaissance information through an intuitive interface.

Features
User-friendly Graphical Interface - Clean, modern UI for easy interaction
Multiple Scan Types:
Basic port scanning
Version detection scanning
Service information gathering
OS detection (requires admin/root privileges)
Real-time Results - View scan results as they're discovered
Color-coded Results - Quickly identify open, closed, or filtered ports
Custom Port Ranges - Scan specific port ranges or use preset options
Progress Tracking - Monitor scan progress with a visual progress bar
Result Saving - Export scan results to text files for documentation
Network Utilities:
Ping hosts
DNS lookups
Whois information

Installation
Prerequisites
Python 3.x
Tkinter (usually included with Python)
Nmap
python-nmap library

Basic Scanning
Enter Target Information:

Input the IP address of the target
Select a port range (e.g., 1-1024 for common ports)
Configure Scan Options:

Choose a scan type from the dropdown menu
Start Scanning:

Click "Start Scan" to begin
Watch the progress bar for scan status
View Results:

Results appear in the table as they're discovered
Green rows indicate open ports
Red rows indicate closed ports
Yellow rows indicate filtered ports
Save Results:

Click "Save Results" to export scan data to a text file
