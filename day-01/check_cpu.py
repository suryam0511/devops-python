#fetch CPU threshold usage

# psutil library 

import psutil

def get_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU usage threshold (%): "))

    current_cpu = psutil.cpu_percent(interval=1)  # Simulated current CPU usage
    print(f"Current CPU Usage: {current_cpu}%")
    
    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    else:
        print("CPU usage is normal.")

get_cpu_threshold()
