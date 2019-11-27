import numpy as np
import matplotlib.pyplot as plt 
q=np.ones((1,10) ,dtype=np.int16)
print (q)
q=np.ones((1,10) ,dtype=np.int16)*0
print (q)
q=np.ones((1,10) ,dtype=np.int16)*5
print (q)
#q2..............................................................
a = np.arange( 30, 71, 1 )
print(a)
#q3...............................................................
a=np.arange( 30, 71, 1 )
for x in a:
    if x%2==0:
        print(x)
#q4................................................................
a = np.arange(12).reshape(3,4)
print(a) 
#q5.................................................................
a = np.random.normal(0,1,1)
print(a)

#q6.................................................................
a = np.arange(10,22).reshape((3, 4))
for x in np.nditer(a):
  print(x,end=" ")


#q7.................................................................
x = np.arange(20)
for a in x:
    if a in range(9,15):
        a=a*-1 
    print(a,end=" ")    
#q8...................................................................
x = np.array([1,8,3,5])
y=np.random.randint(0,11,4)
print("x*y: ",x*y)

#q9...................................................................
c = np.array([[1, 4, 7, 5],[2, 8, 3, 2]])
print ("number of rows and columns: ", c.shape)
print(c)


#q10..................................................................
x = np.random.random((3, 3, 3))
print(x)

#q11..................................................................
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])
print("a-b: ",a-b)
print("a*b: ",a*b)
print("a.dot(b): ",a.dot(b))
print("a*2: ",a*2)
print("np.sin(a): ",np.sin(a))
print("a<3: ",a<3)
print("a.sum(): ",a.sum())
print("a.sum(axis=0): ",a.sum(axis=0))
print("c.sum(): ",c.sum())
print("c.sum(axis=0): ",c.sum(axis=0))
print("a.min(): ",a.min())
print("a.max(): ",a.max())
print("a.mean(): ",a.mean())
print("a average(): ",np.average(a))
print("a median(): ",np.median(a))
print("a std(): ",np.std(a))
print("a var(): ",np.var(a))
print("c.cumsum(): ",c.cumsum())
print("a[1:2] : ",a[1:2])
print("a[2:] : ",a[2:])
print("c[-1] : ",c[-1])



#q12.....................................................................
def y(x) : return x*3
x=np.arange(1,50)

plt.plot(x,y(x))
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title('Draw a line')
plt.show()
#q13.....................................................................
x1=np.array([10,20,30])
y1=np.array([20,40,10])
x2=np.array([10,20,30])
y2=np.array([40,10,30])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.show()


#q14......................................................................
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3,'r^')
plt.show()

#q16......................................................................
x=["Python","Java","PHP","JavaScript","c#","C++"]
y_pos = np.arange(len(x))
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.bar(y_pos, popularity,color=['red', 'black', 'green', 'blue','yellow', 'cyan'])
plt.xticks(y_pos, x)
plt.xlabel('Languages')
plt.ylabel('popularity')
plt.title('Programming language usage')
plt.show()
