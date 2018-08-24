class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

    def __del__(self):
        print("data of {} is deleted".format(self.data))


    @property #getter
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data=data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n
    
class SingleLinkedList:
    def __init__(self):
        self.head=Node()
        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add(self, data): #O(1)
        new_node=Node(data)
        new_node.next=self.head.next
        self.head.next=new_node
        self.d_size+=1
            
    def search(self, target): #O(n)
        cur=self.head.next
        while cur:
            if cur.data==target:
                return cur
            cur=cur.next #travesal 순회(자료구조에 모든데이터에 방문)
        return None

    def delete(self): #O(1)
        if self.empty():
            return

        self.head.next=self.head.next.next
        self.d_size-=1

    def traverse(self):
        cur=self.head.next
        while cur:
            yield cur
            cur=cur.next
    

def show_list(slist):
    print('data size : {}'.format(slist.size()))
    g=slist.traverse()
    for node in g:
        print(node.data, end='  ')
    print()

if __name__=="__main__":
    slist=SingleLinkedList()

    print('*'*100)
    print('데이터 삽입')
    slist.add(1)
    slist.add(2)
    slist.add(3)
    slist.add(4)
    show_list(slist)

    print('데이터 탑색')
    target=3
    res=slist.search(target)
    if res:
        print('data {} 검색 성공'.format(res.data))
    else:
        print('data {} 검색 실패'.format(target))

    res=None
    print()

    print('데이터 삭제')
    slist.delete()
    slist.delete()
    slist.delete()
    show_list(slist)

    print('*'*100)