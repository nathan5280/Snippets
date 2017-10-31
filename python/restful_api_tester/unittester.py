import unittest
from requests import get, put, post

class RESTfulAPITest(unittest.TestCase):
    ip = 'ec2-54-89-76-249.compute-1.amazonaws.com:1717'
    def test_get(self):
        response = get("http://{ip}/addresses".format(ip=self.ip)).json()
        print(response)



if __name__ == '__main__':
    unittest.main()