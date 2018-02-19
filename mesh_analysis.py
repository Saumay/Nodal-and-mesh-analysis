#determinant of matrix
def det(l):
    n=len(l)
    if n>2:
        i=1
        t=0
        sum=0
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

    if n==2:
        cw=1
        while(i<=n):
            print('\nFOR NODE',i,'-')
            print('total no. of resistors connected to node',i,'-',)
            r=int(input())
            if cw==1:
                print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                r_mid=int(input('value of resistance connected between node 1 and node 2:'))
                cw=2
            if r_mid==0:
                c_mid=0
            else:
                c_mid=1/r_mid
            print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
            sum=0
            for j in range(1,r):
                print('r',j,':')
                rnode=int(input())
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

        print('\nAT NODE 1- ')
        II=int(input('net incoming current:'))
        Io=int(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=int(input('net incoming current:'))
        Io2=int(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        matrix0=[[l1[0],-c_mid],[-c_mid,l1[1]]]
        matrix1=[[I1,-c_mid],[I2,l1[1]]]
        matrix2=[[l1[0],I1],[-c_mid,I2]]

        a=det(matrix0)
        b=det(matrix1)
        c=det(matrix2)
        V1=a/b
        V2=a/c
        print('\nNode 1 Voltage:',V1)
        print('Node 2 Voltage:',V2)



#for 3 node system
    elif n==3:
        qw=1
        i=1
        while(i<=n):
            if qw==1:
                print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                r_12=int(input('value of resistance connected between node 1 and node 2:'))
                r_23=int(input('value of resistance connected between node 2 and node 3:'))
                r_13=int(input('value of resistance connected between node 1 and node 3:'))
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
        
            #print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
            sum=0
            for j in range(1,r+1):
                print('r',j,':')
                rnode=int(input())
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
        II=int(input('net incoming current:'))
        Io=int(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=int(input('net incoming current:'))
        Io2=int(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        print('\nAT NODE 3- ')
        II3=int(input('net incoming current:'))
        Io3=int(input('net outgoing current:'))
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
        print('\nNode 1 Voltage:',V1)
        print('Node 2 Voltage:',V2)
        print('Node 3 Voltage:',V3)


#for 4-node system
    elif n==4:
        qw=1
        i=1
        while(i<=n):
            if qw==1:
                print('\nFOR RESISTANCE CONNECTED BETWEEN NODES')
                r_12=int(input('value of resistance connected between node 1 and node 2:'))
                r_23=int(input('value of resistance connected between node 2 and node 3:'))
                r_13=int(input('value of resistance connected between node 1 and node 3:'))
                r_14=int(input('value of resistance connected between node 1 and node 4:'))
                r_24=int(input('value of resistance connected between node 2 and node 4:'))
                r_34=int(input('value of resistance connected between node 3 and node 4:'))
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
        
        #print('\nNOW, FOR RESISTANCES CONNECTED BETWEEN NODES AND NEUTRAL')
            sum=0
            for j in range(1,r+1):
                print('r',j,':')
                rnode=int(input())
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
            #Print(l1)
            i=i+1
    
#taking input of currents
        print('\nAT NODE 1- ')
        II=int(input('net incoming current:'))
        Io=int(input('net outgoing current:'))
        IO=-Io
        I1=IO+II

        print('\nAT NODE 2- ')
        II2=int(input('net incoming current:'))
        Io2=int(input('net outgoing current:'))
        IO2=-Io2
        I2=IO2+II2

        print('\nAT NODE 3- ')
        II3=int(input('net incoming current:'))
        Io3=int(input('net outgoing current:'))
        IO3=-Io3
        I3=IO3+II3

        print('\nAT NODE 4- ')
        II4=int(input('net incoming current:'))
        Io4=int(input('net outgoing current:'))
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
        print('\nNode 1 Voltage:',V1)
        print('Node 2 Voltage:',V2)
        print('Node 3 Voltage:',V3)
        print('Node 4 Voltage:',V4)
          
elif atype==2:
    print(atype)