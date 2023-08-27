import socket 
import pyautogui

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('192.168.1.163', 1233)
sock.bind(server_adress)
sock.listen()

conn, addr = sock.accept()

