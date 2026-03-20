from collections import Counter

log_file = "sample.log"
report_file = "report.txt"

log_types = []

# Read log file
with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            log_types.append("ERROR")
        elif "WARNING" in line:
            log_types.append("WARNING")
        elif "INFO" in line:
            log_types.append("INFO")

# Count logs
result = Counter(log_types)

# Write report
with open(report_file, "w") as report:
    report.write("Log Analysis Report\n")
    report.write("===================\n")
    for key, value in result.items():
        report.write(f"{key}: {value}\n")

print("Report generated successfully!")
