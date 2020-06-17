from tkinter import *
from movement import move
class board(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Chess")
        self.master.geometry()
        self.master.resizable(0,1)
        self.grid()
        self._move=move()
        #This was created to control the function <self._emp>
        #so that it does store erroneous values, when the user
        #mistakenly clicks an empty tile button 
        self._state=True
        #creating the instance variable that stores the 
        #piece and empty tile positions
        self._pieces=[]
        self._name=None
        self._tile={}
        self._count=0
        self._emptile=0
        self._p=[]
        #creating the images
        self._black=PhotoImage(file="./images/black.png")
        self._white=PhotoImage(file="./images/white.png")
        self._king=PhotoImage(file="./images/king.gif")
        self._queen=PhotoImage(file="./images/queen.gif")
        self._rookblack=PhotoImage(file="./images/rook.gif")
        self._rookwhite=PhotoImage(file="./images/rook.gif")
        self._bishopblack=PhotoImage(file="./images/bishop.gif")
        self._bishopwhite=PhotoImage(file="./images/bishop.gif")
        self._knightblack=PhotoImage(file='./images/knight.gif')
        self._knightwhite=PhotoImage(file='./images/knight.gif')
        #placing the images on the screen 
        self._kinglabel=Button(self,image=self._king,command=lambda: self._piece(self._move._kingstore,"king"))
        self._kinglabel.grid(row=7,column=3)
        self._queenlabel=Button(self,image=self._queen,command=lambda: self._piece(self._move._queenstore,"queen"))
        self._queenlabel.grid(row=7,column=4)
        self._rookblacklab=Button(self,image=self._rookblack,command=lambda: self._piece(self._move._blakrookstore))
        self._rookblacklab.grid(row=7,column=0)
        self._rookwhitelab=Button(self,image=self._rookwhite,command=lambda: self._piece(self._move._witerookstore))
        self._rookwhitelab.grid(row=7,column=7)
        self._bishopblacklab=Button(self,image=self._bishopblack,command=lambda: self._piece(self._move._blakbishopstore))
        self._bishopblacklab.grid(row=7,column=2)
        self._bishopwhitelab=Button(self,image=self._bishopwhite,command=lambda: self._piece(self._move._witebishopstore))
        self._bishopwhitelab.grid(row=7,column=5)
        self._knightblacklab=Button(self,image=self._knightblack,command=lambda: self._piece(self._move._blaknite))
        self._knightblacklab.grid(row=7,column=6)
        self._knightwhitelab=Button(self,image=self._knightwhite,command=lambda: self._piece(self._move._witenite))
        self._knightwhitelab.grid(row=7,column=1)
        for rows in range(0,7):
            for cols in range(8):
                if (rows+cols)%2==0:
                    self._tile[self._count]=[rows,cols]
                    self._imagelabel=Button(self,image=self._white,command=lambda: self._emp(self._emptile))
                    self._imagelabel.grid(row=rows,column=cols)
                    self._count+=1
                    self._emptile+=1
                else:
                    self._tile[self._count]=[rows,cols]
                    self._imagelabel=Button(self,image=self._black,command=lambda: self._emp(self._emptile))
                    self._imagelabel.grid(row=rows,column=cols)
                    self._count+=1
                    self._emptile+=1
    def _piece(self,post,name):
        #this function collects the piece position
        #and update the instance variable that
        self._pieces=post
        self._state=not self._state
        self._name=name
    def _emp(self,post):
        # this function collects an empty tile
        # and updates the instance variable
        if self._state!=True:
            self._p=self._tile.get(post)
            self._state=not self._state
            if self._name=='king':
                self._move._king(p[0],p[1])
                a=self._move._kingstore[0]
                b=self._move._kingstore[1]
                self._imagelabel=Button(self,image=self._king,command=lambda: self._piece(self._move._kingstore,"king"))
                self._imagelabel.grid(row=6,column=4)
            elif self._name=='queen':
                #self._move._queen(p[0],p[1])
                #a=self._move._queenstore[0]
                #b=self._move._queenstore[1]
                self._queenlabel=Button(self,text=self._p,command=lambda: self._piece(self._move._queenstore,"queen"))
                self._queenlabel.grid(row=6,column=4)
                print(self._p)
            else:
                pass
        else:
            pass
    def _tilereplace(self,post):
        if (post[0]+post[1])%2==0:
            self._imagelabel=Button(self,image=self._white,text=None,command=lambda: self._emp(rows,cols,self._imagelabel["text"]))
            self._imagelabel.grid(row=post[0],column=post[1])
        else:
            self._imagelabel=Button(self,image=self._black,text=None,command=lambda: self._emp(rows,cols,self._imagelabel["text"]))
            self._imagelabel.grid(row=post[0],column=post[1])
   


    
board().mainloop()