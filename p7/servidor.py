import sys, socket, select

class ChatServer:

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.server_socket.listen()
        print(self.server_socket, file=sys.stderr)

        try: 
            while True:
                file_inputs = [self.server_socket, sys.stdin]
                file_inputs.extend(list(self.clients.values()))
                file_inputs.extend(self.pending)
                readable, _, _ = select.select(file_inputs, [], [])

                for trigger_socket in readable:
                    if trigger_socket == self.server_socket:
                        client_socket, client_address = self.server_socket.accept()
                        identify = "Please enter your UNIQUE nickname: "
                        try:
                            client_socket.send(identify.encode('utf-8'))
                            self.pending.append(client_socket)
                        except BrokenPipeError:
                            client_socket.close()
                    elif trigger_socket == sys.stdin:
                        message = input()
                        if message.lower() == 'exit':
                            self.shutdown()
                            return
                    elif trigger_socket in self.pending:
                        nick, result = self.verify_nick(client_socket)
                        if result:
                            self.send_messages(result)
                        if nick:
                            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}", file=sys.stderr)
                    else: # Receive message from existing client
                        nick = [key for key, value in self.clients.items() if value == trigger_socket][0]
                        try:
                            message = trigger_socket.recv(1024).decode('utf-8')
                            if message:
                                result = self.process_chat_message(message, nick)
                                if result:
                                    self.send_messages(result)
                            else:  # Client disconnected
                                self.disconnect(nick)
                        except (ConnectionResetError, BrokenPipeError):
                            self.disconnect(nick)
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Exiting server.", file=sys.stderr)
        finally:
            self.shutdown()
            

    def verify_nick(self, cli_sock):
        self.pending.remove(cli_sock)
        result = {}
        nick = cli_sock.recv(1024).decode('utf-8')
        if nick in self.clients:
            message = "Your nickname is already in use, unable to log in \n"
            cli_sock.send(message.encode('utf-8'))
            cli_sock.close()
            return False, False
        else:
            self.clients[nick] = cli_sock
            print(list(self.clients), file=sys.stderr)
            login = "You have successfully logged in! Type 'exit' to leave the chat.\n"
            result.update(self.add_message_to_dict(result, login, nick))
            self.chats[nick] = 'gall'
            self.groups['all'].add(nick)
            text = f"{nick} has joined the chat!"
            self.prepare_for_chat(result, text, nick)
            return nick, result

    def process_chat_message(self, message, nick):
        result = {}
        if message.lower().startswith("group: "):
            group = message[len("group: "):]
            result.update(self.leave_old_chat(result, nick))
            self.chats[nick] = 'g' + group
            if not group in self.groups:
                self.groups[group] = set()
            self.groups[group].add(nick)
            you_joined = f"You have joined the group {group}.\n"
            result.update(self.add_message_to_dict(result, you_joined, nick))
            joined = f"{nick} has joined the chat!\n"
            result.update(self.prepare_for_chat(result, joined, nick))
            return result
        elif message.lower().startswith("private: "):
            private = message[len("private: "):]
            result.update(self.leave_old_chat(result, nick))
            self.chats[nick] = 'p' + private
            you_joined = f"You have joined a private chat with {private}.\n"
            result.update(self.add_message_to_dict(result, you_joined, nick))
            joined = f"{nick} has joined a private chat with you.\n"
            result.update(self.prepare_for_chat(result, joined, nick))
            return result
        elif message.lower() == 'exit':
            self.disconnect(nick)
        else:
            text = f"{nick}: {message}"
            result.update(self.prepare_for_chat(result, text, nick))
            return result

    def prepare_for_chat(self, result, message, nick):
        chat = self.chats[nick][len('p'):]
        if self.chats[nick].lower().startswith('g'):
            for client in self.groups[chat]:
                result.update(self.add_message_to_dict(result, message, client))
        elif self.chats[nick].lower().startswith('p'):
            if chat in self.clients:
                result.update(self.add_message_to_dict(result, message, chat))
        return result
    
    def leave_old_chat(self, result, nick):
        old = self.chats[nick][len('g'):]
        left = f"{nick} has left the chat!\n"
        result.update(self.prepare_for_chat(result, left, nick))
        if old in self.groups:
            self.groups[old].remove(nick)
        return result

    def add_message_to_dict(self, result, message, nick):
        if nick in result:
            result[nick].append(message)
        else:
            result[nick] = [message]
        return result
    
    def disconnect(self, nick):
        if nick in self.clients:
            old = self.chats[nick][len('g'):]
            text = f"{nick} has left the chat! \n"
            self.send_to_chat(text, nick)
            if old in self.groups:
                self.groups[old].remove(nick)
            message = 'exit'
            self.send_to_one(message, nick)
            self.clients[nick].close()
            del self.chats[nick]
            del self.clients[nick]

    def send_messages(self, result):
        for nick in result:
            if nick in self.clients:
                for message in result.get(nick, []):
                    self.send_to_one(message, nick)

    def send_to_one(self, message, nick):
        if nick in self.clients:
            self.clients[nick].send(message.encode('utf-8'))

    def send_to_chat(self, message, nick):
        chat = self.chats[nick][len('p'):]
        if self.chats[nick].lower().startswith('g'):
            for client in self.groups[chat]:
                self.send_to_one(message, client)
        elif self.chats[nick].lower().startswith('p'):
            if chat in self.clients:
                self.send_to_one(message, chat)

    def shutdown(self):
        for nick in self.clients.copy():
            self.disconnect(nick)
            self.server_socket.close()

    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.server_socket = None
        self.clients = {}
        self.chats = {}
        self.groups = {'all': set()}
        self.pending = []


if __name__ == "__main__":
    server_address = "0.0.0.0"
    server_port = int(sys.argv[1])
    chat_server = ChatServer(server_address, server_port)
    chat_server.start()