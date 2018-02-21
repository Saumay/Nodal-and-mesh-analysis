# coding=utf-8
#determinant of matrix
def det(l):
    n=len(l)
    if n>2:
        i=1
        t=0
        sum=float(0)
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if m==t:
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return(l[0][0]*l[1][1]-l[0][1]*l[1][0])

print('Analysis type:')
print('FOR NODAL ANALYSIS-1 \nFOR MESH ANALYSIS-2')
atype=int(input('\nAnalysis type:'))
print('\n')
if atype==1:
    print('NODAL ANALYSIS:')
    n=int(input('no. of nodes:'))
    i=1
    l1=[]
#for 2 node system
    if n==2:
        cw=1
        while(i<=n):
            print('\nFOR NODE',i,'-')
            print('total no. of resistors connected to node',i,'-',)
            r=int(input())
            if r==0:
                finalsum=0
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
                
            else:
                if cw==1:
                    print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                    r_mid=float(input('value of resistance connected between node 1 and node 2:'))
                    cw=2
                if r_mid==0:
                    c_mid=0
                else:
                    c_mid=1/r_mid
                print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
                sum=0
                for j in range(1,r):
                    print('r',j,':')
                    rnode=float(input())
#solving in terms of conductances
                    if rnode==0:
                        c=0
                    else:
                        c=1/rnode
                    sum=sum+c
                    finalsum=sum+c_mid
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
    
