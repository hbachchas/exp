# example from: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import json

data = {}
with open('imagenet_class_index.json') as json_file:  
    data = json.load(json_file)

with open('imagenet_class_index_indented.json', 'w') as outfile:  
    json.dump(data, outfile, sort_keys=True, indent=4)
