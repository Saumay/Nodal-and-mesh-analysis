# coding=utf-8
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

elif atype==2:
    print ("MESH ANALYSIS\nNote TYPE=1,2,3")    
    ch=int(input("Enter type:"))
    r=[]
    V=[]
    a=1
    if ch==1:
        l=14
        a1=7
    elif ch==2:
        l=15
        a1=9
    elif ch==3:
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

    if ch==1:
        d=[[r[0]+r[1]+r[2]+r[6],-r[6]],[-r[6],r[3]+r[4]+r[5]+r[6]]]
        d1=[[V[0]+V[1]+V[2],-r[6]],[V[3]+V[4]+V[5],r[3]+r[4]+r[5]+r[6]]]
        d2=[[r[0]+r[1]+r[2]+r[6],V[0]+V[1]+V[2]],[-r[6],V[3]+V[4]+V[5]]]
        print ("Ï1=",(format((det(d1)/det(d)),'.4f')),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A")
    elif ch==2:
        d=[[r[0]+r[1]+r[2]+r[3],-r[6],-r[7]],[-r[6],r[2]+r[6]+r[3]+r[8],-r[8]],[-r[7],-r[8],r[4]+r[7]+r[8]+r[5]]]
        d1=[[V[0]+V[1],-r[6],-r[7]],[V[2]+V[3],r[2]+r[6]+r[3]+r[8],-r[8]],[V[4],-r[8],r[4]+r[7]+r[8]+r[5]]]
        d2=[[r[0]+r[1]+r[2]+r[3],V[0]+V[1],-r[7]],[-r[6],V[2]+V[3],-r[8]],[-r[7],V[4],r[4]+r[7]+r[8]+r[5]]]
        d3=[[r[0]+r[1]+r[2]+r[3],-r[6],V[0]+V[1]],[-r[6],r[2]+r[6]+r[3]+r[8],V[2]+V[3]],[-r[7],-r[8],V[4]]]
        print( "Ï1=",(format((det(d1)/det(d)),'.4f')),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A\nI3=",(format((det(d3)/det(d)), '.4f')),"A")
    elif ch==3 :
        d=[[r[0]+r[1]+r[2]+r[8],-r[8],0],[-r[8],r[3]+r[9]+r[8]+r[4],-r[9]],[0,-r[9],r[5]+r[6]+r[7]+r[9]]]
        d1=[[V[0]+V[1]+V[2],-r[8],0],[V[3]+V[4],r[3]+r[9]+r[8]+r[4],-r[9]],[V[5]+V[6]+V[7],-r[9],r[5]+r[6]+r[7]+r[9]]]
        d2=[[r[0]+r[1]+r[2]+r[8],V[0]+V[1]+V[2],0],[-r[8],V[3]+V[4],-r[9]],[0,V[5]+V[6]+V[7],r[5]+r[6]+r[7]+r[9]]]
        d3=[[r[0]+r[1]+r[2]+r[8],-r[8],V[0]+V[1]+V[2]],[-r[8],r[3]+r[9]+r[8]+r[4],V[3]+V[4]],[0,-r[9],V[5]+V[6]+V[7]]]     
        print( "Ï1=",(format((det(d1)/det(d)),'.4f')),"A\nI2=",(format((det(d2)/det(d)), '.4f')),"A\nI3=",(format((det(d3)/det(d)), '.4f')),"A")
else:
    print("ERROR , PLEASE ENTER CHOICE CORRECTLY ie 1 for nodal and 2 for mesh")

