from pullgerAuthJWT.tests import unit as unitAuthJWT
from rest_framework.test import APITestCase


def setUpUnit(self: APITestCase):
    unitAuthJWT.UnitOperations.CreateUser(self)
    unitAuthJWT.UnitOperations.GetToken(self)
    self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)


def createPeople(self: APITestCase):
    from pullgerReflection.com_linkedin.tests.dataTemplate import person_DATA

    pDATA = person_DATA()

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


def send_all_task_to_processing(self: APITestCase):
    resultGet = self.client.post("/pullgerR/com_linkedin/api/threadtask/sendAllTaskForProcessing")
    self.assertEqual(resultGet.status_code, 200, "Error on sent task for processing")