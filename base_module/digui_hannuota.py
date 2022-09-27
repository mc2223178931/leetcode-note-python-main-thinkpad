def move(n,A,B,C):
    if n == 1:
        print(A,"->",C)
    else:
        move(n-1,A,C,B)
        move(1,A,B,C)
        move(n-1,B,A,C)
n=eval(input("请输入递归层数:"))
move(n,'A','B','C')
