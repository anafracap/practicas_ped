import unittest
from unittest.mock import patch, MagicMock
from servidor import ChatServer

class TestClass(unittest.TestCase):
    def setUp(self):
        self.chat_server = ChatServer("0.0.0.0", 1234)

    def test_continue_conversation_exit(self):
        message = "exit"
        nick = 'ana'
        with patch.object(self.chat_server, 'disconnect') as mock_disconnect:
            self.chat_server.continue_conversation(message, nick)
            mock_disconnect.assert_called_once_with(nick)

if __name__ == '__main__':
    unittest.main()