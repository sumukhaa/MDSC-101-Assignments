
def Print(mat):
    print('\nMatrix: ')
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y],end='\t')
        print()

    return ''

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

def mat_add(mat1,mat2):
    mat3=[]
    for x in range(len(mat1)):
        row=[]
        for y in range(len(mat1[0])):
            z=mat1[x][y]+mat2[x][y]
            row.append(z)
        mat3.append(row)
    return Print(mat3)

def mat_sub(mat1,mat2):
    mat3=[]
    for x in range(len(mat1)):
        row=[]
        for y in range(len(mat1[0])):
            z=mat1[x][y]-mat2[x][y]
            row.append(z)
        mat3.append(row)
    return Print(mat3)

def mat_mul(mat1,mat2):
    mat3=[]
    for x in range(len(mat1)):
        row=[]
        value=0
        for y in range(len(mat2[0])):
            for k in range(len(mat1)):
                value += int(mat1[x][k])*int(mat2[k][y])
            row.append(value)

        #If len=1, append an element into list
        if(len(row)==1):
            mat3.append(row[0])
        #else append a list of elements
        else:
            mat3.append(row)
            
    return Print(mat3)

def main():
    mat1=mat2=[]

    while(True):
        x=int(input('''
1. Display the 2 matrices
2. Input 2 matrices
3. Add both matrices (A+B)
4. Subtract 2 matrices (A-B)
5. Multiply 2 matrices (A*B)
6. Exit\n
Type one of the numbers to do an action: '''))

        if x==1:
            if len(mat1)==0 and len(mat2)==0:
                print('\nNo matrix input given. ')
                continue
            else:
                Print(mat1)
                Print(mat2)
                continue
        
        if x==2:
            m1=int(input('Enter no.of rows of matrix A: '))
            n1=int(input('Enter no.of cols of matrix A: '))
            mat1=add_elements(m1,n1)
    
            m2=int(input('Enter no.of rows of matrix B: '))
            n2=int(input('Enter no.of cols of matrix B: '))
            mat2=add_elements(m2,n2)
    
        if x==3:
            if (len(mat1)==0 and len(mat2)==0):
                print('\nNo matrices input given!')
                continue

            if (m1!=m2 or n1!=n2):
                print('''\nOrder of the matrices is not same.
                        \nType 0 and input new matrices. ''')
                continue
            
            print(mat_add(mat1,mat2))
        
        elif x==4:
            if (len(mat1)==0 and len(mat2)==0):
                print('\nNo matrices input given!')
                continue

            if (m1!=m2 or n1!=n2):
                print('''\n Order of the matrices is not same.
                        \n Type 0 and input new matrices. ''')
                continue
            
            print(mat_sub(mat1,mat2))
        
        elif x==5:
            if (len(mat1)==0 and len(mat2)==0):
                print('\nNo matrices input given!')
                continue

            if (n1!=m2):
                print('''\nThese 2 matrices cant be multiplied.
                        \nType 0 and input new matrices. ''')
                continue
            
            print(mat_mul(mat1,mat2))
        
        elif x==6:
            print("\nBye bye!")
            return ''

        else:
            print('\nEnter a valid number! ')

print(main())
