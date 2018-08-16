class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def preorder(self, n):
        # 전위순회
        if n is not None:
            # 맨 먼저 노드 방문
            print(str(n.key), '', end='')
            # 왼쪽 서브트리 방문 후, 오른쪽 서브트리 방문
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        # 중위 순회
        if n is not None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), '', end='')

            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        # 후위 순회
        if n is not None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), '', end='')

    def get(self, key):
        # 탐색연산
        # 탐색은 루트에서 시작
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n is None:
            # 탐색 실패
            return None
        if n.key > k:
            # k가 노드의 key보다 작으면 왼쪽 서브트리 탐색
            return self.get_item(n.left, k)
        elif n.key < k:
            # k가 노드의 key보다 크면 오른쪽 서브트리 탐색
            return self.get_item(n.right, k)
        else:
            # 탐색 성공
            return n.value

    def put(self, key, value):
        # 삽입연산
        # 탐색연산과 유사하데, 마지막 None을 반환하는 대신, 삽입하고자 하는 key, value 를 갖는 새로운 노드를 생성
        # 그리고 새노드를 부모노드와 연결
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            # 이미 존재하는 key의 경우 value만 갱신
            n.value = value
        # 부모노드와 연결하기 위해 노드 n을 리턴
        return n

    def min(self):
        # 최솟값 가진 노드 찾기
        # 루트로부터 왼쪽자식을 따라 내려가며, None을 만났을 때 None의 부모노드가 가진 Key가 최솟값
        if self.root is None:
            return None
        return self.minmum(self.root)

    def minimum(self, n):
        if n.left is None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        # 최소값 삭제
        # 최솟값을 가진 노드 n을 찾아낸 뒤, n의 부모노드 p와 n의 오른쪽자식 c를 연결
        if self.root is None:
            return None
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, key):
        # 임의의 키를 가진 노드를 삭제하는 연산
        # get()탐색 과정과 같이 삭제할 노드 찾은 후, 이진탐색트리 조건을 만족하도록 삭제된 노드를 부모노드와 자식노드들 연결해야함
        # 2. 자식이 하나인 경우
        # 3. 자식이 둘인 경우
        self.root = self.del_node(self.root, key)

    def del_node(self, n, k):
        # 삭제되는 노드가 자식이 없는 경
        if n is None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)

        elif n.key < k:
            n.right = self.del_node(n.right, k)
        else:
            # 자식이 하나인 경우
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right
            # 자식이 둘인 경우
            # 1. 왼쪽에서 가장 큰 노드 찾기
            # 2. 오른쪽에서 가장 작은 값찾기 <- 이 방법 사용

            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left

        return n


if __name__ == '__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')

    print('전위순회: ', end='')
    t.preorder(t.root)
    print()
    print('중위순회: ', end='')
    t.inorder(t.root)

    print('\n250 ', t.get(250))

    t.delete(200)

    print('200 삭제 후: ')

    print('전위순회: ', end='')
    t.preorder(t.root)
    print()
    print('중위순회: ', end='')
    t.inorder(t.root)
