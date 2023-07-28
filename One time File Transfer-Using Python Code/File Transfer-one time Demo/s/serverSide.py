import socket
import filecmp 
from datetime import datetime

#initializing host, port
HOST = '192.168.0.18'
PORT = 9000

#starting the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
totalTime = 0
print('I am ready for any client side request \n')


# changed from 1 to 100
totalFilesCount = 100  
i=0;
fileName = 'CompareStandard.txt';

# allows the server to receive multiple files from the client
for i in range(1, totalFilesCount + 1):
    conn, addr = s.accept()
    file = 'receive' + str(i) + '.txt'
    print('I am starting receiving file', file, 'for the', i, 'th time')



#opening the file to write
f = open(file, 'wb')
data = conn.recv(1024)
while (data):
    f.write(data)
    data = conn.recv(1024)
f.close()
print('I am finishing receiving file ', file, 'for the ',i,'th time ')
conn.close()
s.close()



# add the code to verify each received file here
# use function "filecmp.cmp('received.txt", fileName, ...)"

error_count = 0
for i in range(1, totalFilesCount + 1):
    file = 'receive' + str(i) + '.txt'
    if not filecmp.cmp(file, fileName):
        error_count += 1

print("Error rate: {}/{}".format(error_count, totalFilesCount))