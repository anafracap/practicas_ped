import os, sys, socket, select

def send_all_clients(message):
    for nick, c in clients.items():
        try:
            send_to_one(message, c)
        except:
            disconnect(nick)

def send_to_chat(message, nick):
    if chats[nick] in groups:
        for client in groups[chats[nick]]:
            send_to_one(message, client)
    else:
        private = chats[nick][len('p'):]
        if private in clients:
            send_to_one(message, private)

def sent_to_one(message, nick):
    clients[nick].send(message.encode('utf-8'))

def verify_nick(cli_sock):
    identify = "Please enter your UNIQUE nickname: "
    cli_sock.send(identify.encode('utf-8'))
    nick = cli_sock.recv(1024).decode('utf-8')
    if nick in clients:
        message = "Your nickname is already in use, unable to log in \n"
        sent_to_one(message, nick)
        cli_sock.close()
        return False
    else:
        clients[nick] = cli_sock
        print(list(clients), file=sys.stderr)
        login = "You have successfully logged in! Type 'exit' to leave the chat.\n"
        sent_to_one(login, nick)
        chats[nick] = 'all'
        groups[chats[nick]].add(nick)
        text = f"{nick} has joined the chat!"
        send_to_chat(text, nick)
        return nick

def continue_conversation(message, nick):
    text = f"{nick}: {message}"
    if message.lower() == 'exit':
        disconnect(nick)
    elif message.lower().startswith("group: "):
        text = f"{nick} has left the chat!"
        send_to_chat(text, nick)
        group = message[len("group: "):]
        if chats[nick] in groups:
            groups[chats[nick]].remove(nick)
        chats[nick] = group
        if not group in groups:
            groups[group] = set()
        groups[group].add(nick)
        message = f"You have joined the group {group}.\n"
        send_to_one(message, nick)
        text = f"{nick} has joined the chat!"
        send_to_chat(text, nick)
    elif message.lower().startswith("private: "):
        text = f"{nick} has left the chat!"
        send_to_chat(text, nick)
        private = message[len("private: "):]
        if chats[nick] in groups:
            groups[chats[nick]].remove(nick)
        chats[nick] = 'p' + private
        message = f"You have joined a private chat with {private}.\n"
        send_to_one(message, nick)
        text = f"{nick} has joined a private chat with you.\n"
        send_to_chat(text, nick)
    else:
        send_to_chat(text, nick)

def disconnect(nick):
    if nick in clients:
        text = f"{nick} has left the chat!"
        send_to_chat(text, nick)
        message = 'exit'
        send_to_one(message, nick)
        clients[nick].close()
        if chats[nick] in groups:
            groups[chats[nick]].remove(nick)
        del chats[nick]
        del clients[nick]
        

server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))
server_socket.listen()
print(server_socket, file=sys.stderr)

clients = {}
chats = {}
groups = {'all' : set()}

try: 
    while True:
        readable, _, _ = select.select([server_socket] + list(clients.values()), [], [])

        for trigger_socket in readable:
            if trigger_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                nick = verify_nick(client_socket)
                if nick:
                    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}", file=sys.stderr)
            else: # Receive message from existing client
                nick = [key for key, value in clients.items() if value == trigger_socket][0]
                message = trigger_socket.recv(1024).decode('utf-8')
                continue_conversation(message, nick)

except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting server.", file=sys.stderr)
finally:
    for nick in clients.copy():
        disconnect(nick)
    server_socket.close()

