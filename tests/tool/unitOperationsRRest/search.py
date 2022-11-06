from rest_framework.test import APITestCase


def add_search(self: APITestCase):
    from pullgerReflection.com_linkedin.tests.tools.dataTemplatesR import people_search_data

    psDATA = people_search_data()

    resultGet = self.client.post('/pullgerR/com_linkedin/api/search-requests', psDATA)
    self.assertEqual(resultGet.status_code, 201, "REST error on creating search request")

    response = self.client.get("/pullgerR/com_linkedin/api/search-requests")
    self.assertEqual(response.status_code, 200, "Incorrect get data list search request")

    dataResponse = response.data.get("data")
    self.assertIsNotNone(dataResponse, "Incorrect get response search request")

    self.assertEqual(dataResponse.get('count'), 1, "Incorrect count of search request response")
    self.assertEqual(dataResponse.get('page_current'), 1, "Incorrect page count of search request response")

    dataPosts = dataResponse.get('posts')
    self.assertIsNotNone(dataPosts, "No 'posts' in response")

    self.assertEqual(len(dataPosts), 1, "Incorrect size of list")

    # for key, value in psDATA.items():
    #     self.assertEqual(dataPosts[0].get(key), value, "Incorrect count of response")
