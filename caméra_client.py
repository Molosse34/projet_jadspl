import socket
import numpy as np
import cv2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.101', 1233)

sock.connect(server_address)

data = b''  # Initialiser le tampon de données

while True:
    packet = sock.recv(4096)
    if not packet:
        break
    data += packet

    
    if packet.endswith(b'\xff\xd9'):
       
        img_data = np.frombuffer(data, dtype=np.uint8)
        frame = cv2.imdecode(img_data, flags=cv2.IMREAD_COLOR)
        cv2.imshow('Screen', frame)

        if cv2.waitKey(1) == ord('a'):
            break

        data = b''  

sock.close()
cv2.destroyAllWindows()