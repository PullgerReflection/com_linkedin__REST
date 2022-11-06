from rest_framework.test import APITestCase
from pullgerReflection.com_linkedin.tests.tools import dataTemplatesR


def add_location(self: APITestCase):

    location_data = dataTemplatesR.location_data()

    for cur_location in location_data:
        resultGet = self.client.post('/pullgerR/com_linkedin/api/location', cur_location)
        self.assertEqual(resultGet.status_code, 201, "REST error on creating 'location'")

    response = self.client.get("/pullgerR/com_linkedin/api/location")
    self.assertEqual(response.status_code, 200, "Incorrect get data list 'location'")

    dataResponse = response.data.get("data")
    self.assertIsNotNone(dataResponse, "Incorrect get response 'location'")

    self.assertEqual(dataResponse.get('count'), len(location_data), "Incorrect count of 'location' response")
    self.assertEqual(dataResponse.get('page_current'), 1, "Incorrect page count of 'location' response")

    dataPosts = dataResponse.get('posts')
    self.assertIsNotNone(dataPosts, "No posts of 'location' in response")

    self.assertEqual(len(dataPosts), len(location_data), "Incorrect size of list")

    # for cur_location in location_data:
    #     for key, value in cur_location.items():
    #         self.assertEqual(dataPosts[0].get(key), value, "Incorrect count of response")
