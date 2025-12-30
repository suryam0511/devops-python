# import psutil

# # Function to get user thresholds
# def get_thresholds():
#     cpu_threshold = int(input("Enter CPU usage threshold (%) : "))
#     memory_threshold = int(input("Enter Memory usage threshold (%) : "))
#     disk_threshold = int(input("Enter Disk usage threshold (%) : "))
#     return cpu_threshold, memory_threshold, disk_threshold


# # Function to check system health
# def check_system_health(cpu_t, mem_t, disk_t):
#     cpu_usage = psutil.cpu_percent(interval=1)
#     memory_usage = psutil.virtual_memory().percent
#     disk_usage = psutil.disk_usage('/').percent

#     print("\n--- System Health Report ---")

#     if cpu_usage > cpu_t:
#         print(f"CPU WARNING: {cpu_usage}% used")
#     else:
#         print(f"CPU OK: {cpu_usage}% used")

#     if memory_usage > mem_t:
#         print(f"MEMORY WARNING: {memory_usage}% used")
#     else:
#         print(f"MEMORY OK: {memory_usage}% used")

#     if disk_usage > disk_t:
#         print(f"DISK WARNING: {disk_usage}% used")
#     else:
#         print(f"DISK OK: {disk_usage}% used")


# # Main program
# def main():
#     cpu_t, mem_t, disk_t = get_thresholds()
#     check_system_health(cpu_t, mem_t, disk_t)


# main()


#!/usr/bin/env python3

try:
    import psutil
except ImportError:
    print("Error: psutil module not installed.")
    print("Install it using: pip install psutil")
    exit(1)


def get_cpu_usage():
    """Returns CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Returns memory usage percentage."""
    return psutil.virtual_memory().percent


def get_disk_usage(path="/"):
    """Returns disk usage percentage for given path."""
    return psutil.disk_usage(path).percent


def main():
    try:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()

        print("System Health Report")
        print("--------------------")
        print(f"CPU Usage    : {cpu_usage}%")
        print(f"Memory Usage : {memory_usage}%")
        print(f"Disk Usage   : {disk_usage}%")

    except Exception as error:
        print("An unexpected error occurred:")
        print(error)


if __name__ == "__main__":
    main()
