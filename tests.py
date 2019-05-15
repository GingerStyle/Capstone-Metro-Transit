"""This class holds all the tests to test the API_Manager requests, and request processing"""

import API_Manager
import unittest

class TestAPIPRocessing(unittest.TestCase):

    def test_get_routes_response_processing(self):
        """Test that the API_Manager.get_routes response is processed into a list of route numbers correctly"""

        example_response = [
            { "Route": "4", "sdfdgsg": "Sdfsdfsf"},
            { "Route": "40", "asduhsdif": "Sdfsdfsf"},
            { "Route": "B", "sdfijsdfoij": "Sdfsdfsf"},
        ]

        route_numbers = API_Manager.route_numbers_from_response(example_response)
        self.assertEqual(['4', '40', 'B'], route_numbers)


    def test_get_directions_response_processing(self):
        """Testing that the API_Manager.get_directions processes the directions into a list correctly"""

        example_response = [{"Text": "NORTHBOUND", "Value": "4"},
                            {"Text": "SOUTHBOUND", "Value": "1"}]

        directions = API_Manager.directions_from_response(example_response)
        self.assertEqual(['NORTHBOUND', 'SOUTHBOUND'], directions)


    def test_get_Stops_response_processing(self):
        """Testing that the API_Manager.get_stops processes the stop information into a dictionary"""

        example_response = [{"Text":"Mall of America Transit Station","Value":"MAAM"},
                            {"Text":"Portland Ave and 77th St","Value":"77PO"},
                            {"Text":"Portland Ave and 66th St","Value":"66PO"}]

        stop_dict = API_Manager.stops_from_response(example_response)
        self.assertEqual({"Mall of America Transit Station": "MAAM",
                          "Portland Ave and 77th St": "77PO",
                          "Portland Ave and 66th St": "66PO"}, stop_dict)


    def test_get_times_response_processing(self):
        """Testing the API_Manager.get_times processes the times into a list"""

        example_response = [{"BlockNumber":1058,"DepartureText":"3 Min","DepartureTime":"\/Date(1557603720000-0500)\/","Route":"5","RouteDirection":"NORTHBOUND"},
                            {"BlockNumber":1053,"DepartureText":"8 Min","DepartureTime":"\/Date(1557604020000-0500)\/","Route":"5","RouteDirection":"NORTHBOUND"},
                            {"BlockNumber":1055,"DepartureText":"2:59","DepartureTime":"\/Date(1557604740000-0500)\/","Route":"5","RouteDirection":"NORTHBOUND"}
                            ]

        times = API_Manager.times_from_response(example_response)
        self.assertEqual(['3 Min', '8 Min', '2:59'], times)


    def test_build_marker_list_processing(self):
        """Testing API_Manager.build_marker_list for proper string concatenation"""

        example_list = ['Apple Valley', 'Minneapolis']

        list = API_Manager.build_marker_list(example_list)
        self.assertEqual(['size:small|color:red|Apple Valley', 'size:small|color:red|Minneapolis'], list)


    def test_build_visible_list_processing(self):
        """Testing API_Manager.build_visible_list for proper list conversion"""

        example_list = ['Apple Valley', 'Bloomington', 'St. Paul', 'Minneapolis']

        list = API_Manager.build_visible_list(example_list)
        self.assertEqual(['Apple Valley', 'Minneapolis'], list)


    def test_convert_to_direction_code(self):
        """Test that convert_to_direction_code returns the correct code"""

        direction = 'NORTHBOUND'
        code = API_Manager.convert_to_direction_code(direction)
        self.assertEqual('4', code)

        direction = 'SOUTHBOUND'
        code = API_Manager.convert_to_direction_code(direction)
        self.assertEqual('1', code)

        direction = 'EASTBOUND'
        code = API_Manager.convert_to_direction_code(direction)
        self.assertEqual('2', code)

        direction = 'WESTBOUND'
        code = API_Manager.convert_to_direction_code(direction)
        self.assertEqual('3', code)



if __name__ == '__main__':
    unittest.main()