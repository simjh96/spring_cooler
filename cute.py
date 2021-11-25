import re

s = input()
if len(s) <= 4:
    print("not cute")
elif s[-5:] == "driip":
    print("cute")