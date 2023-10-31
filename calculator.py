
Ans=float(input("number"))
while True:
    opt=input("symbol:")
    if opt=="=":
        break
    num=int(input("number:"))
    
    if opt =="+":
        
        Ans+=num
    elif opt=="-":
        Ans-=num
    elif opt=="*":
        Ans*=num        
    elif opt=="/":
        Ans/=num   
    else:
        print("invalid")
    print("answer:",Ans)  

a=eval(input("enter the number"))

while(True):
    print("enter your choice + - / * = ")
    ch=input()
    if(ch=="="):
        break
    b=eval(input("Enter the number"))
    
    
    match(ch):
        case "+":
            # print(a+b)
            a=a+b
        case"-":
            # print(a-b)
            a=a-b
        case "*":
            # print(a*b)
            a=a*b
        case "/":
            # print(a/b)
            a=a/b
        case default:
            print("Enter wrong sign")  
print("answer :",a)              
               
             
    
       