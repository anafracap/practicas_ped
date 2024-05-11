import os, sys, socket, select

class Chat_server:

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.server_socket.listen()
        print(server_socket, file=sys.stderr)

        try: 
            while True:
                readable, _, _ = select.select([self.server_socket] + list(self.clients.values()), [], [])

                for trigger_socket in readable:
                    if trigger_socket == self.server_socket:
                        client_socket, client_address = self.server_socket.accept()
                        nick = self.verify_nick(client_socket)
                        if nick:
                            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}", file=sys.stderr)
                    else: # Receive message from existing client
                        nick = [key for key, value in self.clients.items() if value == trigger_socket][0]
                        message = trigger_socket.recv(1024).decode('utf-8')
                        self.continue_conversation(message, nick)

        except KeyboardInterrupt:
            print("Keyboard interrupt received. Exiting server.", file=sys.stderr)
        finally:
            for nick in self.clients.copy():
                self.disconnect(nick)
            self.server_socket.close()

    def verify_nick(self, cli_sock):
        identify = "Please enter your UNIQUE nickname: "
        cli_sock.send(identify.encode('utf-8'))
        nick = cli_sock.recv(1024).decode('utf-8')
        if nick in self.clients:
            message = "Your nickname is already in use, unable to log in \n"
            self.send_to_one(message, nick)
            cli_sock.close()
            return False
        else:
            self.clients[nick] = cli_sock
            print(list(self.clients), file=sys.stderr)
            login = "You have successfully logged in! Type 'exit' to leave the chat.\n"
            self.send_to_one(login, nick)
            self.chats[nick] = 'all'
            self.groups[chats[nick]].add(nick)
            text = f"{nick} has joined the chat!"
            self.send_to_chat(text, nick)
            return nick

    def continue_conversation(self, message, nick):
        text = f"{nick}: {message}"
        if message.lower() == 'exit':
            self.disconnect(nick)
        elif message.lower().startswith("group: "):
            text = f"{nick} has left the chat!"
            self.send_to_chat(text, nick)
            group = message[len("group: "):]
            if self.chats[nick] in self.groups:
                self.groups[self.chats[nick]].remove(nick)
            self.chats[nick] = group
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
            if self.chats[nick] in self.groups:
                self.groups[self.chats[nick]].remove(nick)
            self.chats[nick] = 'p' + private
            message = f"You have joined a private chat with {private}.\n"
            self.send_to_one(message, nick)
            text = f"{nick} has joined a private chat with you.\n"
            self.send_to_chat(text, nick)
        else:
            self.send_to_chat(text, nick)

    def disconnect(self, nick):
        if nick in self.clients:
            text = f"{nick} has left the chat!"
            self.send_to_chat(text, nick)
            message = 'exit'
            self.send_to_one(message, nick)
            self.clients[nick].close()
            if self.chats[nick] in self.groups:
                self.groups[chats[nick]].remove(nick)
            del self.chats[nick]
            del self.clients[nick]

    def send_to_chat(self, message, nick):
        if self.chats[nick] in self.groups:
            for client in self.groups[self.chats[nick]]:
                self.send_to_one(message, client)
        else:
            private = self.chats[nick][len('p'):]
            if private in self.clients:
                self.send_to_one(message, private)

    def send_to_one(self, message, nick):
        self.clients[nick].send(message.encode('utf-8'))

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