
global oui   
oui=0
Sudoku=[[1,2,4,1],[2,3,1,2],[4,1,2,4],[2,3,4,1]]
def valid_ligne(Sudoku,n):
    for i in range(len(Sudoku)):
        a=Sudoku[n].count(i)
        if a>=2:
            return False
    return True
 
print(valid_ligne(Sudoku,3))

l1=[1,2,5,5,6,6,6,4,4,5,6,9,9,8,9,1,7,7]
def fonction(l1):
    count=[]
    for i in range  (len(l1)):
        a=l1.count(i)
        count.append(a)
    return count

print(fonction(l1))

            
        
    