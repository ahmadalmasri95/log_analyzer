📝 Automated SSH Log Analyzer (SIEM Lite)
Description
A Python-based security tool designed to parse Linux authentication logs (/var/log/auth.log) to identify potential Brute Force attacks. This script automates the tedious process of manual log review by using Regular Expressions (Regex) to extract timestamps, targeted usernames, and source IP addresses.

Key Features
Regex Extraction: Utilizes complex capture groups to isolate Indicators of Compromise (IoCs).

Frequency Analysis: Uses Python’s collections module to rank the most frequent attacking IP addresses.

Volume Identification: Provides a total count of failed login attempts to gauge the scale of the threat.

Robust Error Handling: Validates file existence before processing to prevent script crashes.

Security Logic
The script specifically looks for the "Failed password" pattern, which is the standard indicator of an unsuccessful login attempt in SSHD. By isolating the IP address, security teams can use this data to update Firewall or Fail2Ban rules.

How to Use
Prepare your log file: Ensure you have a .log or .txt file containing standard Linux auth logs.

Run the script:

Bash

python log_parser.py
Analyze the output: The script will display the total number of failures and a "Top 5 Attacking IPs" list.

Sample Output
Plaintext

[+] Total Failed Logins Found: 142

--- Top Attacking IPs ---
IP: 192.168.1.50 | Attempts: 87
IP: 203.0.113.1  | Attempts: 22
IP: 10.0.0.15    | Attempts: 12
Technical Skills Demonstrated
Data Parsing: Transforming unstructured text into structured data.

Regular Expressions: Pattern matching for security forensics.

Python Automation: Streamlining repetitive security tasks.
