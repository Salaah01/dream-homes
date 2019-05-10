from django.test import SimpleTestCase

from listings.search_tool import SearchListings
# from listings.models import Listing

class GetCityTest(SimpleTestCase):
    '''
    Tests for the method get_city_list
    '''

    def country_cities(self):
        england = [
            'bath',
            'birmingham',
            'bradford',
            'brighton and hove',
            'bristol',
            'cambridge',
            'canterbury',
            'carlisle',
            'chester',
            'chichester',
            'coventry',
            'derby',
            'durham',
            'ely',
            'exeter',
            'gloucester',
            'hereford',
            'kingston upon hull',
            'lancaster',
            'leeds',
            'leicester',
            'lichfield',
            'lincoln',
            'liverpool',
            'city of london',
            'london',
            'manchester',
            'newcastle upon tyne',
            'newcastle',
            'norwich',
            'nottingham',
            'oxford',
            'peterborough',
            'plymouth',
            'portsmouth',
            'preston',
            'ripon',
            'salford',
            'salisbury',
            'sheffield',
            'southampton',
            'st albans',
            'st. albans',
            'stoke-on-trent',
            'stoke on trent',
            'sunderland',
            'truro',
            'wakefield',
            'wells',
            'westminster',
            'winchester',
            'wolverhampton',
            'worcester',
            'york',
        ]
        wales = [
            'bangor',
            'cardiff',
            'newport',
            'st davids',
            'swansea',
        ]
        scotland = [
            'aberdeen',
            'dundee',
            'edinburgh',
            'glasgow',
            'inverness',
            'stirling',
        ]
        northern_ireland = [
            'aberdeen',
            'dundee',
            'edinburgh',
            'glasgow',
            'inverness',
            'stirling',
        ]
        ireland = [
            'cork',
            'waterford',
            'kilkenny',
            'limerick',
            'galway',
            'dublin',
            'armagh',
            'belfast',
            'londonderry',
            'derry',
            'lisburn',
            'newry',
        ]

        country_cities = {
            'england': england,
            'wales': wales,
            'scotland': scotland,
            'northern ireland': northern_ireland,
            'ireland': ireland
        }

        return country_cities                    
    
    def test_england_cities(self):
        '''
        Test to check that if "england" is passed through the function get_city_list that it returns all cities in England
        '''
        cities = SearchListings().get_city_list('england')
        self.assertEqual (self.country_cities()['england'], cities)

    def test_wales_cities(self):
        '''
        Test to check that if "wales" is passed through the function get_city_list that it returns all cities in England
        '''
        cities = SearchListings().get_city_list('wales')
        self.assertEqual(self.country_cities()['wales'], cities)
    
    def test_scotland_cities(self):
        '''
        Test to check that if "scotland" is passed through the function get_city_list that it returns all cities in Scotland
        '''
        cities = SearchListings().get_city_list('scotland')
        self.assertEqual(self.country_cities()['scotland'], cities)

    def test_northern_ireland_cities(self):
        '''
        Test to check that if "northern ireland" is passed through the function get_city_list that it returns all cities in Northern Ireland
        '''
        cities = SearchListings().get_city_list('northern ireland')
        self.assertEqual(self.country_cities()['northern ireland'], cities)

    def test_ireland_cities(self):
        '''
        Test to check that if "ireland" is passed through the function get_city_list that it returns all cities in Ireland
        '''
        cities = SearchListings().get_city_list('ireland')
        self.assertEqual(self.country_cities()['ireland'], cities) 

