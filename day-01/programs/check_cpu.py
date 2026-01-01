import psutil # import the library from pypi

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold : ")) # DONE

    current_cpu = psutil.cpu_percent(interval=1) # DONE
    print("Current CPU %: ",current_cpu)
    if current_cpu > cpu_threshold:  # DONE
        print("CPU Alert Email sent...") # dummy email
    else:
        print("CPU in Safe state...")


check_cpu_threshold()