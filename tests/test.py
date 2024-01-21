import sys
import unittest

sys.path.append("../the_weather")
from the_weather import *

class WeatherTest(unittest.TestCase):
    
    def test_init(self):
        weather = Weather(22025)
        self.assertEqual(weather.res.status_code, 200)

    def test_invalid_measure(self):
        with self.assertRaises(TypeError):
            Weather(22801, "invalid")

    def test_metric_measure(self):
        weather = Weather(22801, "metric")
        self.assertEqual(weather.res.status_code, 200)

    def test_imperial_measure(self):
        weather = Weather(22801, "imperial")
        self.assertEqual(weather.res.status_code, 200)

if __name__ == '__main__':
    unittest.main()