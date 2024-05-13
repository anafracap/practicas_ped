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
        self.chat_server.clients = {
            'ana': '',
            'raquel': '',
            'ivan': ''
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
        contain = False
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

    def test_enter_group_changed_chats (self):
        message = 'group: hola'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        chats = {
            'ana': 'ghola',
            'raquel': 'gall',
            'ivan': 'gall'
        }
        self.assertEqual(self.chat_server.chats, chats)

    def test_enter_group_left_chat(self):
        message = 'group: hola'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'ana has left the chat!\n'
        contain = []
        nicks = ['ana', 'raquel', 'ivan']
        for nick in nicks:
            if expected in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True, True])
    
    def test_enter_group_joined_chat(self):
        message = 'group: hola'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'ana has joined the chat!\n'
        contain = False
        if expected in result.get(nick, []):
            contain = True
        self.assertTrue(contain)
    
    def test_enter_group_no_joined_chat(self):
        message = 'group: hola'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'ana has joined the chat!\n'
        nicks = ['raquel', 'ivan']
        contain = []
        for nick in nicks:
            if expected not in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True])

    def test_enter_private(self):
        message = 'private: raquel'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'You have joined a private chat with raquel.\n'
        contain = False
        if expected in result.get(nick, []):
            contain = True
        self.assertTrue(contain)
    
    def test_enter_private_changed_group (self):
        message = 'private: raquel'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        groups = {'all': set()}
        groups['all'].add('raquel')
        groups['all'].add('ivan')
        self.assertEqual(self.chat_server.groups, groups)

    def test_enter_private_changed_chats (self):
        message = 'private: raquel'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        chats = {
            'ana': 'praquel',
            'raquel': 'gall',
            'ivan': 'gall'
        }
        self.assertEqual(self.chat_server.chats, chats)

    def test_enter_private_left_chat(self):
        message = 'private: raquel'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = f'{nick} has left the chat!\n'
        contain = []
        nicks = ['ana', 'raquel', 'ivan']
        for nick in nicks:
            if expected in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True, True])
    
    def test_enter_private_joined_chat(self):
        message = 'private: raquel'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = 'You have joined a private chat with raquel.\n'
        contain = False
        if expected in result.get(nick, []):
            contain = True
        self.assertTrue(contain)
    
    def test_enter_private_no_joined_chat(self):
        message = 'private: raquel'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = '{nick} has joined a private chat with you.\n'
        nicks = ['ana', 'ivan']
        contain = []
        for nick in nicks:
            if expected not in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True])

    def test_send_message_all(self):
        message = 'hola'
        nick = 'ana'
        result = self.chat_server.treat_message(message, nick)
        expected = f"{nick}: {message}"
        contain = []
        nicks = ['ana', 'raquel', 'ivan']
        for nick in nicks:
            if expected in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True, True])
    
    def test_send_message_group(self):
        message = 'group: hola'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        message = 'hola'
        result = self.chat_server.treat_message(message, nick)
        expected = f"{nick}: {message}"
        contain = False
        if expected in result.get(nick, []):
            contain = True
        self.assertTrue(contain)
    
    def test_send_message_group_not_others(self):
        message = 'group: hola'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        message = 'hola'
        result = self.chat_server.treat_message(message, nick)
        expected = f"{nick}: {message}"
        nicks = ['raquel', 'ivan']
        contain = []
        for nick in nicks:
            if expected not in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True])
    
    def test_send_message_private(self):
        message = 'private: raquel'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        message = 'holi'
        result = self.chat_server.treat_message(message, nick)
        expected = f"{nick}: {message}"
        contain = False
        if expected in result.get('raquel', []):
            contain = True
        self.assertTrue(contain)
    
    def test_send_message_private_not_others(self):
        message = 'private: raquel'
        nick = 'ana'
        self.chat_server.treat_message(message, nick)
        message = 'hola'
        result = self.chat_server.treat_message(message, nick)
        expected = f"{nick}: {message}"
        nicks = ['ana', 'ivan']
        contain = []
        for nick in nicks:
            if expected not in result.get(nick, []):
                contain.append(True)
        self.assertEqual(contain, [True, True])



if __name__ == '__main__':
    unittest.main()