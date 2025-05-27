import os

# Set the path to the directory you want to list
directory_path = '/'  # Replace with your path

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
