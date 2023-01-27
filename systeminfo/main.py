#This program uses the platform module to get the name of the machine and the operating system name and version. 
# It uses the psutil module to get the number of CPU's and amount of memory. It uses the socket module to get 
# the IP address of the machine. And it uses the timeit module to compute a CPU strength score.

import platform
import psutil
import socket
import timeit

# name of machine
print("Name of Machine: ", platform.node())

# operating system name
print("Operating System Name: ", platform.system())

# operating system version
print("Operating System Version: ", platform.release())

# number of cpu's
print("Number of CPUs: ", psutil.cpu_count())

# amount of memory
memory = psutil.virtual_memory()
print("Amount of Memory: ", memory.total / (1024.0 ** 3), "GB")

# IP address of machine
print("IP Address: ", socket.gethostbyname(socket.gethostname()))

# CPU strength score
def test_cpu():
    for i in range(100000):
        for j in range(100000):
            k = i * j

print("CPU Strength Score: ", timeit.timeit(test_cpu))