# Dictionaries.py
#Key-Values

#OR: d = dict()
d = {}

d["George"] = 24
d["Tom"] = 32
d["Jennie"] = 16

#Prints Value associated with George
print(d["George"])
#Override Value
d["Jennie"] = 25

#Keys can only be Strings or Numbers
#How to iterate over key-value pairs in a Dictionary
for key, value in d.items():
    print("Key:")
    print(key)
    print("Value:")
    print(value)
    print('')
