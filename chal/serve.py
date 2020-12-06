import socket
from random import randint

# SOCKET START

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(( "0.0.0.0", 4000))
s.listen(60)
#print('socket start')
# SOCKET END

flag = "flag{Str_C8763}"
test = "flag{Str_C8763}"

def dosort():
    arr = [randint(1, 100) for _ in range(6)]
    return arr, sorted(arr)

errormessage ="Error"

while True:
    conn, addr = s.accept()
    try:
        for _ in range(1):
            q, a = dosort()
            ans = '['+', '.join([str(i) for i in a])+']'
            #print(ans)
            conn.sendall((' '.join([str(i) for i in q]) + '\n').encode())
            conn.sendall("Answer: ".encode())
            data = conn.recv(1024).strip().decode()
            #print(data)
            if (data != ans):
                conn.sendall(errormessage.encode())
                conn.close()

        conn.sendall(test.encode())
        conn.close()
    except socket.error:
        print("ERROR")
        conn.close()