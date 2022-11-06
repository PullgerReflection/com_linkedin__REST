from rest_framework.test import APITestCase


def create_people(self: APITestCase):
    from pullgerReflection.com_linkedin.tests.tools.DataTemplate import person_data

    pDATA = person_data()

    resultGet = self.client.post('/pullgerR/com_linkedin/api/people', pDATA)
    self.assertEqual(resultGet.status_code, 201, "REST error on creating people")

    response = self.client.get("/pullgerR/com_linkedin/api/people")
    self.assertEqual(response.status_code, 200, "Incorrect get data")

    dataResponse = response.data.get("data")
    self.assertIsNotNone(dataResponse, "Incorrect get response")

    self.assertEqual(dataResponse.get('count'), 1, "Incorrect count of response")
    self.assertEqual(dataResponse.get('page_current'), 1, "Incorrect page count of response")

    dataPosts = dataResponse.get('posts')
    self.assertIsNotNone(dataPosts, "No 'posts' in response")

    self.assertEqual(len(dataPosts), 1, "Incorrect size of list")

    for key, value in pDATA.items():
        self.assertEqual(dataPosts[0].get(key), value, "Incorrect count of response")
