
import os
from . import uk_all_cities
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import sys
sys.path
print(sys.path)
# from listings import models


currDir = os.path.dirname(__file__)
listingsFP = os.path.join(currDir, 'listings data.xlsx')

startRange = 5
endRange = 20

listings = []
listingsData = pd.read_excel(listingsFP, sheet_name='Sheet1')

for l in range(startRange, endRange):
    listings.append(
        {
            'agent': listingsData['agent'][l],
            'title': listingsData['title'][l],
            'address': listingsData['address'][l],
            'city': listingsData['city'][l],
            'postcode': listingsData['postcode'][l],
            'longitute': listingsData['longitude'][l],
            'latitude': listingsData['latitude'][l],
            'description': listingsData['description'][l],
            'price': listingsData['price'][l],
            'bedrooms': listingsData['bedrooms'][l],
            'bathrooms': listingsData['bathrooms'][l],
            'garage': listingsData['garage'][l],
        }
    )
