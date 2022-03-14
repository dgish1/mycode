#!/usr/bin/env python3

# Define IP list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#Print the IP addresses
# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
