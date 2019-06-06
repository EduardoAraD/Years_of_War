from Personagem import *
from Acampamento import *
from funcoesComplexas import *
import pygame

class Construtor(Personagem):
    def __init__(self, pos_x, pos_y):
        Personagem.__init__(self,pos_x,pos_y)
        self.vidaMax = 60
        self.vida = 60
        self.move = [4,4]
        self.zonaCura = [1,1]
        self.cura = 40
        
    def curarEstrutura(self, matriz,Players,amigo):
        ix, fx = self.pos_x - self.zonaCura[0] , self.pos_x + self.zonaCura[0] + 1
        iy, fy = self.pos_y - self.zonaCura[1] , self.pos_y + self.zonaCura[1] + 1
        podeCurarCastelo = True
        for x in range(ix,fx):
            for y in range(iy,fy):
                if x >= 0 and x < 30:
                    if y >= 0 and y < 50:
                        podeCurarCastelo = self.estruturaCurar(matriz,x,y,Players,amigo,podeCurarCastelo)

    def estruturaCurar(self,matriz,x,y,Players,amigo,podeCurarCastelo):
        if matriz[x][y] == "p0" or matriz[x][y] == "p1" or matriz[x][y] == "p2" or matriz[x][y] == "p3":
            num = int(matriz[x][y][1])
            if num == amigo:
                Players[num].curarAtributo(matriz,"Acampamento",x,y,self.cura)
            return podeCurarCastelo
        if matriz[x][y] == "cas1" or matriz[x][y] == "cas2" or matriz[x][y] == "cas3" or matriz[x][y] == "cas4" or matriz[x][y] == 9 :
            if podeCurarCastelo == False:
                return False
            num = identificarCastelo(x,y)
            if num == amigo:
                Players[num].castelo.receberCura(self.cura)
            return False
        return podeCurarCastelo

    def construirAcampamento(self):
        acampamento = Acampamento(self.pos_x,self.pos_y)
        return acampamento

    def atributoInter(self,tela,fonte,fonte2):
    
        Personagem.atributoInter(self,tela,fonte2)

        cor = (0,0,0)
        text_Personagem = fonte.render("Construtor",1,cor)
        text_Conserto = fonte2.render("Consertar",1,cor)
        text_qtdConsertar = fonte2.render(str(self.cura),1,cor)

        tela.blit(text_Personagem,(1010,350))
        tela.blit(text_Conserto,(1010,415))
        tela.blit(text_qtdConsertar,(1100,415))
