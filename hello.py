cat_art = """
 /\\_/\\  
( o.o ) 
 > ^ <
"""
print(cat_art)

import catqdm
import time

from catqdm import big_cat_bar

for _ in big_cat_bar(range(100)):
    time.sleep(0.05)