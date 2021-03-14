#Wap in which user take input the operator to operate the expression.

print("A=10 and B=20")
while(1):
    
    op=input("Enter Any Operator for performing operation on expression: ")
    a=10
    b=20
    
    if(op=="+"):
       sum=a+b
       print("A+B:",sum)
    elif(op=="-"):
       sub=a-b
       print("A-B:",sub)
    elif(op=="*"):
       mul=a*b
       print("A*B:",mul)
    elif(op=="/"):
       div=a/b
       print("A/B:",div)
    else:
       print("Invalid Operator")
       
    
    


        
