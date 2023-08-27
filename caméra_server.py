import socket
import cv2
import numpy as np
import keyboard

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.163', 1233)

sock.bind(server_address)

sock.listen()

conn, addr = sock.accept()

screen = cv2.VideoCapture(0)

while True:
    ret, frame = screen.read()
    
    img_encoded = cv2.imencode('.jpg', frame)

    data = img_encoded[1].tobytes()

    conn.sendall(data)
    if keyboard.is_pressed('a'):
        break

sock.close()
conn.close()
screen.release()