#taking input of currents
        print('\nAT NODE 1- ')
        II=float(input('net incoming current:'))
        Io=float(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=float(input('net incoming current:'))
        Io2=float(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        matrix0=[[l1[0],-c_mid],[-c_mid,l1[1]]]
        matrix1=[[I1,-c_mid],[I2,l1[1]]]
        matrix2=[[l1[0],I1],[-c_mid,I2]]
        #print(matrix0)
        #print(matrix1)
        #print(matrix2)

#calculating node voltage
        a=det(matrix0)
        b=det(matrix1)
        c=det(matrix2)
        V1=a/b
        V2=a/c
        print('\nNode 1 Voltage:',V1,'V')
        print('Node 2 Voltage:',V2,'V')



#for 3 node system
    elif n==3:
        qw=1
        i=1
        while(i<=n):
            if qw==1:
                print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                r_12=float(input('value of resistance connected between node 1 and node 2:'))
                r_23=float(input('value of resistance connected between node 2 and node 3:'))
                r_13=float(input('value of resistance connected between node 1 and node 3:'))
                qw=2
#problem-common resistance between nodes has to be input again and again for every loop
            if r_12==0:
                c_12=0
            else:
                c_12=1/r_12

            if r_23==0:
                c_23=0
            else:
                c_23=1/r_23

            if r_13==0:
                c_13=0
            else:
                c_13=1/r_13
            

            print('\nFOR NODE',i,'-')
            print('total no. of resistors connected between node',i,' and neutral-',)
            r=int(input())
            if r==0:
                if i==1:
                    sum=0
                    finalsum=sum+c_12+c_13
                if i==2:
                    sum=0
                    finalsum=sum+c_23+c_12
                if i==3:
                    sum=0
                    finalsum=sum+c_13+c_23
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
            else:
                #print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
                sum=0
                for j in range(1,r+1):
                    print('r',j,':')
                    rnode=float(input())
#solving in terms of conductances
                    c=1/rnode
                    sum=sum+c
                    if i==1:
                        finalsum=sum+c_12+c_13
                    elif i==2:
                        finalsum=sum+c_23+c_12
                    elif i==3:
                        finalsum=sum+c_13+c_23
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
    
#taking input of currents
        print('\nAT NODE 1- ')
        II=float(input('net incoming current:'))
        Io=float(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=float(input('net incoming current:'))
        Io2=float(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        print('\nAT NODE 3- ')
        II3=float(input('net incoming current:'))
        Io3=float(input('net outgoing current:'))
        IO3=-Io3
        I3=IO3+II3

        matrix0=[[l1[0],-c_12,-c_13],[-c_12,l1[1],-c_23],[-c_13,-c_23,l1[2]]]
        matrix1=[[I1,-c_12,-c_13],[I2,l1[1],-c_23],[I3,-c_23,l1[2]]]
        matrix2=[[l1[0],I1,-c_13],[-c_12,I2,-c_23],[-c_13,I3,l1[2]]]
        matrix3=[[l1[0],-c_12,I1],[-c_12,l1[1],I2],[-c_13,-c_23,I3]]
        #print(matrix0)
        #print(matrix1)
        #print(matrix2)
        #print(matrix3)
#calculating node voltage
        a=det(matrix0)
        b=det(matrix1)
        c=det(matrix2)
        d=det(matrix3)
        V1=b/a
        V2=c/a
        V3=d/a
        print('\nNode 1 Voltage:',V1,'V')
        print('Node 2 Voltage:',V2,'V')
        print('Node 3 Voltage:',V3,'V')


#for 4-node system
    elif n==4:
        qw=1
        i=1
        while(i<=n):
            if qw==1:
                print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                r_12=float(input('value of resistance connected between node 1 and node 2:'))
                r_23=float(input('value of resistance connected between node 2 and node 3:'))
                r_13=float(input('value of resistance connected between node 1 and node 3:'))
                r_14=float(input('value of resistance connected between node 1 and node 4:'))
                r_24=float(input('value of resistance connected between node 2 and node 4:'))
                r_34=float(input('value of resistance connected between node 3 and node 4:'))
                qw=2
#problem-common resistance between nodes has to be input again and again for every loop
            if r_12==0:
                c_12=0
            else:
                c_12=1/r_12

            if r_23==0:
                c_23=0
            else:
                c_23=1/r_23

            if r_13==0:
                c_13=0
            else:
                c_13=1/r_13

            if r_14==0:
                c_14=0
            else:
                c_14=1/r_14

            if r_24==0:
                c_24=0
            else:
                c_24=1/r_24

            if r_34==0:
                c_34=0
            else:
                c_34=1/r_34

            print('\nFOR NODE',i,'-')
            print('total no. of resistors connected between node',i,' and neutral-',)
            r=int(input())

            if r==0:
                sum=0
                if i==1:
                    finalsum=sum+c_12+c_13+c_14
                elif i==2:
                    finalsum=sum+c_23+c_12+c_24
                elif i==3:
                    finalsum=sum+c_14+c_24+c_34
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
        
        #print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
            else:
                sum=0
                for j in range(1,r+1):
                    print('r',j,':')
                    rnode=float(input())
#solving in terms of conductances
                    c=1/rnode
                    sum=sum+c
                    if i==1:
                        finalsum=sum+c_12+c_13+c_14
                    elif i==2:
                        finalsum=sum+c_23+c_12+c_24
                    elif i==3:
                        finalsum=sum+c_13+c_23+c_34
                    elif i==4:
                        finalsum=sum+c_14+c_24+c_34
                l1.append(finalsum)
                #print(finalsum)
                #print(l1)
                i=i+1
    
#taking input of currents
        print('\nAT NODE 1- ')
        II=float(input('net incoming current:'))
        Io=float(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=float(input('net incoming current:'))
        Io2=float(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        print('\nAT NODE 3- ')
        II3=float(input('net incoming current:'))
        Io3=float(input('net outgoing current:'))
        IO3=-Io3
        I3=IO3+II3

        print('\nAT NODE 4- ')
        II4=float(input('net incoming current:'))
        Io4=float(input('net outgoing current:'))
        IO4=-Io4
        I4=IO4+II4

        matrix0=[[l1[0],-c_12,-c_13,-c_14],[-c_12,l1[1],-c_23,-c_24],[-c_13,-c_23,l1[2],-c_34],[-c_14,-c_24,-c_34,l1[3]]]
        matrix1=[[I1,-c_12,-c_13,-c_14],[I2,l1[1],-c_23,-c_24],[I3,-c_23,l1[2],-c_34],[I4,-c_24,-c_34,l1[3]]]
        matrix2=[[l1[0],I1,-c_13,-c_14],[-c_12,I2,-c_23,-c_24],[-c_13,I3,l1[2],-c_34],[-c_14,I4,-c_34,l1[3]]]
        matrix3=[[l1[0],-c_12,I1,-c_14],[-c_12,l1[1],I2,-c_24],[-c_13,-c_23,I3,-c_34],[-c_14,-c_24,I4,l1[3]]]
        matrix4=[[l1[0],-c_12,-c_13,I1],[-c_12,l1[1],-c_23,I2],[-c_13,-c_23,l1[2],I3],[-c_14,-c_24,-c_34,I4]]
        #print(matrix0)
        #print(matrix1)
        #print(matrix2)
        #print(matrix3)
#calculating node voltage
        a=det(matrix0)
        b=det(matrix1)
        c=det(matrix2)
        d=det(matrix3)
        e=det(matrix4)
        V1=b/a
        V2=c/a
        V3=d/a
        V4=e/a
        print('\nNode 1 Voltage:',V1,'V')
        print('Node 2 Voltage:',V2,'V')
        print('Node 3 Voltage:',V3,'V')
        print('Node 4 Voltage:',V4,'V')

elif atype==2:    
    print ("MESH ANALYSIS\n")    
    ch=int(input("No. of meshes(2 or 3):"))
    if ch==3:
        chx=input('Circuit Type(a or b):')
    r=[]
    V=[]
    a=1
    if ch==2:
        l=14
        a1=7
    elif chx=='a':
        l=15
        a1=9
    elif chx=='b':
        l=19
        a1=10
    for i in range(1,l):
        if a<=a1:
            print('R',i,':')
            r.append(float(input()))
            a=a+1
        else:
            print('V',i-a1,':')
            V.append(float(input()))

    if ch==2:
        d=[[r[0]+r[1]+r[2]+r[6],-r[6]],[-r[6],r[3]+r[4]+r[5]+r[6]]]
        d1=[[V[0]+V[1]+V[2],-r[6]],[V[3]+V[4]+V[5],r[3]+r[4]+r[5]+r[6]]]
        d2=[[r[0]+r[1]+r[2]+r[6],V[0]+V[1]+V[2]],[-r[6],V[3]+V[4]+V[5]]]
        print ("Ï1=",(format((det(d1)/det(d)),'.4f',)),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A")
    elif chx=='a':
        d=[[r[0]+r[1]+r[2]+r[3],-r[6],-r[7]],[-r[6],r[2]+r[6]+r[3]+r[8],-r[8]],[-r[7],-r[8],r[4]+r[7]+r[8]+r[5]]]
        d1=[[V[0]+V[1],-r[6],-r[7]],[V[2]+V[3],r[2]+r[6]+r[3]+r[8],-r[8]],[V[4],-r[8],r[4]+r[7]+r[8]+r[5]]]
        d2=[[r[0]+r[1]+r[2]+r[3],V[0]+V[1],-r[7]],[-r[6],V[2]+V[3],-r[8]],[-r[7],V[4],r[4]+r[7]+r[8]+r[5]]]
        d3=[[r[0]+r[1]+r[2]+r[3],-r[6],V[0]+V[1]],[-r[6],r[2]+r[6]+r[3]+r[8],V[2]+V[3]],[-r[7],-r[8],V[4]]]
        print( "Ï1=",(format((det(d1)/det(d)),'.4f')),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A\nI3=",(format((det(d3)/det(d)), '.4f')),"A")
    elif chx=='b':
        d=[[r[0]+r[1]+r[2]+r[8],-r[8],0],[-r[8],r[3]+r[9]+r[8]+r[4],-r[9]],[0,-r[9],r[5]+r[6]+r[7]+r[9]]]
        d1=[[V[0]+V[1]+V[2],-r[8],0],[V[3]+V[4],r[3]+r[9]+r[8]+r[4],-r[9]],[V[5]+V[6]+V[7],-r[9],r[5]+r[6]+r[7]+r[9]]]
        d2=[[r[0]+r[1]+r[2]+r[8],V[0]+V[1]+V[2],0],[-r[8],V[3]+V[4],-r[9]],[0,V[5]+V[6]+V[7],r[5]+r[6]+r[7]+r[9]]]
        d3=[[r[0]+r[1]+r[2]+r[8],-r[8],V[0]+V[1]+V[2]],[-r[8],r[3]+r[9]+r[8]+r[4],V[3]+V[4]],[0,-r[9],V[5]+V[6]+V[7]]]     
        print( "Ï1=",(format((det(d1)/det(d)),'.4f',)),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A\nI3=",(format((det(d3)/det(d)), '.4f')),"A")
else:
    print("ERROR , PLEASE ENTER CHOICE CORRECTLY ie 1 for nodal and 2 for mesh")
