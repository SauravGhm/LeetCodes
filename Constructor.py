class ListNode: #defines listnode which represents a node in linked list
    def __init__(self, data = 0, next_node = None): #constructor for the listnode class,
        self.data = data
        self.next = next_node #sets the next attribute of the Listnode instance to the provided next node

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None: #Checks if the linked list is empty
            self.head = new_node #If the Linked List is empty, sets the head of the linked list to the new node
            return #Exits the method if the linked list was empty
        last_node = self.head #Initializes a variable 'last_node' to the head of the linked list
        while last_node.next is not None: #Iterates through the linked list until it reaches the last node-->
            #-->where next is none
            last_node = last_node.next #updates 'last_node' to the next node in the linked list
        last_node.next = new_node #Links the new node to the last node, effectively appending it to the end of
        #the linked list

    def display(self): #This method is used to display the elements of the linked list
        current_node = self.head #initializes the variable "current_node" to the head of the linked list
        while current_node is not None: #Iterates through the linked list
            print(current_node.data, end ="-->") #prints data of the current node followed by "-->"
            current_node =current_node.next #updates 'current_node' to the next node in the linked list
        print("None")

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()





