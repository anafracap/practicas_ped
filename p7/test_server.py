import unittest
from unittest.mock import call, patch, MagicMock
from servidor import ChatServer

class TestClass(unittest.TestCase):
    def setUp(self):
        self.chat_server = ChatServer("0.0.0.0", 1234)
        self.chat_server.chats = {
            'ana': 'gall',
            'raquel': 'gall',
            'ivan': 'gall'
        }
        self.chat_server.groups['all'].add('ana')
        self.chat_server.groups['all'].add('raquel')
        self.chat_server.groups['all'].add('ivan')
        
    def tearDown(self):
        self.chat_server.chats = {}
        self.chat_server.groups = {'all': set()}

    def test_enter_group(self):
        message = 'group: hola'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'You have joined the group hola.\n'
        if expected in result.get(nick, []):
            contain = True
        self.assertTrue(contain)
    
    def test_enter_group_changed_group (self):
        message = 'group: hola'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        groups = {'all': set(),
                  'hola': set()}
        groups['hola'].add('ana')
        groups['all'].add('raquel')
        groups['all'].add('ivan')
        self.assertEqual(self.chat_server.groups, groups)


if __name__ == '__main__':
    unittest.main()