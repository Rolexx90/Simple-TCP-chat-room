import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}:{input("")}'
        client.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
