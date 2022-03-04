import threading
import unittest
from unittest import mock
from unittest.mock import patch, Mock

from Client import Client
from Server import Server


def create_server():
    Server()


class test_client(unittest.TestCase):
    def test_port(self):
        # creating a server to connect to
        t1 = threading.Thread(target=create_server)
        t1.daemon = True
        t1.start()
        with mock.patch('builtins.input', side_effect=['55001', 'amit', 2]):
            client = Client()
