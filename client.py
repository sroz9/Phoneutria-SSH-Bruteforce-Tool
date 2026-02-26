import threading
import socket
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
nickname = input("[*] Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.107.195.160", 55734))

running = True  

def receive():
    global running
    while running:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            elif message == "EXIT":
                print("[-] Disconnected from server.")
                running = False
                client.close()
                break
            else:
                print(message)
        except:
            running = False
            client.close()
            break

def write():
    global running
    while running:
        try:
            message = input(">")
            if message.lower() == "/exit":
                client.send("EXIT".encode("ascii"))  
                continue  
            client.send(f"{nickname}: {message}".encode("ascii"))
        except:
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
