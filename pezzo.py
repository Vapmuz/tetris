
class Pezzo:
    def __init__(self, name, color, lPositions):
        self.name = name
        self.color = color
        self.pos=lPositions
        




    def __str__(self):
      return f'{self.name}:l={len(self.pos)}'
    
    
    # data una tupla di cordinate 
    # relative (x,y) genera una tupla ruotata di 90 gradi a destra

    def rotpos(selfself,xy):  
        x,y = xy
        a=0
        if x>0 and y==0:
            return(y,-x)
            a= a+1
        if x==0 and y<0:
            return(y,x)
            a= a+1

        if x<0 and y==0:
            return(y,-x)
            a= a+1

        if x==0 and y>0:
            return(y,x)
            a= a+1




    def rotate(self):
        lRotpos= list(map(self.rotpos, self.pos ))
        self.pos= lRotpos
        return(self)
    

    # with this function I'm positionating my piece on the table based on the table start point
    def positionate(self, xy):
        x,y =xy
        x= x+10
        y= y+20
        if x>=0 and y>=0:
            return(x,y)
        else:
            return(False)





    def positionate_piece(self):
        lPosition=list(map(self.positionate(),self.pos))
        self.pos=lPosition
