import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0",4000))
s.listen(60)

flag="flag{5201314}"

errormessage="ERROR"
n1="16696107426011171174262336472112678981490112006105780001313833092028351494218061654773105559349071306655941268549561999231216258581311874627306547188414142613468304294902377561328571311725643733258014771257547527004453272047390617660427802675001909124270986379736632416155192382439839746928767850432904144499738085382889239996222727557173507408482139393644418538946546634519108892441684995840523844427668015754554458776703218439129424547038669717975572293810221686640755479968577033372543704022690211391138407503628986364922636200614050899505817463903658033353935219075656983819510570502988960754516145919393103981301"
n2="21931214102758530322832620158035671370505215772000127064860347769478178044423493002630209332654850761380319781758558472756052548620085283466649978186073849978114993046457807340599461620685233082157047641647173917788068894247004755208607532824840703067713391052600413226549183678241109114717121721117207839117667430329052726524910515545306462946875444788995858969899538933842403432416373575035475505855892682612601715687886156136722286162255535069230587795416483552505948673918427036799966390624637576285712644992335642983718712790941010000729654399816232099073418977745673310583072214994498145912664184205801036440463"
while True:
    conn,addr=s.accept()
    try:
        conn.sendall("Hospital B has cooperated with Hospital A for a long time. ".encode())
        conn.sendall("one day suddenly wanted to steal the encrypted message from Hospital A".encode())
        conn.sendall("Please help Hospital B to get the encrypted message from Hospital A".encode())
        conn.sendall("There are two public key for federated learning".encode())
        conn.sendall("key1:".encode())
        conn.sendall(n1.encode())
        conn.sendall("key2:".encode())
        conn.sendall(n2.encode())
        conn.sendall("They use keras to run the model".encode())
        conn.sendall("Please use model.config and cypertext file (pc1.txt) to get answer".encode())
        conn.sendall("Answer is the last 6 weight Answer example: flag{XXXXXXX}".encode())
        conn.sendall("Answer: ".encode())
        data = conn.recv(1024).strip().decode()
        if (data != flag):
            conn.sendall(errormessage.encode())
            conn.close()
        else:
            conn.sendall(flag.encode())
            conn.close()
            
    except socket.error:
        print("socket error")
        conn.close()