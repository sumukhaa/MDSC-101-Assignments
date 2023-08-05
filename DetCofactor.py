def minor(row,col):
    if (row+col)%2==0:
        return 1
    return -1

def cof(arr): #returns cofactor matrix
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
            
            cofactor=minor(row,col)*deter(temp)
            cof_row.append(cofactor)
        cof_arr.append(cof_row)

    return cof_arr

def deter(mat): #returns determinant of the matrix
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

            det+=minor(row,col)*mat[row][col]*deter(temp)

    return det

arr=[[1,2],
     [3,4]]
arr2=[[1,2,3],
      [4,5,6],
      [7,8,9]]
arr3=[[1,3,1,4],
      [3,9,5,15],
      [0,2,1,1],
      [0,4,2,3]]

print(deter(arr3))
print(cof(arr3))