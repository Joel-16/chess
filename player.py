from movement import move
class player(move):
    def __init__(self):
        move.__init__(self)
    def kill(self):
        return move.get(self)
