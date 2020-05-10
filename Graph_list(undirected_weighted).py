class node:
    def __init__(self,data,weight=0):
        self.data=data
        self.next=None
        self.weight=weight
class lList:
    def __init__(self):
        self.head=None
    def add(self,key,weight):
        if self.head==None:
            self.head=node(key,weight)
        else:
            if self.search(key)==-1:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=node(key,weight)
            else:
                return 
    def search(self,key):
        if self.head==None:
            return -1
        else:
            temp=self.head
            while temp!=None and temp.data!=key:
                temp=temp.next
            if temp!=None:
                if temp.data==key:
                    return 0
            else:
                    return -1
    def delete(self,key):
        if self.head==None:
            return
        else:
            temp=self.head
            while temp.next!=None and temp.next.data!=key:
                temp=temp.next
            if temp.next.data==key:
                temp.next=temp.next.next
                return
    def Lprint(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,"+",temp.weight,end="  ")
                temp=temp.next
            print("  ")
class Graph:
    def __init__(self,vertices):
        self.list1=vertices
        self.arr=[None]*len(vertices)
        for i in range(len(self.arr)):
            self.arr[i]=lList()
            self.arr[i].add(vertices[i],0)
    def addEdge(self,u,v,weight):
        i=self.list1.index(u)
        j=self.list1.index(v)
        self.arr[i].add(v,weight)
        self.arr[j].add(u,weight)
    def deleteEdge(self,u,v):
        i=self.list1.index(u)
        j=self.list1.index(v)
        self.arr[i].delete(v)
        self.arr[j].delete(u)
    def Gprint(self):
        for i in range(len(self.arr)):
            self.arr[i].Lprint()

g1=Graph([7,8,9,6,5,4])
g1.addEdge(7,8,2)
g1.addEdge(8,7,3)
g1.addEdge(9,8,8)
g1.addEdge(6,5,1)
g1.addEdge(7,9,7)
g1.addEdge(7,5,3)
g1.addEdge(4,8,1)
g1.addEdge(6,8,2)
g1.addEdge(6,4,6)
g1.deleteEdge(6,5)
g1.deleteEdge(5,7)
print("vertices + Edge-weight")
g1.Gprint()