class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeMngt:
    def __init__(self, data):
        self.head = Node(data)
        self.length = 1

    def __len__(self):
        return self.length

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
            self.length = 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
            self.length += 1

    def addMidAfter(self, num, data):
        node = self.head

        while node:
            if node.data == num:
                temp = node.next
                node.next = Node(data)
                node.next.next = temp
                self.length += 1
                return
            else:
                node = node.next

    def delete(self, data):
        if self.head == "":
            print("해당 값에 해당하는 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            self.length -= 1
        else:
            node = self.head
            while node:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    self.length -= 1
                    return
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print("\n")

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


linkedList = NodeMngt(0)
linkedList.desc()

# print(linkedList.head)
# linkedList.delete(0)
# print(linkedList.head)


for index in range(1, 10):
    linkedList.add(index)

linkedList.desc()
# node = linkedList.search(4)
# print(node.data)
print(linkedList.length)
linkedList.delete(4)
linkedList.desc()
print(linkedList.length)
# node = linkedList.search(4)
linkedList.addMidAfter(3, 4)
print(linkedList.length)
# linkedList.add(4)
# linkedList.desc()
# print(linkedList.length)
