import socket
import pyautogui as pag
import keyboard as key

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.101', 1233)

sock.bind(server_address)

sock.listen()

conn, addr = sock.accept()
while True:
    image = pag.screenshot()

    image_bit = image.tobytes()

    conn.sendall(image_bit)

    if key.is_pressed('a'):
        break
sock.close()
conn.close()