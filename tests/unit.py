from rest_framework.test import APITestCase
from .tool import unitOperationsRRest


class Test_000_Smoke(APITestCase):
    def setUp(self):
        unitOperationsRRest.setUpUnit(self)

    def test_001_0_0_Ping(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        resultGet = self.client.get("/pullgerR/com_linkedin/api/ping/")

        self.assertEqual(resultGet.status_code, 200, "General REST API Critical error.")

    def test_002_0_0_ThreadPing(self):
        resultGet = self.client.get("/pullgerR/com_linkedin/api/threadtask/ping")
        self.assertEqual(resultGet.status_code, 200, "General Thread REST API Critical error.")

    def test_003_0_0_People(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

        unitOperationsRRest.createPeople(self)

    def test_004_0_0_SendTaskToProcessing(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

        unitOperationsRRest.createPeople(self)
        unitOperationsRRest.send_all_task_to_processing(self)