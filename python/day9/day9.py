from collections import defaultdict
        

class Marble:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        if self.left == None:
            self.left = self
        if self.right == None:
            self.right = self

def day9(PLAYERS,LAST_MARBLE):
    SCORE = defaultdict(lambda: 0)
    player = 0
    marble = 0
    current_marble_pos = 0
    current_marble = None

    while marble <= LAST_MARBLE:
        if marble > 0 and marble % 23 == 0:
            SCORE[player] += marble
            pivote = current_marble.left.left.left.left.left.left.left
            SCORE[player] += pivote.value
            pivote.left.right = pivote.right
            pivote.right.left = pivote.left
            current_marble = pivote.right

        else:
            if current_marble == None:
                current_marble = Marble(marble)
            else:
                current_marble = Marble(marble,current_marble.right,current_marble.right.right)
                current_marble.left.right = current_marble
                current_marble.right.left = current_marble
        player += 1
        player = player % PLAYERS
        marble += 1
    return max(SCORE.values())