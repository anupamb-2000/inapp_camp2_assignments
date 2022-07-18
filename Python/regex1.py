#Program that matches a string that has an 'a' followed by anthing, ending in 'b'
import re

regex = ".*a.*b"

print(re.findall(regex, "Aaaaaasdandandjnab"))
print(re.findall(regex, "abhhubdjjjj"))