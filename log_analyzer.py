log_file = "sample.log"

error_count = 0
warning_count = 0
info_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

print("Log Summary:")
print("Errors:", error_count)
print("Warnings:", warning_count)
print("Info:", info_count)
