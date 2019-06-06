from Personagem import *
from funcoesComplexas import *
import pygame

class Guerreiro(Personagem):
    def __init__(self, pos_x,pos_y):
        Personagem.__init__(self,pos_x,pos_y)
        self.vidaMax = 150
        self.vida = 150
        self.move = [4,4]
        self.dano = 20
        self.zonaAtk = [1,1]
        
    def causarDano(self,matriz,Players,amigo):
        ix, fx = self.pos_x - self.zonaAtk[0] , self.pos_x + self.zonaAtk[0] + 1
        iy, fy = self.pos_y - self.zonaAtk[1] , self.pos_y + self.zonaAtk[1] + 1
        podeAtacarCastelo = True # verificar se pode atacar o castelo
        for x in range(ix,fx):
            for y in range(iy,fy):
                if x >= 0 and x < 30:
                    if y >= 0 and y < 50:
                        podeAtacarCastelo = quemRecebeDano(matriz,x,y,Players,amigo,self.dano,podeAtacarCastelo)

    def atributoInter(self,tela,fonte,fonte2):
    
        Personagem.atributoInter(self,tela,fonte2)

        cor = (0,0,0)
        text_Personagem = fonte.render("Guerreiro",1,cor)
        text_Dano = fonte2.render("Dano",1,cor)
        text_qtdDano = fonte2.render(str(self.dano),1,cor)

        tela.blit(text_Personagem,(1010,350))
        tela.blit(text_Dano,(1010,415))
        tela.blit(text_qtdDano,(1100,415))
