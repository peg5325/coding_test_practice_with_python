class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class NodeMngt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == "":
            self.head = Node(data)
            self.tail = self.haed
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True

        node = self.tail
        while before_data != node.data:
            node = node.prev
            if node.prev == None:
                return False

        new = Node(data)
        before_new = node.prev
        before_new.next = new
        new.prev = before_new
        new.next = node
        node.prev = new

        return True

    def search_from_head(self, data):
        if self.head == None:
            print("해당하는 노드가 없습니다.")
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        print("검색하신 노드가 없습니다.")
        return False

    def search_from_tail(self, data):
        if self.head == None:
            print("해당하는 노드가 없습니다.")
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        print("검색하신 노드가 없습니다.")
        return False

    def delete(self, data):
        if self.head == None:
            print("해당하는 노드가 없습니다.")
            return False

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node:
                if node.data == data:
                    temp = node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    del temp
                    return
                else:
                    node = node.next
            print("검색하신 노드가 없습니다.")

    def desc(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next


double_linked_list = NodeMngt(0)
for index in range(1, 10):
    double_linked_list.insert(index)
double_linked_list.desc()

print("\n")

double_linked_list.insert_before(3.5, 4)
double_linked_list.desc()

print("\n")

double_linked_list.delete(2)
double_linked_list.desc()
