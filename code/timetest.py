import time
from datetime import datetime


current_time = datetime.now().strftime("%Y_%m_%d__%H:%M:%S")
file_out = './recordings/' + current_time + '.avi'

print(file_out)