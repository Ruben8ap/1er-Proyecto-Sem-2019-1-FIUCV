def ProductoMatricial (A,B):
    resultado=[[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]
    for r in resultado:
        print(r)
    return A,B
