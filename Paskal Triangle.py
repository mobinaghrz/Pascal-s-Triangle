ExcpectedLine = int(input("Please Enter the Expected Line Number:"))
LinearHolder_L = []

if ExcpectedLine == 1:
    LinearHolder_L.append(1)
    print(LinearHolder_L)

elif ExcpectedLine == 2:
    print(LinearHolder_L)

else:

    LinearHolder_L = [1,1,1]

    Pointer1 = 1

    counter = 3
    EndLen = 3

    while counter <= ExcpectedLine:
        Pointer2 = Pointer1 + 1
        LinearHolder_L.append(1)
        EndLen += counter

        while len(LinearHolder_L) < EndLen-1:

            LinearHolder_L.append(LinearHolder_L[Pointer1]+LinearHolder_L[Pointer2])
            Pointer1+=1
            Pointer2+=1
        
        LinearHolder_L.append(1)
        counter+=1
        Pointer1 += 1

    print(LinearHolder_L)

