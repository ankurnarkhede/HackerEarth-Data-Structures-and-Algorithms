
import sys


class Node:
    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if (self.head == None):  # To imply that if head == None
            self.head = Node (data)
            self.tail = self.head
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node (data, None, current)
            self.tail = current.next


    def fwd_print(self):
        to_print=[]
        current = self.head
        if current == None:
            print ("No elements")
            return False
        while (current != None):
            to_print.append(current.data)
            current = current.next
        print(*to_print)
        return True



    def delete_friend(self):
        DeleteFriend = False

        currentnode = self.head

        while currentnode.next != None:
            if (currentnode.data < currentnode.next.data):
                # print("working on {} and {}".format(currentnode.data,currentnode.next.data))
                try:
                    # print("Deleting1 ={}".format(currentnode.data))
                    # print("prev and next= {},{}".format(currentnode.prev.data,currentnode.next.data))
                    currentnode.prev.next=currentnode.next
                    currentnode.next.prev = currentnode.prev

                except(AttributeError):
                    # If given item is the first element of the linked list
                    # print("Deleting2 ={}".format(currentnode.data))
                    self.head = currentnode.next
                    self.head.prev = None

                DeleteFriend=True
                break
            currentnode = currentnode.next


        if(DeleteFriend == False):
            # for deleting the last node
            self.tail = self.tail.prev
            self.tail.next = None
        return True




def main():

    t = int (sys.stdin.readline ().strip ())

    for i in range(0,t,+1):
        n, k = (map (int, sys.stdin.readline ().strip ().split (' ')))
        popularity = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

        dll = DoubleLinkedList ()
        for j in range(0,len(popularity),+1):
            dll.insert(popularity[j])

        # dll.fwd_print()
        for j in range(0, k, +1):
            dll.delete_friend()

        dll.fwd_print ()



if __name__ == "__main__":
    main ()

