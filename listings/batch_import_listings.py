import os
import json

fp = os.path.join(os.path.dirname(os.path.abspath(__file__)),'new_listings.json')

with open(fp) as json_file:
    print (json_file)
    listings = json.load(json_file,)
    for listing in listings:
        print (listing[0])


