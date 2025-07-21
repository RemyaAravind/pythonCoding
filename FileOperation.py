import os

# Check if file exists
if os.path.exists('file.txt'):
    print('File exists')

# Get file size
size = os.path.getsize('file.txt') 

# Get file modification time
import time
mod_time = os.path.getmtime('file.txt') # in which format 
readable_time = time.ctime(mod_time) #output


##########################################################################################

