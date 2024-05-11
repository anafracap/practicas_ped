import unittest
from unittest.mock import call, patch, MagicMock
from servidor import ChatServer

class TestClass(unittest.TestCase):
    def setUp(self):
        self.chat_server = ChatServer("0.0.0.0", 1234)
        self.chat_server.chats = {
            'ana': 'all',
            'raquel': 'all',
            'ivan': 'all'
        }
        self.chat_server.groups['all'].add('ana')
        self.chat_server.groups['all'].add('raquel')
        self.chat_server.groups['all'].add('ivan')
        
    def tearDown(self):
        self.chat_server.chats = {}
        self.chat_server.groups = {'all': set()}

    def test_continue_conversation_exit(self):
        message = "exit"
        nick = 'ana'
        with patch.object(self.chat_server, 'disconnect') as mock_disconnect:
            self.chat_server.continue_conversation(message, nick)
            mock_disconnect.assert_called_once_with(nick)

    def test_continue_conversation_groups(self):
        message = 'group: hola'
        nick = 'ana'
        with patch.object(self.chat_server, 'send_to_one') as mock_send_one:
            self.chat_server.continue_conversation(message, nick)
            expected_calls = [
                call('ana has left the chat!', 'ana'),
                call('ana has left the chat!', 'raquel'),
                call('ana has left the chat!', 'ivan'),
                call('You have joined the group hola.\n', 'ana'),
                call('ana has joined the chat!', 'ana')]
            mock_send_one.assset_has_calls(expected_calls)
    
    def test_continue_conversation_private(self):
        message = 'private: raquel'
        nick = 'ana'
        with patch.object(self.chat_server, 'send_to_one') as mock_send_one:
            self.chat_server.continue_conversation(message, nick)
            expected_calls = [
                call('ana has left the chat!', 'ana'),
                call('ana has left the chat!', 'raquel'),
                call('ana has left the chat!', 'ivan'),
                call('You have joined private chat with raquel.\n', 'ana'),
                call('ana has joined a private chat with you!', 'raquel')]
            mock_send_one.assset_has_calls(expected_calls)

    def test_continue_conversation_regular_all(self):
        message = 'holaaa'
        nick = 'ana'
        response = 'ana: holaaa'
        with patch.object(self.chat_server, 'send_to_one') as mock_send_one:
            self.chat_server.continue_conversation(message, nick)
            expected_calls = [
                call(response, 'ana'),
                call(response, 'raquel'),
                call(response, 'ivan')]
            mock_send_one.assset_has_calls(expected_calls)
    
    def test_continue_conversation_regular_group_convo(self):
        message = 'group: hola'
        nick = 'ana'
        with patch.object(self.chat_server, 'send_to_one') as mock_send_one:
            self.chat_server.continue_conversation(message, nick)
        new_message = 'holaaa'
        response = 'ana: holaaa'
        with patch.object(self.chat_server, 'send_to_one') as mock_send_one:
            self.chat_server.continue_conversation(new_message, nick)
            expected_calls = [
                call(response, 'ana')]
            mock_send_one.assset_has_calls(expected_calls)


if __name__ == '__main__':
    unittest.main()