# Trie 자료구조를 사용하고 싶어서 선택한 문제
# 자료구조에서 cnt를 올리는 로직을 바꿔야 할 듯? 아님말구
# 노드를 따라가면서 자손이 하나만 있거나 자손이 있고 종료되는 문자열이 있는 경우 버튼 입력
# 클래스 선언이 뭔가 어색하다.

class Node(object) :
    def __init__(self,data):
        self.data = data
        self.count = 0
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.count +=1

        for c in string :
            if c not in cur.child :
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1


    def count(self,prefix):
        cur = self.head
        
        for c in prefix :
            if c not in cur.child :
                return 0
            cur = cur.child[c]

        return cur.count
    
A = Trie()
A.insert('aaa')
print(A.count)