class PostcodePermutations(SimpleTestCase):
    '''
    Tests for function postcode_permutations
    '''

    # --------------------------------------------------------------------
    # Minimum / Maximum Length Tests + <1 Space Test
    # --------------------------------------------------------------------

    def test_string_too_short(self):
        '''
        A string where the length is less than 5 should return ['']
        '''
        postcode_patterns = SearchListings().postcode_permutations('a')
        self.assertEqual(postcode_patterns, [''])

    def test_string_too_long(self):
        '''
        A string where the length is greater than 8 should return ['']
        '''
        postcode_patterns = SearchListings().postcode_permutations('abcdefghi')
        self.assertEqual(postcode_patterns, [''])

    def test_mutliple_spaces(self):
        '''
        A string with multiple spaces should return ['']
        '''
        postcode_patterns = SearchListings().postcode_permutations('a c de')
        self.assertEqual(postcode_patterns, [''])

    # --------------------------------------------------------------------
    # Tests for Strings with 1 Space
    # --------------------------------------------------------------------

    def test_1_space_len_6_valid(self):
        '''
        A string in the correct postcode format of length 6 which has 1 space should return itself in a list.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e1 5bb')
        self.assertEqual(postcode_patterns, ['E1 5BB'])
    
    def test_1_space_len_6_invalid(self):
        '''
        A string in the wrong postcode format of length 6 which has 1 space should return [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('e15 bb')
        self.assertEqual(postcode_patterns, [''])

    def test_1_space_len_7_valid(self):
        '''
        A string in the correct postcode format of length 7 which has 1 space should return itself in a list.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e11 5bb')
        self.assertEqual(postcode_patterns, ['E11 5BB'])
    
    def test_1_space_len_7_invalid(self):
        '''
        A string in the wrong postcode format of length 7 which has 1 space should return [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('ew15 bb')
        self.assertEqual(postcode_patterns, [''])

    def test_1_space_len_8_valid(self):
        '''
        A string in the correct postcode format of length 8 which has 1 space should return itself in a list.
        '''
        postcode_patterns = SearchListings().postcode_permutations('sw11 5bb')
        self.assertEqual(postcode_patterns, ['SW11 5BB'])
    
    def test_1_space_len_8_invalid(self):
        '''
        A string in the wrong postcode format of length 8 which has 1 space should return [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('sw1 11bb')
        self.assertEqual(postcode_patterns, [''])

    # --------------------------------------------------------------------
    # Tests for Strings with 0 Space
    # --------------------------------------------------------------------

    def test_no_space_len2_valid(self):
        '''
        A valid string of length 2 with no spaces should return the list of postcode patterns.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e1')
        self.assertEqual(postcode_patterns, ['E1'])

    def test_no_space_len2_invalid(self):
        '''
        An invalid string of length 2 with no spaces should [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('ee')
        self.assertEqual(postcode_patterns, [''])

    def test_no_space_len3_valid(self):
        '''
        A valid string of length 3 with no spaces should return the list of postcode patterns.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e11')
        self.assertEqual(postcode_patterns, ['E11'])

    def test_no_space_len3_invalid(self):
        '''
        An invalid string of length 3 with no spaces should [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('ee1')
        self.assertEqual(postcode_patterns, [''])

    def test_no_space_len4_valid(self):
        '''
        A valid string of length 4 with no spaces should return the list of postcode patterns.
        '''
        postcode_patterns = SearchListings().postcode_permutations('se11')
        self.assertEqual(postcode_patterns, ['SE11'])

    def test_no_space_len3_invalid(self):
        '''
        An invalid string of length 4 with no spaces should [''].
        '''
        postcode_patterns = SearchListings().postcode_permutations('e1e1')
        self.assertEqual(postcode_patterns, [''])

    def test_no_space_len5_valid(self):
        '''
        A valid string of length 5 with no spaces should return the list of postcode patterns.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e15bb')
        self.assertEqual(postcode_patterns, ['E1 5BB'])

    def test_no_space_len5_invalid(self):
        postcode_patterns = SearchListings().postcode_permutations('e155b')
        self.assertEqual(postcode_patterns, [''])

    def test_no_space_len6_ssiiss_valid(self):
        '''
        A valid string of length 6 with no spaces should return the list of postcode patterns.
        The string is in the format ssiiss where s is a letter and i is a digit.
        '''
        postcode_patterns = SearchListings().postcode_permutations('sw15bb')
        self.assertEqual(postcode_patterns, ['SW1 5BB'])

    def test_no_space_len6_siiiss_valid(self):
        '''
        A valid string of length 6 with no spaces should return the list of postcode patterns.
        The string is in the format siiiss where s is a letter and i is a digit.
        '''
        postcode_patterns = SearchListings().postcode_permutations('e145bb')
        self.assertEqual(postcode_patterns, ['E14 5BB'])
    
    def test_no_space_len6_invalid(self):
        postcode_patterns = SearchListings().postcode_permutations('e145b8')
        self.assertEqual(postcode_patterns, [''])

    def test_no_space_len7_valid(self):
        '''
        A valid string of length 7 with no spaces should return the list of postcode patterns.
        '''
        postcode_patterns = SearchListings().postcode_permutations('sw115bb')
        self.assertEqual(postcode_patterns, ['SW11 5BB'])

    def test_no_space_len5_invalid(self):
        postcode_patterns = SearchListings().postcode_permutations('1e140bb')
        self.assertEqual(postcode_patterns, [''])
