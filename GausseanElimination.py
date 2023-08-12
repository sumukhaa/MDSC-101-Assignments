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

def Print(mat):
    print('\nMatrix: ')
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y],end='\t')
        print()

    return 

def gauss_elim(mat):
    arr=[]
    
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

m=int(input('Enter no.of unknowns: '))
mat=add_elements(m,m)
c=[]
for x in range(1,m+1):
    constant=int(input('Enter constant {} : '.format(x)))
    c.append(constant)

for x in range(len(mat)):
    mat[x].append(c[x])

Print(mat)
Print(gauss_elim(mat))