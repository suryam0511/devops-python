import psutil

# Function to get user thresholds
def get_thresholds():
    cpu_threshold = int(input("Enter CPU usage threshold (%) : "))
    memory_threshold = int(input("Enter Memory usage threshold (%) : "))
    disk_threshold = int(input("Enter Disk usage threshold (%) : "))
    return cpu_threshold, memory_threshold, disk_threshold


# Function to check system health
def check_system_health(cpu_t, mem_t, disk_t):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print("\n--- System Health Report ---")

    if cpu_usage > cpu_t:
        print(f"CPU WARNING: {cpu_usage}% used")
    else:
        print(f"CPU OK: {cpu_usage}% used")

    if memory_usage > mem_t:
        print(f"MEMORY WARNING: {memory_usage}% used")
    else:
        print(f"MEMORY OK: {memory_usage}% used")

    if disk_usage > disk_t:
        print(f"DISK WARNING: {disk_usage}% used")
    else:
        print(f"DISK OK: {disk_usage}% used")


# Main program
def main():
    cpu_t, mem_t, disk_t = get_thresholds()
    check_system_health(cpu_t, mem_t, disk_t)


main()
