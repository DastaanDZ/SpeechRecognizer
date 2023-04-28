import turtle
turtle.bgcolor("black")
dz = turtle.Turtle()

width=5
height=7

dot_distance = 25

dz.setpos(-250,250)

dz.penup()
def spiral(m,n):
    k,l = 0,0
    flag = 0
    dz.color("white")

    while(k<m and l<n):

        if flag == 1:
            dz.right(90)

        for i in range(l,n):
            dz.dot()
            dz.forward(dot_distance)
            # print(a[k][i], ends=" ")
        k+=1
        flag = 1

        dz.right(90)

        for i in range(k,m):
            dz.dot()
            dz.forward(dot_distance)
            # print(a[i][n-1], ends=" ")
        n-=1
        
        dz.right(90)
        if(k<m):
            for i in range(n-1,l-1,-1):
                dz.dot()
                dz.forward(dot_distance)
                # print(a[m-1][i], ends=" ")
            m-=1

        dz.right(90)

        if(l<n):
            for i in range(m-1,k-1,-1):
                # print(a[i][l], ends=" ")
                dz.dot()
                dz.forward(dot_distance)

            l+=1

spiral(20,20)
turtle.done()