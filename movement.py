import math
rows,cols=7,3
class move(object):
    """this class represents the entire  chess pieces"""
    
    msg="Invalid move"
    def __init__(self):
        self._pawnstate=True
        self._kingstate=True
        self._blackrook=True
        self._whiterook=True
        self._blakrookstore=[7,0]
        self._witerookstore=[7,7]
        self._kingstore=[7,3]
        self._queenstore=[7,4]
        self._blakbshopstore=[7,2]
        self._witebshopstore=[7,5]
        self._witenite=[7,1]
        self._blaknite=[7,6,]
        
    def _pawn(self,rows,cols,rowboard,colboard):
        """gets the position and desired position and moves it"""
        pass
    def _castling(self,rows,cols,rowboard,colboard):
        a=rows-rowboard
        b=cols-colboard
        if rowboard==7 and colboard==0:
            rows=7
            cols=1
            self._kingstate=False
            self.blackrook(7,2)
            print("castling complete")
            return rows,cols
        if rowboard==7 and colboard==7:
            rows=7
            cols=5
            self._kingstate=False
            self.whiterook(7,4)
            print(self._kingstate)
            return rows,cols
    def king(self,rowboard,colboard):
        if (rowboard==7 and colboard==0)or (rowboard==7 and colboard==7):
            if (self._kingstate==True and self._blackrook==True) or (self._kingstate==True and self._whiterook==True):            
                self._kingstore[0],self._kingstore[1]=self._castling(self._kingstore[0],self._kingstore[1],rowboard,colboard)     
        else:
            a=self._kingstore[0]-rowboard
            b=self._kingstore[1]-colboard
            if (abs(a)>1) or (abs(b)>1):
                return move.msg
            elif (abs(a)== 1) and (abs(b)== 1) and(abs(a)==abs(b)) or (self._kingstore[0]==rowboard or self._kingstore[1]==colboard):
                self._kingstore[0]+=(-a)
                self._kingstore[1]+=(-b)
                self._kingstate=False
                return self._kingstore[0],self._kingstore[1]
                
            else:
                return move.msg
    def queen(self,rowboard,colboard):
        a=self._queenstore[0]-rowboard
        b=self._queenstore[1]-colboard
        if (abs(a) in range (8)) and (abs(b)in range (8)) and(abs(a)==abs(b)) or (self._queenstore[0]==rowboard or self._queenstore[1]==colboard):
            self._queenstore[0]+=(-a)
            self._queenstore[1]+=(-b)
            return self._queenstore[0], self._queenstore[1] 
        else:
            return move.msg
    def blackbishop(self,rowboard,colboard):
        if rowboard>7 or colboard>7:
            return move.msg
        a=self._blakbshopstore[0]-rowboard
        b=self._blakbshopstore[1]-colboard
        if (abs(a) in range (8)) and (abs(b)in range (8)) and(abs(a)==abs(b)):
            self._blakbshopstore[0]+=(-a)
            self._blakbshopstore[1]+=(-b)
            return self._blakbshopstore[0],self._blakbshopstore[1]
        else:
            return move.msg
    def whitebishop(self,rowboard,colboard):
        if rowboard>7 or colboard>7:
            return move.msg
        a=self._witebshopstore[0]-rowboard
        b=self._witebshopstore[1]-colboard
        if (abs(a) in range (8)) and (abs(b)in range (8)) and(abs(a)==abs(b)):
            self._witebshopstore[0]+=(-a)
            self._witebshopstore[1]+=(-b)
            return self._witebshopstore[0],self._witebshopstore[1]
        else:
            return move.msg
    def blackrook(self,rowboard,colboard):
        a=self._blakrookstore[0]-rowboard
        b=self._blakrookstore[1]-colboard
        if self._blakrookstore[0]==rowboard or self._blakrookstore[1]==colboard:
            self._blakrookstore[0]+=(-a)
            self._blakrookstore[1]+=(-b)
            self._blackrook=False
            return self._blakrookstore[0],self._blakrookstore[1]
        else:
             return move.msg
    def whiterook(self,rowboard,colboard):
        a=self._witerookstore[0]-rowboard
        b=self._witerookstore[1]-colboard     
        if self._witerookstore[0]==rowboard or self._witerookstore[1]==colboard:
            self._witerookstore[0]+=(-a)
            self._witerookstore[1]+=(-b)
            self._whiterook=False
            return self._witerookstore[0],self._witerookstore[1]
        else:
             return move.msg  
    def whiteknight(self,rowboard,colboard):
        a=self._witenite[0]-rowboard
        b=self._witenite[1]-colboard
        if (abs(a)<3) and (abs(b)<3):
            if colboard- rowboard==abs(-1):
                self._witenite[0]+=(-a)
                self._witenite[1]+=(-b)
                return self._witenite[0], self._witenite[1]
            else:
                return move.msg
        else:
            return move.msg
    def blackknight(self,rowboard,colboard):
        a=self._blaknite[0]-rowboard
        b=self._blaknite[1]-colboard
        if (abs(a)<3) and (abs(b)<3):
            if colboard- rowboard==abs(-1):
                self._blaknite[0]+=(-a)
                self._blaknite[1]+=(-b)
                return self._blaknite[0], self._blaknite[1]
            else:
                return move.msg
        else:
            return move.msg
    