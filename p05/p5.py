"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys 

x=20

for i in range(1, 200000000):
	x +=20
	if (x % 2 == 0):
		if(x % 3 == 0):
			if (x % 4 == 0):
				if (x % 5 == 0):
					if (x % 6 == 0):
						if (x % 7 ==0) and (x % 8 ==0) and (x % 9 ==0) and ( x % 10 ==0) and (x % 11 ==0) and (x % 12 ==0) and (x % 13 ==0) and (x % 14 ==0) and (x % 15 ==0) and (x % 16 ==0) and (x % 17 ==0) and (x % 18 ==0) and (x % 19 ==0) and (x % 19 ==0): print(x); sys.exit();
	
