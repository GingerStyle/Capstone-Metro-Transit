import API_Manager 
import unittest

class TestAPIPRocessing(unittest.TestCase):
    def test_get_routes_response_processing(self):
        example_response = [
            { "Route": "4", "sdfdgsg": "Sdfsdfsf"},
            { "Route": "40", "asduhsdif": "Sdfsdfsf"},
            { "Route": "B", "sdfijsdfoij": "Sdfsdfsf"},
        ]

        route_numbers = API_Manager.route_numbers_from_response(example_response)
        self.assertEqual(['4', '40', 'B'], route_numbers)