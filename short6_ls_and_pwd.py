import os

pwd = os.getcwd()

print("Present Working Directory:", pwd)

# List the contents of the present working directory
contents = os.listdir(pwd)
print("Contents of the directory:")
for item in contents:
    print(item)