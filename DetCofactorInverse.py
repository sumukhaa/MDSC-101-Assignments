def Print(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y],end='\t')
        print()

    return ''

def minor(row,col):
    if (row+col)%2==0:
        return 1
    return -1

def cofactor(arr): #returns cofactor matrix
    cof_arr=[]

    for i in range(len(arr)):
        cof_row=[]
        for j in range(len(arr[i])):
            row = i
            col = j

            temp=[]
            for x in range(len(arr)):
                row_arr=[]
                for y in range(len(arr)):
                    if x!=row and y!=col:
                        row_arr.append(arr[x][y])

                if len(row_arr)!=0:
                    temp.append(row_arr)
            
            cofactor=minor(row,col)*determinant(temp)
            cof_row.append(cofactor)
        cof_arr.append(cof_row)

    return cof_arr

def determinant(mat): #returns determinant of the matrix
    det=0
    if len(mat)==2:
        det=(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])
    
    else:
        for i in range(len(mat)):
            row = 0
            col = i

            temp=[]
            for x in range(len(mat)):
                row_arr=[]
                for y in range(len(mat)):
                    if x!=row and y!=col:
                        row_arr.append(mat[x][y])

                if len(row_arr)!=0:
                    temp.append(row_arr)

            det+=minor(row,col)*mat[row][col]*determinant(temp)

    return det

def transpose(mat):
    trans=[]
    size=len(mat)
    
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat)):
            row.append(mat[j][i])
        trans.append(row)

    return trans

def inverse(mat):
    inv=[]
    adj=transpose(cofactor(mat))
    det=determinant(mat)

    for i in range(len(mat)):
        row=[]
        for j in range(len(mat)):
            elem=adj[i][j]/det
            if elem==-0.0:
                elem=0
            row.append(elem)
        inv.append(row)

    return inv


    
arr=[[1,2],
     [3,4]]
arr2=[[1,2,3],
      [4,5,6],
      [7,8,9]]
arr3=[[1,3,1,4],
      [3,9,5,15],
      [0,2,1,1],
      [0,4,2,3]]

print('Det of the matrix is: ', determinant(arr3))

print('Cofactor of the matrix is: ')
Print(cofactor(arr3))

print('Transpose of the matrix is: ')
Print(transpose(arr3))

print('Inverse of the matrix is: ')
Print(inverse(arr3))