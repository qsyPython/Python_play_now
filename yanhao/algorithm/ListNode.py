#链表的基本形式是：1 -> 2 -> 3 -> null，反转需要变为 3 -> 2 -> 1 -> null。这里要注意：
#访问某个节点 curt.next 时，要检验 curt 是否为 null。
#要把反转后的最后一个节点（即反转前的第一个节点）指向


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

    def rverse(self,head):
        prev =None
        while head:
            temp = head.next
            prev = head
            head = temp
        return prev

    #双向链表的反转核心在于next和prev域的交换，还需要注意的是当前节点和上一个节点的递推。

class DListNode:
    def __init__(self,val):
        self.val = val
        self.prev = self.next = null

    def reverse(self,head):
        curt = None
        while head:
            curt = head
            head=curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt
