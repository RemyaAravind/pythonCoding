#JSON Files
import json

# Reading JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Writing JSON
data = {'name': 'Alice', 'age': 30}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)   #indent?

#Binary Files
# Reading binary file
with open('image.jpg', 'rb') as f:
    binary_data = f.read()

# Writing binary file
with open('copy.jpg', 'wb') as f:
    f.write(binary_data)


#Working with Paths
from pathlib import Path

# Modern way to handle paths
file_path = Path('folder/file.txt')
if file_path.exists():
    content = file_path.read_text()
    
# Create directories if they don't exist
file_path.parent.mkdir(parents=True, exist_ok=True)

#Temporary Files
import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write('Temporary content')
    temp_filename = temp_file.name

#File Encoding
# Specify encoding (important for non-ASCII characters)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

#Processing Large Files
def process_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:  # Memory efficient - reads one line at a time
            # Process line
            yield line.strip()

#Backup and Safe Writing
import shutil
import os
def safe_write(filename, content):
    backup_name = filename + '.backup'
    
    # Create backup if file exists
    if os.path.exists(filename):
        shutil.copy2(filename, backup_name)
    
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        # Restore backup if write fails
        if os.path.exists(backup_name):
            shutil.copy2(backup_name, filename)
        raise e
