#!/usr/bin/env python3

#import sys
#
#if len(sys.argv) != 0:
#    print(f"Usage: {sys.argv[0]} name age")
#    sys.exit(1)
#elif len(sys.argv) >= 4:
#    print(f"Usage: {sys.argv[0]} name age")
#    sys.exit(1)
#name = sys.argv[1]
#age = sys.argv[2]


#print(f"Hi {name}, you are {age} years old.")

#!/usr/bin/env python3

import sys

    # Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

    # Assign command-line arguments to variables
name = sys.argv[1]
age = sys.argv[2]

    # Print the output in the required format
result = 'Hi ' + name + ', you are ' + str(age) + ' years old.'

print(result)
