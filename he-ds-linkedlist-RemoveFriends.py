import sys


class Node:
    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if (self.head == None):  # To imply that if head == None
            self.head = Node (data)
            self.tail = self.head
        else:
            new_node = Node (data, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def fwd_print(self):
        to_print = []
        current = self.head
        if current == None:
            # print ("No elements")
            return False
        while (current != None):
            to_print.append (current.data)
            current = current.next
        print (*to_print)
        return True

    def delete_friend(self, count):
        DeleteFriend = False
        count = count
        currentnode = self.head

        while (count > 0):
            # print ("count1=", count)
            while (currentnode.next != None and count > 0):
                # print ("count2=", count)
                # print ("looking on {} and {}".format (currentnode.data, currentnode.next.data))
                if (currentnode.data < currentnode.next.data):
                    try:
                        # print ("Deleting1 ={}".format (currentnode.data))
                        # print ("prev and next= {},{}".format (currentnode.prev.data, currentnode.next.data))

                        # node at the middle of list
                        currentnode.prev.next = currentnode.next
                        currentnode.next.prev = currentnode.prev
                        currentnode = currentnode.prev

                    except(AttributeError):
                        # If given item is the first element of the linked list
                        # print ("Deleting2 ={}".format (currentnode.data))
                        self.head = currentnode.next
                        self.head.prev = None
                        currentnode = self.head

                    DeleteFriend = True
                    count -= 1
                else:
                    currentnode = currentnode.next

            if (DeleteFriend == False):
                # for deleting the last node
                self.tail = self.tail.prev
                self.tail.next = None
                currentnode = self.tail
                count -= 1
        return True


def main():
    t = int (sys.stdin.readline ().strip ())

    for i in range (0, t, +1):
        n, k = (map (int, sys.stdin.readline ().strip ().split (' ')))
        popularity = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

        dll = DoubleLinkedList ()
        for j in range (0, len (popularity), +1):
            dll.insert (popularity[j])

        dll.delete_friend (k)

        dll.fwd_print ()


if __name__ == "__main__":
    main ()
