#import functionlist
#import functionlist as fn
#from functionlist import add,country
#from functionlist import add as sm,country as cn
#from functionlist import *
import sys
#sys.path.append(r'C:\Users\Krishna\training\codes')

if __name__ == "__main__":
	from functionlist import *
	print("sum : ",add(12,3))
	print("hello ",country)
	
	print(sys.path)