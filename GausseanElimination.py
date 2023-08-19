#Main code starts at line 107

import copy

def mat_mul(mat1,mat2):
    mat3=[]
    for x in range(len(mat1)):
        row=[]
        value=0
        for y in range(len(mat2[0])):
            for k in range(len(mat1)):
                value += round(mat1[x][k]*mat2[k][y])
            row.append(value)

        #If len=1, append an element into list
        if(len(row)==1):
            mat3.append(row[0])
        #else append a list of elements
        else:
            mat3.append(row)
            
    return mat3

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


# MAIN CODE STARTS HERE
#Calculating no. of zero rows to find rank of a matrix
def rank(mat):
    size=len(mat)
    matric=gauss_elim(mat)
    r=0
    for row in matric:
        for j in row:
            if j!=0:
                r-=1
                break
        r+=1
    
    return size-r
        
#Taking elements as input in a 2D Matrix
def add_elements(m,n):
    matrix=[]
    for x in range(m):
        row=[]
        print('Enter all the elements of row ',x,':')
        
        for y in range(n):
            temp=int(input())
            row.append(temp)
            
        matrix.append(row)
        
    return matrix

#Prints matrix in a nice way
def Print(mat):
    print('Matrix: ')
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y],end='\t')
        print()
    print()
    return 

#Performs gaussean elimination for a given matrix
def gauss_elim(matric):
    arr=[]

    mat = copy.deepcopy(matric)
    
    pivot,const=0,0
    for i in range(len(mat)-1):
        for k in range(i+1,len(mat)):
            for j in range(i,len(mat[i])):
                if i==j:
                    pivot=mat[i][j] 
               
                if pivot==0:
                    #Swapping a row if non-zero row is found until zero pivot element
                    for x in range(i+1,len(mat)):
                        if mat[x][i]!=0:
                            temp=mat[x]
                            mat[x]=mat[i]
                            mat[i]=temp
                            #Print(mat)
                            break
                    pivot=mat[i][j]            
                
                if const==0:  
                    const=mat[k][i]/pivot  
                
                mat[k][j]=round(mat[k][j]-const*mat[i][j],3)
            
            #Print(mat)
                
            const=0

    return mat

#Takes a matrix, constant vector and no.ofunkowns as input and checks 
# if the equations are consistent. If consistent it'll print solution!
def consistency(mat,c,u):
    new_mat = copy.deepcopy(mat)
    
    for x in range(len(new_mat)):
        # print('mat',mat)
        # print('new_mat=',new_mat)
        new_mat[x].append(c[x][0])

    print('Gaussean elimination of Matrix A:')
    Print(gauss_elim(mat))
    
    print('Gaussean elimination of Augmented Matrix A|B:')
    Print(gauss_elim(new_mat))

    if rank(mat)==rank(new_mat):
        ran=rank(mat)

        if ran==u:             
            solution=mat_mul(inverse(mat),c)
            print('Since rank(A) = rank(A|B) = No. of unkownks, given set of eqns are')
            return 'Consistent and Unique solution exists. Solution is {}\n'.format(solution)
        
        print('Since rank(A) = rank(A|B) < No. of unkownks, given set of eqns are')
        return 'Consistent but Infinite solutions exist.\n'
    
    print('Since rank(A) != rank(A|B) given set of eqns are')
    return 'Inconsistent and has no solution.\n'


mat1=[[1,-1,2],[2,0,1],[3,2,1]]
c1=[[3],[1],[4]]

mat2=[[1,-4,7],[3,8,-2],[7,-8,26]]
c2=[[14],[13],[5]]

mat3=[[1,1,1],[1,2,3],[1,4,7]]
c3=[[6],[14],[30]]

print(consistency(mat1,c1,3))
