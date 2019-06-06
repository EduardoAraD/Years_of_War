from Personagem import *
import pygame

class Explorador(Personagem):
    def __init__(self, pos_x, pos_y):
        Personagem.__init__(self,pos_x,pos_y)
        self.vidaMax = 60
        self.vida = 60
        self.move = [6,6]
        
    def movimentar(self,pos_x, pos_y,matriz): #corta raiz automatico
        def possivelMovimentacao(self,pos_x,pos_y):
            def aux(x, pos):
                if pos[0] <= x and x <= pos[1]:
                    return x
                elif pos[0] <= x :
                    return pos[1]
                else:
                    return pos[0]
            ix,fx = self.pos_x - self.move[0], self.pos_x + self.move[0]
            iy,fy = self.pos_y - self.move[1], self.pos_y + self.move[1]
            pos_x = aux(pos_x,[ix,fx])
            pos_y = aux(pos_y,[iy,fy])
            return pos_x,pos_y
        pos_x,pos_y = possivelMovimentacao(self,pos_x,pos_y)

        if pos_x >= 30:
            pos_x = 29
        if pos_y >= 50 :
            pos_y = 49

        def podePisar(x,y,matriz):
            if matriz[x][y] == 0 or matriz[x][y] == 1 or matriz[x][y] == 2 or matriz[x][y] == 3:
                return True
            return False
        limite = 0
        val = matriz[self.pos_x][self.pos_y]
        mover = False
        while limite < 2:
            if limite == 0:
                if self.pos_x < pos_x:
                    if podePisar(self.pos_x+1,self.pos_y,matriz):
                        matriz[self.pos_x][self.pos_y] = 0
                        self.pos_x += 1
                        matriz[self.pos_x][self.pos_y] = val
                        limite = 0
                        mover = True
                    else :
                        limite = 1
                else:
                    if self.pos_x > pos_x:
                        if podePisar(self.pos_x-1,self.pos_y,matriz):
                            matriz[self.pos_x][self.pos_y] = 0
                            self.pos_x -= 1
                            matriz[self.pos_x][self.pos_y] = val
                            limite = 0
                            mover = True
                        else :
                            limite = 1
                    else :
                        limite = 1
            if limite == 1 :
                if self.pos_y < pos_y:
                    if podePisar(self.pos_x,self.pos_y+1,matriz):
                        matriz[self.pos_x][self.pos_y] = 0
                        self.pos_y += 1
                        matriz[self.pos_x][self.pos_y] = val
                        limite = 0
                        mover = True
                    else :
                        limite = 2
                else:
                    if self.pos_y > pos_y:
                        if podePisar(self.pos_x,self.pos_y-1,matriz):
                            matriz[self.pos_x][self.pos_y] = 0
                            self.pos_y -= 1
                            matriz[self.pos_x][self.pos_y] = val
                            limite = 0
                            mover = True
                        else :
                            limite = 2
                    else:
                        limite = 2
        matriz[self.pos_x][self.pos_y] = val
        if mover :
            self.podeMover -= 1

    def atributoInter(self,tela,fonte,fonte2):
    
        Personagem.atributoInter(self,tela,fonte2)

        cor = (0,0,0)
        text_Personagem = fonte.render("Explorador",1,cor)

        tela.blit(text_Personagem,(1010,350))

