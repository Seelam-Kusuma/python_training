import os

def find_largest_file(directory):
    max_size = 0
    largest_file=""
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            if size > max_size:
                max_size = size
                largest_file = path
    
    return largest_file, max_size

# Replace 'your_directory_path' with the path to your directory
directory_path = r'C:\Users\Kusuma\handson'
file,size = find_largest_file(directory_path)
print(f'largest file:{file}({size} bytes)')

