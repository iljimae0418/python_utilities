from sympy import * 

A = Matrix([[3,3,6],[2,1.5,5]]).rref()  
print A # The first is the reduced row echelon form, the second is a tuple of indices of the pivot columns.  
