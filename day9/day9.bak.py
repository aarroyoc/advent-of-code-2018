from collections import defaultdict,deque

PLAYERS = 30
LAST_MARBLE = 5807

#PLAYERS = 486
#LAST_MARBLE = 7083300

class List:
    def __init__(self,head):
        self.head = Node(head)
        self.size = 1

    def insert(self,n,value):
        node = Node(value)
        if n == 0:
            node.next_node = self.head
            self.head = node
        else:
            prev_n = self.get_n(n-1)
            next_n = prev_n.next_node
            node.next_node = next_n
            prev_n.next_node = node
        self.size += 1
    def remove(self,n):
        if n == 0:
            self.head = self.head.next_node
        else:
            prev_n = self.get_n(n-1)
            next_n = prev_n.next_node.next_node
            prev_n.next_node = next_n
        self.size -= 1

    def get_n(self,n):
        i = 0
        node = self.head
        while i<n:
            node = node.next_node
            i += 1
        return node

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next_node = next
    def get_value(self):
        return self.value
    def next(self):
        return self.next_node

MARBLE = None
SCORE = defaultdict(lambda: 0)
player = 0
marble = 0
current_marble_pos = 0

while marble <= LAST_MARBLE:
    if marble > 0 and marble % 23 == 0:
        SCORE[player] += marble
        SCORE[player] += MARBLE.get_n(current_marble_pos-8).value
        MARBLE.remove(current_marble_pos-8)
        current_marble_pos -= 7
    else:
        if marble == 0:
            MARBLE = List(0)
        else:
            MARBLE.insert(current_marble_pos+1,marble)
            current_marble_pos = current_marble_pos + 2
            current_marble_pos = current_marble_pos % MARBLE.size
    player += 1
    player = player % PLAYERS
    marble += 1
    if marble % 1000000 == 0:
        print("MARBLE: %d" % marble)
print(max(SCORE.values()))
