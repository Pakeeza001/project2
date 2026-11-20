failed = 0
error = 0
login = 0
ip_count = {}

# Use 'with' to safely open and automatically close the file
try:
    with open("log.txt", "r") as file:
        for line in file:
            upper_line = line.upper()

            if "FAILED" in upper_line:
                failed += 1

                # Extract the IP cleanly, even if there is more text after it
                if "ip=" in line:
                    ip_part = line.split("ip=")[1]
                    ip = ip_part.split()[0].strip(",;")
                    ip_count[ip] = ip_count.get(ip, 0) + 1

            elif "LOGIN" in upper_line:
                login += 1

            if "ERROR" in upper_line:
                error += 1

    print("=== SECURITY LOGS REPORT ===")
    print("FAILED LOGIN:", failed)
    print("ERROR:", error)
    print("LOGIN:", login)

    print("\n=== SUSPICIOUS IPs ===")
    found_suspicious = False
    for ip, count in ip_count.items():
        if count >= 3:
            print("POSSIBLE SUSPICIOUS IP:", ip, "TOTAL ATTEMPTS:", count)
            found_suspicious = True

    if not found_suspicious:
        print("None detected.")

except FileNotFoundError:
    print("Error: 'log.txt' was not found. Make sure it is in the same folder as your script.")

