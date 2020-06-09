from tkinter import *
from movement import move
class board(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Chess")
        self.master.geometry()
        self.master.resizable(0,1)
        self.grid()
        #This was created to control the function <self._emp>
        #so that it does store erroneous values, when the user
        #mistakenly clicks an empty tile button 
        self._state=True
        #creating the instance variable that stores the 
        #piece and empty tile positions
        self._piece=[]
        self._emptile=[]
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
        self._kinglabel=Button(self,image=self._king,text="king",command=lambda: self._piece([7,3,self._kinglabel["text"]]))
        self._kinglabel.grid(row=7,column=3)
        self._queenlabel=Button(self,image=self._queen,text="queen",command=lambda: self._piece([7,4,self._queenlabel["text"]]))
        self._queenlabel.grid(row=7,column=4)
        self._rookblacklab=Button(self,image=self._rookblack,text="blackrook",command=lambda: self._piece([7,0,self._rookblacklab["text"]]))
        self._rookblacklab.grid(row=7,column=0)
        self._rookwhitelab=Button(self,image=self._rookwhite,text="whiterook",command=lambda: self._piece([7,7,self._rookwhitelab["text"]]))
        self._rookwhitelab.grid(row=7,column=7)
        self._bishopblacklab=Button(self,image=self._bishopblack,text="blackbishop",command=lambda: self._piece([7,2,self._bishopblacklab["text"]]))
        self._bishopblacklab.grid(row=7,column=2)
        self._bishopwhitelab=Button(self,image=self._bishopwhite,text="whitebishop",command=lambda: self._piece([7,5,self._bishopwhitelab["text"]]))
        self._bishopwhitelab.grid(row=7,column=5)
        self._knightblacklab=Button(self,image=self._knightblack,text="blackknight",command=lambda: self._piece([7,6,self._knightblacklab["text"]]))
        self._knightblacklab.grid(row=7,column=6)
        self._knightwhitelab=Button(self,image=self._knightwhite,text="whiteknight",command=lambda: self._piece([7,1,self._knightwhitelab["text"]]))
        self._knightwhitelab.grid(row=7,column=1)
        for rows in range(0,6):
            for cols in range(8):
                if (rows+cols)%2==0:
                    self._imagelabel=Button(self,image=self._white,text=None,command=lambda: self._emp([rows,cols,self._imagelabel["text"]]))
                    self._imagelabel.grid(row=rows,column=cols)
                else:
                    self._imagelabel=Button(self,image=self._black,text=None,command=lambda: self._emp([rows,cols,self._imagelabel["text"]]))
                    self._imagelabel.grid(row=rows,column=cols)
    def _piece(self,post):
            self._piece=post
            self._state=not self._state
    def _emp(self,tile):
        if self._state!=True:
            self._emptile=tile
            self._state=not self._state
            self._a=Label(self,text=str(tile))
            self._a.grid(row=8,column=0)
            #return tile[0],tile[1]
        else:
            pass
    def _tilereplace(self,post):
        if (post[0]+post[1])%2==0:
            self._imagelabel=Button(self,image=self._white,text=None,command=lambda: self._emp([rows,cols,self._imagelabel["text"]]))
            self._imagelabel.grid(row=post[0],column=post[1])
        else:
            self._imagelabel=Button(self,image=self._black,text=None,command=lambda: self._emp([rows,cols,self._imagelabel["text"]]))
            self._imagelabel.grid(row=post[0],column=post[1])


        
def main():
    board().mainloop()
if __name__=="__main__":
    main()
