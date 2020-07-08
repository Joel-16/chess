from threading import Thread,Condition
class blackplayer(Thread):
    def __init__(self):
        Thread.__init__(self,name="black")
    def kill(self):



        
class whiteplayer(Thread):
    def __init__(self):
        Thread.__init__(self,name="white")
        
    def run(self):
    

