# Base Node.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        

# Linked List Object.
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, item):
        node = Node(item, self.head)
        self.head = node
        
    def insertAtEnd(self, item):
        if self.head is None:
            self.head = Node(item, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(item, None)
        
    def insertValues(self, new_list):
        self.head = None
        for item in new_list:
            self.insertAtEnd(item)
            
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def removeAt(self, index):
        if index<0 or index>=self.length():
            raise Exception('You have supplied an invalid index.')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    
    def insertAt(self, index, item):
        if index<0 or index>self.length():
            raise Exception('You have supplied an invalid index.')
        if index == 0:
            self.insertAtBeginning(item)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(item, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
            
    def insertAfterItem(self, itemAfter, itemInsert):
        if self.head is None:
            return
        
        if self.head.item == itemAfter:
            self.head.next = Node(itemInsert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.item == itemAfter:
                itr.next = Node(itemInsert, itr.next)
                break
            itr = itr.next
            
    def removeItem(self, item):
        if self.head is None:
            return
        
        if self.head.item == item:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.item == item:
                itr.next = itr.next.next
                break
            itr = itr.next
                
    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        string = ''
        while itr:
            string += str(itr.item) + '->'
            itr = itr.next
        print(string)

# ifunanyaScript