class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

l = Node("a",Node("b",Node("c",Node("d"))))
print(l.next.next.value)


