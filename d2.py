import re
import sys

x = input()
if re.search(r'[dD]2',x):
    print('D2')
else:
    print('unrated')
