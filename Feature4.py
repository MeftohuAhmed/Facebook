class request_limiter:
    '''
    This class is responsible for limiting the number of requests. It allows a request to be printed only if the request
    has not been made in the last 5 seconds. Otherwise, it rejects the request.
    '''
    def __init__(self):
        self.requests = {}

    def request_approver(self, timestamp, request):
        '''
        This method checks if a request can be approved based on the timestamp and the request itself.

        :param timestamp: The time at which the request is made. It is an integer representing the seconds.
        :param request: The request that needs to be approved. It is a string representing the request.
        :return: Returns True if the request can be approved i.e., if the same request has not been made in the last 5 seconds. Otherwise, it returns False.
        '''

        if request not in self.requests or timestamp - self.requests[request] >= 5:
            self.requests[request] = timestamp
            print("Request Accepted")
            return True
        else:
            print("Request Rejected")
            return False

# Driver code
import unittest
from Feature4 import request_limiter

class TestRequestLimiter(unittest.TestCase):
    def setUp(self):
        '''
        This method is run before each test. It creates an instance of the request_limiter class.
        '''
        self.obj = request_limiter()

    def test_request_accepted(self):
        '''
        This method tests the cases where the requests should be accepted.
        It asserts that the request_approver method returns True for these cases.
        '''
        self.assertTrue(self.obj.request_approver(1, "send_message"))
        self.assertTrue(self.obj.request_approver(2, "block"))
        self.assertTrue(self.obj.request_approver(8, "send_message"))
        self.assertTrue(self.obj.request_approver(10, "block"))

    def test_request_rejected(self):
        '''
        This method tests the cases where the requests should be rejected.
        It asserts that the request_approver method returns False for these cases.
        '''
        self.assertTrue(self.obj.request_approver(1, "send_message"))
        self.assertFalse(self.obj.request_approver(3, "send_message"))
        self.assertTrue(self.obj.request_approver(2, "block"))
        self.assertFalse(self.obj.request_approver(4, "block"))