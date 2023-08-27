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
        decoded_screenshot = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        
        if decoded_screenshot is not None:

            cv2.imshow('Screen', decoded_screenshot)
            if cv2.waitKey(1) == ord('a'):
                break
        else:
            print('Echec de décodage !!!')

        data = b''  

sock.close()
cv2.destroyAllWindows()