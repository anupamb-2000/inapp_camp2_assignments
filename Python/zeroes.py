#Program to remove zeroes from an IP address

ipAddress = "216.08.094.196"

#Remove zeroes
strippedIPList = ipAddress.split('0')

#Join into a new string
newIP = ""
print(newIP.join(strippedIPList))