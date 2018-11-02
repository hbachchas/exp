# Check whether GPU is being or not
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())