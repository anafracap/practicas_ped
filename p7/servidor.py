import os, sys, socket, select

class ChatServer:

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.server_socket.listen()
        print(self.server_socket, file=sys.stderr)

        try: 
            while True:
                readable, _, _ = select.select([self.server_socket, sys.stdin] + list(self.clients.values()), [], [])

                for trigger_socket in readable:
                    if trigger_socket == self.server_socket:
                        client_socket, client_address = self.server_socket.accept()
                        identify = "Please enter your UNIQUE nickname: "
                        client_socket.send(identify.encode('utf-8'))
                    elif trigger_socket == sys.stdin:
                        message = input()
                        if message.lower() == 'exit':
                            self.shutdown()
                            return
                    else: # Receive message from existing client
                        nick = [key for key, value in self.clients.items() if value == trigger_socket][0]
                        if not nick:
                            nick = self.verify_nick(client_socket)
                            if nick:
                                print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}", file=sys.stderr)
                        message = trigger_socket.recv(1024).decode('utf-8')
                        self.treat_message(message, nick)
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Exiting server.", file=sys.stderr)
        finally:
            self.shutdown()
            

    def verify_nick(self, cli_sock):
        nick = cli_sock.recv(1024).decode('utf-8')
        if nick in self.clients:
            message = "Your nickname is already in use, unable to log in \n"
            cli_sock.send(message.encode('utf-8'))
            cli_sock.close()
            return False
        else:
            self.clients[nick] = cli_sock
            print(list(self.clients), file=sys.stderr)
            login = "You have successfully logged in! Type 'exit' to leave the chat.\n"
            self.send_to_one(login, nick)
            self.chats[nick] = 'gall'
            self.groups['all'].add(nick)
            text = f"{nick} has joined the chat!"
            self.send_to_chat(text, nick)
            return nick

    def continue_conversation(self, message, nick):
        if message.lower() == 'exit':
            self.disconnect(nick)
        elif message.lower().startswith("group: "):
            text = f"{nick} has left the chat!"
            self.send_to_chat(text, nick)
            group = message[len("group: "):]
            old = self.chats[nick][len('p'):]
            
            if old in self.groups:
                self.groups[old].remove(nick)

            self.chats[nick] = 'g' + group
            if not group in self.groups:
                self.groups[group] = set()
            self.groups[group].add(nick)
            message = f"You have joined the group {group}.\n"
            self.send_to_one(message, nick)
            text = f"{nick} has joined the chat!"
            self.send_to_chat(text, nick)

        elif message.lower().startswith("private: "):
            text = f"{nick} has left the chat!"
            self.send_to_chat(text, nick)

            private = message[len("private: "):]
            old = self.chats[nick][len('g'):]
            if old in self.groups:
                self.groups[old].remove(nick)

            self.chats[nick] = 'p' + private
            message = f"You have joined a private chat with {private}.\n"
            self.send_to_one(message, nick)
            text = f"{nick} has joined a private chat with you.\n"
            self.send_to_chat(text, nick)
        else:
            text = f"{nick}: {message}"
            self.send_to_chat(text, nick)

    def treat_message(self, message, nick):
        if message.lower().startswith("group: "):
            group = message[len("group: "):]
            old = self.chats[nick][len('g'):]
            print(old)
            if old in self.groups:
                self.groups[old].remove(nick)
            self.chats[nick] = 'g' + group
            if not group in self.groups:
                self.groups[group] = set()
            self.groups[group].add(nick)
            message = f"You have joined the group {group}.\n"
            result = {}
            result[nick] = [message]
            return result


    def disconnect(self, nick):
        if nick in self.clients:
            old = self.chats[nick][len('g'):]
            text = f"{nick} has left the chat! \n"
            self.send_to_chat(text, nick)
            message = 'exit'
            self.send_to_one(message, nick)
            self.clients[nick].close()
            if old in self.groups:
                self.groups[old].remove(nick)
            del self.chats[nick]
            del self.clients[nick]

    def send_to_chat(self, message, nick):
        chat = self.chats[nick][len('p'):]
        if self.chats[nick].lower().startswith('g'):
            for client in self.groups[chat]:
                self.send_to_one(message, client)
        elif self.chats[nick].lower().startswith('p'):
            if chat in self.clients:
                self.send_to_one(message, chat)

    def send_to_one(self, message, nick):
        self.clients[nick].send(message.encode('utf-8'))

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


if __name__ == "__main__":
    server_address = "0.0.0.0"
    server_port = int(sys.argv[1])
    chat_server = ChatServer(server_address, server_port)
    chat_server.start()