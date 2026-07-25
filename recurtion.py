def recur_facorial(n):
    if n==1:
        return n
    else:
        return n*recur_facorial(n-1)

num = int(input("pls enter the number: "))

# check if the number if negative,or zero, or else

if num<0:
    print("sorry the negative nos dont hava factorial idiot")
elif num== 0 :
    print("the factorial of zero id 1")
else:
    print("the factorial of the number" , num , "is" , recur_facorial(num))