# example from: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import json

with open('data.json') as json_file:  
    data = json.load(json_file)
    
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')