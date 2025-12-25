import re
from collections import Counter

filename = input("Please enter the filename: ")

try:
    with open(filename, "r") as file:
        log_data = file.read()

    # The pattern you wrote is solid! 
    # We add 're.MULTILINE' so '^' works for every line in the file.
    failed_login_pattern = r"^([A-Z][a-z]{2}\s+\d{1,2}\s\d{2}:\d{2}:\d{2})\s.*Failed password for (?:invalid user )?(\S+) from ([\d.]+)"
    
    # findall returns a list of tuples: (timestamp, username, ip)
    matches = re.findall(failed_login_pattern, log_data, re.MULTILINE)

    # 1. Count total failures
    total_failures = len(matches)
    print(f"\n[+] Total Failed Logins Found: {total_failures}")

    # 2. Extract and count IP addresses
    # The IP is the 3rd group in our tuple (index 2)
    ips = [match[2] for match in matches]
    ip_counts = Counter(ips)

    print("\n--- Top Attacking IPs ---")
    for ip, count in ip_counts.most_common(5):
        print(f"IP: {ip} | Attempts: {count}")

except FileNotFoundError:
    print("Error: That file was not found. Please check the path.")
