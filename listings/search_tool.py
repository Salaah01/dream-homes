import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dream_homes.settings")
import re
from .uk_all_cities import all_cities, cities_by_country
from .choices import price_choices

class SearchListings():

    def __init__(self, request='', queryset_list=[]):
        self.queryset_list = queryset_list
        self.request = request

    def searchFields(self):
        self.queryset_list = self.keywords()
        self.queryset_list = self.location()
        self.queryset_list = self.bedrooms()
        self.queryset_list = self.price()
        return self.queryset_list
    
    def keywords(self):
        if 'keywords' in self.request:
            keywords = self.request['keywords']
            if keywords:
                if ", " in keywords:
                    keywords = keywords.split(', ')
                else:
                    keywords = keywords.split(',')
                for keyword in keywords:
                    self.queryset_list = self.queryset_list.filter(description__icontains=keyword)    
        return self.queryset_list

    def bedrooms(self):
        if 'bedrooms' in self.request:
            bedrooms = self.request['bedrooms']
            if bedrooms:
                if bedrooms == "5+":
                    self.queryset_list = self.queryset_list.filter(bedrooms__gte=6)
                elif bedrooms == "0":
                    pass
                else:
                    self.queryset_list = self.queryset_list.filter(bedrooms__iexact=bedrooms)
        return self.queryset_list

    def price(self):
        if 'price' in self.request:
            price = self.request['price']
            if price and price != 'max':
                self.queryset_list = self.queryset_list.filter(price__lte=price)
            elif price == 'max':
                # Calculate the Max Value
                max_price = sorted(price_choices.keys())
                max_price.remove('max')
                max_price_val = max(list(map(int, max_price)))
                self.queryset_list = self.queryset_list.filter(price__gte=max_price_val)
                print(max_price_val)
        return self.queryset_list

    def location(self):
        if 'location' in self.request:
            location = self.request['location']
            if location:
                # Check if the search criteria has commas, if so split the string by the commas.
                    
                # (list is reversed as we will be searching in that order (contry -> city -> etc..))
                if ', ' in location:
                    location = location.split(', ')[::-1]
                elif ',' in location:
                    location = location.split(',')[::-1]
                else:
                    location = location.split(' ')[::-1]
                
                for location_field in location:
                    search_end = 0
                    
                    # If user enters UK or similar
                    if location_field.lower() in ['united kingdom', 'uk', 'gb']:
                        pass
                    
                    # Check if user enters England/ Wales/ Scotland/ Northern Ireland/ Ireland-
                    elif location_field.lower() in ['england', 'wales', 'scotland', 'northern ireland', 'ireland']:
                        cities = self.get_city_list(location_field.lower())
                        self.queryset_list = self.queryset_list.filter(city__in=cities)

                    # City
                    elif self.queryset_list.filter(city__icontains=location_field):
                        self.queryset_list = self.queryset_list.filter(city__icontains=location_field.lower())

                    # Postcode
                    elif self.postcode_permutations(location_field) != ['']:
                        postcode_patterns = self.postcode_permutations(location_field)[0]
                        if self.queryset_list.filter(postcode__icontains=postcode_patterns):
                            self.queryset_list = self.queryset_list.filter(postcode__icontains=postcode_patterns)

                    # Address
                    elif self.queryset_list.filter(address__icontains=location_field):
                        self.queryset_list = self.queryset_list(address__icontains=location_field)
                    
                    # Title
                    else:
                        self.queryset_list = self.queryset_list.filter(title__icontains=location_field)
                        
        
        return self.queryset_list

    def get_city_list(self, criteria):
        '''
        This will take a criteria and check if it is a UK country.
        If it is, then it will return all the cities that belong to it.
        '''

        cities = []

        # Ensure that the type is string, if not, try to convert or throw error
        if type(criteria) == str:
            criteria = criteria.lower()
        elif type(criteria) == list and len(criteria) == 1:
            criteria = str(criteria[0]).lower()
        else:
            raise Exception('{} is not a string. Ensure that the criteria is a string.'.format(criteria))

        # England
        if criteria == 'england':
            cities = cities_by_country['England']

        # Wales
        elif criteria == 'wales':
            cities = cities_by_country['Wales']
        
        # Scotland
        elif criteria == 'scotland':
            cities = cities_by_country['Scotland']
        
        # Northen Ireland
        elif criteria == 'northern ireland':
            cities = cities_by_country['Northern Ireland']
        
        # Ireland
        elif criteria == 'ireland':
            cities = cities_by_country['Ireland']

        return cities

    def postcode_permutations(self, postcode_str):
        '''
        Function will take string and return a list of possible strings which may include the postcode in the desired format. 
        '''

        postcode_patterns = ['']
        postcode_str = postcode_str.upper()
        str_spaces = postcode_str.count(' ')
        str_length = len(postcode_str)

        # String has only 1 space
        if str_length <= 8 and str_length >=2 and str_spaces == 1:

            space_index = postcode_str.index(' ')

            # Using he space index and the length of the user input, appy rule to accept only strings which follow the format of a postcode.
            
            # (length, space_index)
            valid_postcode_formats = [(6, 2), (7, 3), (8, 4)]

            if (str_length, space_index) in valid_postcode_formats:
                postcode_patterns = [postcode_str]
            
        elif str_spaces == 0:
            
            # Partial Postcodes
            if str_length == 2:
                if re.search('([A-z][0-9])',postcode_str):
                    postcode_patterns = [postcode_str]
            
            if str_length == 3:
                if re.search('([A-z][0-9][0-9])', postcode_str):
                    postcode_patterns = [postcode_str]

            if str_length == 4:
                if re.search('([A-z][A-z][0-9][0-9])', postcode_str):
                    postcode_patterns = [postcode_str]

            if str_length == 5:
                if re.search('([A-z][0-9][0-9][A-z][A-z])', postcode_str):
                    postcode_patterns = [
                        postcode_str[0:2] + ' ' + postcode_str[2:],
                    ]
            
            elif str_length == 6:
                if re.search('([A-z][A-z|0-9][0-9][0-9][A-z][A-z])', postcode_str):
                    postcode_patterns = [
                        postcode_str[0:3] + ' ' + postcode_str[3:],
                    ]
            
            elif str_length == 7:
                if re.search('([A-z][A-z][0-9][0-9][0-9][A-z][A-z])', postcode_str):
                    postcode_patterns = [
                        postcode_str[0:4] + ' ' + postcode_str[4:],
                    ]
            
        return postcode_patterns
