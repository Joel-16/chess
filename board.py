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
        self._a0=Button(self,image=self._white,text=str("00"),command=lambda: self._emp(self._a0["text"]))
        self._a0.grid(row=0,column=0)
        self._a1=Button(self,image=self._black,text=str("01"),command=lambda: self._emp(self._a1["text"]))
        self._a1.grid(row=0,column=1)
        self._a2=Button(self,image=self._white,text=str("02"),command=lambda: self._emp(self._a2["text"]))
        self._a2.grid(row=0,column=2)
        self._a3=Button(self,image=self._black,text=str("03"),command=lambda: self._emp(self._a3["text"]))
        self._a3.grid(row=0,column=3)
        self._a4=Button(self,image=self._white,text=str("04"),command=lambda: self._emp(self._a4["text"]))
        self._a4.grid(row=0,column=4)
        self._a5=Button(self,image=self._black,text=str("05"),command=lambda: self._emp(self._a5["text"]))
        self._a5.grid(row=0,column=5)
        self._a6=Button(self,image=self._white,text=str("06"),command=lambda: self._emp(self._a6["text"]))
        self._a6.grid(row=0,column=6)
        self._a7=Button(self,image=self._black,text=str("07"),command=lambda: self._emp(self._a7["text"]))
        self._a7.grid(row=0,column=7)
        self._b0=Button(self,image=self._black,text=str("10"),command=lambda: self._emp(self._b0["text"]))
        self._b0.grid(row=1,column=0)
        self._b1=Button(self,image=self._white,text=str("11"),command=lambda: self._emp(self._b1["text"]))
        self._b1.grid(row=1,column=1)
        self._b2=Button(self,image=self._black,text=str("12"),command=lambda: self._emp(self._b2["text"]))
        self._b2.grid(row=1,column=2)
        self._b3=Button(self,image=self._white,text=str("13"),command=lambda: self._emp(self._b3["text"]))
        self._b3.grid(row=1,column=3)
        self._b4=Button(self,image=self._black,text=str("14"),command=lambda: self._emp(self._b4["text"]))
        self._b4.grid(row=1,column=4)
        self._b5=Button(self,image=self._white,text=str("15"),command=lambda: self._emp(self._b5["text"]))
        self._b5.grid(row=1,column=5)
        self._b6=Button(self,image=self._black,text=str("16"),command=lambda: self._emp(self._b6["text"]))
        self._b6.grid(row=1,column=6)
        self._b7=Button(self,image=self._white,text=str("17"),command=lambda: self._emp(self._b7["text"]))
        self._b7.grid(row=1,column=7)
        self._c0=Button(self,image=self._white,text=str("20"),command=lambda: self._emp(self._c0["text"]))
        self._c0.grid(row=2,column=0)
        self._c1=Button(self,image=self._black,text=str("21"),command=lambda: self._emp(self._c1["text"]))
        self._c1.grid(row=2,column=1)
        self._c2=Button(self,image=self._white,text=str("22"),command=lambda: self._emp(self._c2["text"]))
        self._c2.grid(row=2,column=2)
        self._c3=Button(self,image=self._black,text=str("23"),command=lambda: self._emp(self._c3["text"]))
        self._c3.grid(row=2,column=3)
        self._c4=Button(self,image=self._white,text=str("24"),command=lambda: self._emp(self._c4["text"]))
        self._c4.grid(row=2,column=4)
        self._c5=Button(self,image=self._black,text=str("25"),command=lambda: self._emp(self._c5["text"]))
        self._c5.grid(row=2,column=5)
        self._c6=Button(self,image=self._white,text=str("26"),command=lambda: self._emp(self._c6["text"]))
        self._c6.grid(row=2,column=6)
        self._c7=Button(self,image=self._black,text=str("27"),command=lambda: self._emp(self._c7["text"]))
        self._c7.grid(row=2,column=7)
        self._d0=Button(self,image=self._black,text=str("30"),command=lambda: self._emp(self._d0["text"]))
        self._d0.grid(row=3,column=0)
        self._d1=Button(self,image=self._white,text=str("31"),command=lambda: self._emp(self._d1["text"]))
        self._d1.grid(row=3,column=1)
        self._d2=Button(self,image=self._black,text=str("32"),command=lambda: self._emp(self._d2["text"]))
        self._d2.grid(row=3,column=2)
        self._d3=Button(self,image=self._white,text=str("33"),command=lambda: self._emp(self._d3["text"]))
        self._d3.grid(row=3,column=3)
        self._d4=Button(self,image=self._black,text=str("34"),command=lambda: self._emp(self._d4["text"]))
        self._d4.grid(row=3,column=4)
        self._d5=Button(self,image=self._white,text=str("35"),command=lambda: self._emp(self._d5["text"]))
        self._d5.grid(row=3,column=5)
        self._d6=Button(self,image=self._black,text=str("36"),command=lambda: self._emp(self._d6["text"]))
        self._d6.grid(row=3,column=6)
        self._d7=Button(self,image=self._white,text=str("37"),command=lambda: self._emp(self._d7["text"]))
        self._d7.grid(row=3,column=7)
        self._e0=Button(self,image=self._white,text=str("40"),command=lambda: self._emp(self._e0["text"]))
        self._e0.grid(row=4,column=0)
        self._e1=Button(self,image=self._black,text=str("41"),command=lambda: self._emp(self._e1["text"]))
        self._e1.grid(row=4,column=1)
        self._e2=Button(self,image=self._white,text=str("42"),command=lambda: self._emp(self._e2["text"]))
        self._e2.grid(row=4,column=2)
        self._e3=Button(self,image=self._black,text=str("43"),command=lambda: self._emp(self._e3["text"]))
        self._e3.grid(row=4,column=3)
        self._e4=Button(self,image=self._white,text=str("44"),command=lambda: self._emp(self._e4["text"]))
        self._e4.grid(row=4,column=4)
        self._e5=Button(self,image=self._black,text=str("45"),command=lambda: self._emp(self._e5["text"]))
        self._e5.grid(row=4,column=5)
        self._e6=Button(self,image=self._white,text=str("46"),command=lambda: self._emp(self._e6["text"]))
        self._e6.grid(row=4,column=6)
        self._e7=Button(self,image=self._black,text=str("47"),command=lambda: self._emp(self._e7["text"]))
        self._e7.grid(row=4,column=7)
        self._f0=Button(self,image=self._black,text=str("50"),command=lambda: self._emp(self._f0["text"]))
        self._f0.grid(row=5,column=0)
        self._f1=Button(self,image=self._white,text=str("51"),command=lambda: self._emp(self._f1["text"]))
        self._f1.grid(row=5,column=1)
        self._f2=Button(self,image=self._black,text=str("52"),command=lambda: self._emp(self._f2["text"]))
        self._f2.grid(row=5,column=2)
        self._f3=Button(self,image=self._white,text=str("53"),command=lambda: self._emp(self._f3["text"]))
        self._f3.grid(row=5,column=3)
        self._f4=Button(self,image=self._black,text=str("54"),command=lambda: self._emp(self._f4["text"]))
        self._f4.grid(row=5,column=4)
        self._f5=Button(self,image=self._white,text=str("55"),command=lambda: self._emp(self._f5["text"]))
        self._f5.grid(row=5,column=5)
        self._f6=Button(self,image=self._black,text=str("56"),command=lambda: self._emp(self._f6["text"]))
        self._f6.grid(row=5,column=6)
        self._f7=Button(self,image=self._white,text=str("57"),command=lambda: self._emp(self._f7["text"]))
        self._f7.grid(row=5,column=7)
        self._g0=Button(self,image=self._white,text=str("60"),command=lambda: self._emp(self._g0["text"]))
        self._g0.grid(row=6,column=0)
        self._g1=Button(self,image=self._black,text=str("61"),command=lambda: self._emp(self._g1["text"]))
        self._g1.grid(row=6,column=1)
        self._g2=Button(self,image=self._white,text=str("62"),command=lambda: self._emp(self._g2["text"]))
        self._g2.grid(row=6,column=2)
        self._g3=Button(self,image=self._black,text=str("63"),command=lambda: self._emp(self._g3["text"]))
        self._g3.grid(row=6,column=3)
        self._g4=Button(self,image=self._white,text=str("64"),command=lambda: self._emp(self._g4["text"]))
        self._g4.grid(row=6,column=4)
        self._g5=Button(self,image=self._black,text=str("65"),command=lambda: self._emp(self._g5["text"]))
        self._g5.grid(row=6,column=5)
        self._g6=Button(self,image=self._white,text=str("66"),command=lambda: self._emp(self._g6["text"]))
        self._g6.grid(row=6,column=6)
        self._g7=Button(self,image=self._black,text=str("67"),command=lambda: self._emp(self._g7["text"]))
        self._g7.grid(row=6,column=7)

        
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
            #self._p=self._tile.get(post,post)
            self._state=not self._state
            if self._name=='king':
                a,b=self._move.king(int(post[0]),int(post[1]))
                self._imagelabel=Button(self,image=self._king,command=lambda: self._piece(self._move._kingstore,"king"))
                self._imagelabel.grid(row=a,column=b)
            elif self._name=='queen':
                a,b=self._move.queen(int(post[0]),int(post[1]))
                self._queenlabel=Button(self,image=self._queen,command=lambda: self._piece(self._move._queenstore,"queen"))
                self._queenlabel.grid(row=a,column=b)
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