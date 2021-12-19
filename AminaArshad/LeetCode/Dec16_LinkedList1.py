#237. Delete Node in a Linked List: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

class Node():
    def __init__(self):
        self.data = None
        self.next = None
        
def push(head_ref, new_data):
 
    # allocate node
    new_node = Node()
 
    # put in the data
    new_node.data = new_data
 
    # link the old list off the new node
    new_node.next = head_ref
 
    # move the head to point to the new node
    head_ref = new_node
 
    return head_ref
 
 
def printList(head):
    temp = head
    while(temp != None):
        print(temp.data, end=' ')
        temp = temp.next
 
 
def deleteNode(node_ptr):
    temp = node_ptr.next
    node_ptr.data = temp.data
    node_ptr.next = temp.next
 
 
# Driver code
if __name__ == '__main__':
 
    # Start with the empty list
    head = None
 
    # Use push() to construct below list
    # 1->12->1->4->1
    head = push(head, 1)
    head = push(head, 4)
    head = push(head, 1)
    head = push(head, 12)
    head = push(head, 1)
 
    print("Before deleting ")
    printList(head)
 
    # I'm deleting the head itself.
    # You can check for more cases
    deleteNode(head)
 
    print("\nAfter deleting")
    printList(head)
 