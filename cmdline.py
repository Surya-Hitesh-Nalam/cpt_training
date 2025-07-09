import sys
'''print("Script name:", sys.argv[0])
print("All args:",sys.argv[1:])
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")
'''

'''nums1 = int(sys.argv[1])
nums2 = int(sys.argv[2])
nums3 = int(sys.argv[3])
print("Product:",nums1*nums2*nums3)'''

'''if len(sys.argv) != 3:
    print("Usage: python sample.py 1 b")
else:
    l=float(sys.argv[1])
    b=float(sys.argv[2])
print("Calculated area:",l*b)'''

'''if len(sys.argv)<2:
    print("Uagage: Python sample.py n1,n2...")
    sys.exit()
nums=[int(arg) for arg in sys.argv[1:]]
total = sum(nums)
print("Numbers:",numbers)
print("Sum:",total)'''

'''import argparse
parser=argparse.ArgumentParser(description=" Add 2 Number")
parser.add_argument('--x',type=int,required=True,help="First number")
parser.add_argument('--y',type=int,required=True,help="Second number")
parser.add_argument('--opt',type=str,required=True,choices=['add','sub','mul','div'],help="operation")
args=parser.parse_args()
result = 0
if args.opt=='add':
    result = args.x+args.y
elif args.opt == 'sub':
    result = args.x-args.y
elif args.opt=='mul':
    result = args.x*args.y
elif args.opt == 'div':
    result = args.x/args.y
print("Result is:",result)'''

'''import os
path="."
files=os.listdir(path)
print("files and folders in current directory")
for f in files:
    print(f)'''

import os
'''folder = "new_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created")
else:
    print(f"Folder '{folder}' already exists")'''

'''file = "DeleteMe.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"{file} deleted.")
else:
    print("File not found")'''

file = "cmdline.py"
if os.path.exists(file):
    size = os.path.getsize(file)
    print(f"{file} size:{size} bytes.")
else:
    print("File not found")


    










