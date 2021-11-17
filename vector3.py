class vector3():
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=x
        self.y=y
        self.z=z
        
    def __str__(self):
        return"[{},{},{}]".format(str(self.x),(self.y),(self.z))
a=vector3(2,4,3)
print(a)
b=vector3(5,2,4)
print(a)
b=vector3(5,2,6)
print(b)
def add(self,b):
    c=vector3()
    c.x=self.x + b.x
    c.y=self.y + b.y
    c.z=self.z + b.z
vector3.add =add
c=a.add(b)
print(c)
    
def mul(self,s):
    return vector3(s * self.x,s*self.y,s*self.z)

vector3.mul =mul
d=a.mul(2)
print(d)

def sub(self,b):
    return self.add( b.mul(-1) )

vector3.sub = sub  
d_min_b = d.sub(b)
print(d_min_b)

    
def Dot_Product(A, B,C):
    product = 0
    # Loop for calculate Dot product
    for i in range(0, 2):
        product = product + A[i] * B[i] * C[i]
    return product
vector3.Dot_Product=Dot_Product
if __name__=='__main__':
    A = [3, -5]
    B = [2, 6]
    C = [4, 6]
    print("Dot product:")
    print(Dot_Product(A, B,C))
 
        