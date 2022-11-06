from rest_framework.test import APITestCase
from pullgerAuthJWT.tests import unit as unitAuthJWT


def set_up_unit(self: APITestCase):
    unitAuthJWT.UnitOperations.CreateUser(self)
    unitAuthJWT.UnitOperations.GetToken(self)
    self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)


def send_all_task_to_processing(self: APITestCase):
    resultGet = self.client.post("/pullgerR/com_linkedin/api/thread-task/send-all-task-for-processing")
    self.assertEqual(resultGet.status_code, 200, "Error on sent task for processing")
