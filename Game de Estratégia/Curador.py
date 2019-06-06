from Personagem import *
from Player import *
import pygame

class Curador(Personagem):
    def __init__(self, pos_x, pos_y):
        Personagem.__init__(self,pos_x,pos_y)
        self.vidaMax = 60
        self.vida = 60
        self.move = [3,3]
        self.zonaCura = [2,2]
        self.cura = 40 
        
    def oferecerCura(self, matriz, Players, amigo):
        ix, fx = self.pos_x - self.zonaCura[0] , self.pos_x + self.zonaCura[0] + 1
        iy, fy = self.pos_y - self.zonaCura[1] , self.pos_y + self.zonaCura[1] + 1
        for x in range(ix,fx):
            for y in range(iy,fy):
                if x >= 0 and x < 30:
                    if y >= 0 and y < 50:
                        quemRecebeCura(matriz,x,y,Players,amigo,self.cura)

    def atributoInter(self,tela,fonte,fonte2):
    
        Personagem.atributoInter(self,tela,fonte2)

        cor = (0,0,0)
        text_Personagem = fonte.render("Curador",1,cor)
        text_Cura = fonte2.render("Curar",1,cor)
        text_qtdCura = fonte2.render(str(self.cura),1,cor)

        tela.blit(text_Personagem,(1010,350))
        tela.blit(text_Cura,(1010,415))
        tela.blit(text_qtdCura,(1100,415))

def quemRecebeCura(matriz, x, y, Players,amigo,cura):
    if matriz[x][y] == "g0" or matriz[x][y] == "g1" or matriz[x][y] == "g2" or matriz[x][y] == "g3":
        num = int(matriz[x][y][1])
        if num == amigo:
            Players[num].curarAtributo(matriz,"Guerreiro",x,y,cura)
        return
    if matriz[x][y] == "a0" or matriz[x][y] == "a1" or matriz[x][y] == "a2" or matriz[x][y] == "a3":
        num = int(matriz[x][y][1])
        if num == amigo:
            Players[num].curarAtributo(matriz,"Arqueiro",x,y,cura)
        return
    if matriz[x][y] == "e0" or matriz[x][y] == "e1" or matriz[x][y] == "e2" or matriz[x][y] == "e3":
        num = int(matriz[x][y][1])
        if num == amigo:
            Players[num].curarAtributo(matriz,"Explorador",x,y,cura)
        return
    if matriz[x][y] == "c0" or matriz[x][y] == "c1" or matriz[x][y] == "c2" or matriz[x][y] == "c3":
        num = int(matriz[x][y][1])
        if num == amigo:
            Players[num].curarAtributo(matriz,"Construtor",x,y,cura)
        return
    if matriz[x][y] == "s0" or matriz[x][y] == "s1" or matriz[x][y] == "s2" or matriz[x][y] == "s3":    #ATENCAO, O CURADOR ESTA CURANDO ELE MESMO TAMBEM
        num = int(matriz[x][y][1])
        if num == amigo:
            Players[num].curarAtributo(matriz,"Curador",x,y,cura)
        return
        

        
