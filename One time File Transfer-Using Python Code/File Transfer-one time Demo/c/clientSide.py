import socket
from datetime import datetime



#initializing host, port, filename, total time and number of times to send the file
host = '192.168.0.18'
port = 9000
fileName = "send.txt"
 

print('I am connecting to server side: ', host,'\n')  
s = socket.socket()
s.connect((host, port))
x=1 
print('I am sending file', fileName,' for the ',x,'th  time')



#opening file to read
file_to_send = open(fileName, 'rb')


    
#reading the first 1024 bytes
data = file_to_send.read(1024)
while data:
    s.send(data)
    
    
#reading the next 1024 bits
    data = file_to_send.read(1024)
print('I am finishing sending file', fileName,' for the ',x,'th  time')
file_to_send.close()

s.close()
print('I am done')
