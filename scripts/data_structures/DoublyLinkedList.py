# Base Node.
class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


# Doubly Linked List Object.
class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insertAtBeginning(self, item):
        if self.head == None:
            node = Node(item, self.head, None)
            self.head = node
        else:
            node = Node(item, self.head, None)
            self.head.prev = node
            self.head = node

    
    def insertAtEnd(self, item):
        if self.head is None:
            self.head = Node(item, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(item, None, itr)

        
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

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1
    
    
    def insertAt(self, index, item):
        if index<0 or index>self.length():
            raise Exception('You have supplied an invalid index.')

        if index==0:
            self.insertAtBeginning(item)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(item, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1
    
    
    def lastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    
    def printForward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        string = ''
        while itr:
            string += str(itr.item) + ' -> '
            itr = itr.next
        print(string)

    
    def printBackward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        lastNode = self.lastNode()
        itr = lastNode
        string = ''
        while itr:
            string += itr.item + '->'
            itr = itr.prev
        print(f"Reversed linked list: {string}")


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insertValues(['a', 'concise', 'implementation of', 'doublylinkedlist'])
    ll.insertAtBeginning('This')
    ll.insertAt(1, 'is')
    ll.insertAtEnd('by ifunanyaScript')
    ll.insertAtEnd('with')
    ll.insertAtEnd('much')
    ll.insertAtEnd('love.')
    ll.printForward()
    ll.removeAt(8)
    ll.printForward()
    ll.insertValues(['love.', 'with', 'ifunanyaScript', 'from', 'list', 'linked', 'doubly', 'A'])
    ll.printBackward()

# ifunanyaScript