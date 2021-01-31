"""
Write a Python function remove_leading(ip) that, given a string with an IPv4 address ip, returns a new string with all leading zeros removed from ip. An IPv4 address is an address in the format N.N.N.N, where N is an integer in the interval [0, 255].

"""

def remove_leading(ip):
    numbers = ip.split(".")
    for i in range(len(numbers)):
        numbers[i] = str(int(numbers[i]))
    return ".".join(numbers)