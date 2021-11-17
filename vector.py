class vector():
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
        
    def __str__(self):
        return"[{},{}]".format(str(self.x),(self.y))
a=vector(2,4)
print(a)
b=vector(5,2)
print(a)
b=vector(5,2)
print(b)
def add(self,b):
    c=vector()
    c.x=self.x + b.x
    c.y=self.y + b.y
vector.add =add
c=a.add(b)
print(c)
    
def mul(self,s):
    return vector(s * self.x,s*self.y)

vector.mul =mul
d=a.mul(2)
print(d)

def sub(self,b):
    return self.add( b.mul(-1) )

vector.sub = sub  
d_min_b = d.sub(b)
print(d_min_b)



    
def Dot_Product(A, B):
    product = 0
    # Loop for calculate dot product
    for i in range(0, 2):
        product = product + A[i] * B[i]
 
    return product
vector.Dot_Product=Dot_Product
if __name__=='__main__':
    A = [3, -5]
    B = [2, 6]
    print("Dot product:")
    print(Dot_Product(A, B))
 
        