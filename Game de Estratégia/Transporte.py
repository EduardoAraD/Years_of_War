import pygame

class Transporte:
    def __init__(self,pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vidaMax = 200
        self.vida = 200
        self.move = [6,6]
        self.madeira = 0
        self.minerio = 0
        self.podeMover = 2

    def receberDano(self,dano):
        self.vida -= dano
        if self.vida <= 0 :
            self.vida = 0
            return True
    
    def coletar(self, matrizRec,x,y):
        def verificarRecurso(val):
                if val[0] == "m":
                    return "madeira"
                else:
                    return "minerio"
        if matrizRec[x][y] != 0:
            val = matrizRec[x][y]
            tipo = verificarRecurso(val)
            if tipo == "madeira":
                mad = int(val[1])
                self.madeira += mad
            if tipo == "minerio":
                mine = int(val[1])
                self.minerio += mine
            matrizRec[x][y] = 0

    def descarregar(self,castelo):
        def podeDescarregar(x,y,cas):
            if cas == 0:
                if 0 <= x <= 3 and 0 <= y <= 3:
                    return True
            if cas == 1:
                if 0 <= x <= 3 and 46 <= y <= 49:
                    return True
            if cas == 2:
                if 26 <= x <= 29 and 0 <= y <= 3:
                    return True
            if cas == 3:
                if 26 <= x <= 29 and 46 <= y <= 49:
                    return True
            return False
        if podeDescarregar(self.pos_x,self.pos_y,castelo):
            md = self.madeira
            mn = self.minerio
            self.madeira = 0
            self.minerio = 0
            return md, mn
        return 0,0

    def movimentar(self,pos_x, pos_y,matriz,matrizRec): #o personagem se movimentando
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
            if matriz[x][y] == 0:
                self.coletar(matrizRec,x,y)
                return True
            return False
        limite = 0
        val = matriz[self.pos_x][self.pos_y]
        matriz[self.pos_x][self.pos_y] = 0
        mover = False
        while limite < 2:
            if limite == 0:
                if self.pos_x < pos_x:
                    if podePisar(self.pos_x+1,self.pos_y,matriz):
                        self.pos_x += 1
                        limite = 0
                        mover = True
                    else :
                        limite = 1
                else:
                    if self.pos_x > pos_x:
                        if podePisar(self.pos_x-1,self.pos_y,matriz):
                            self.pos_x -= 1
                            limite = 0
                            mover = True
                        else :
                            limite = 1
                    else :
                        limite = 1
            if limite == 1 :
                if self.pos_y < pos_y:
                    if podePisar(self.pos_x,self.pos_y+1,matriz):
                        self.pos_y += 1
                        limite = 0
                        mover = True
                    else :
                        limite = 2
                else:
                    if self.pos_y > pos_y:
                        if podePisar(self.pos_x,self.pos_y-1,matriz):
                            self.pos_y -= 1
                            limite = 0
                            mover = True
                        else :
                            limite = 2
                    else:
                        limite = 2
        matriz[self.pos_x][self.pos_y] = val
        if mover:
            self.podeMover -= 1
        return
        return

    def atributoInter(self,tela,fonte,fonte2):

        cor = (0,0,0)
        text_Transporte = fonte.render("Transporte",1,cor)
        text_Vida = fonte2.render("Vida",1,cor)
        text_mover = fonte2.render("Mover-se",1,(0,0,0))
        text_qtdmove = fonte2.render(str(self.podeMover),1,(0,0,0))
        text_madeira = fonte2.render("Madeira",1,cor)
        text_minerio = fonte2.render("Minerio",1,cor)
        text_qtdMadeira = fonte2.render(str(self.madeira),1,cor)
        text_qtdMinerio = fonte2.render(str(self.minerio),1,cor)
        tela.blit(text_Transporte,(1010,350))
        tela.blit(text_Vida,(1010,380))
        tela.blit(text_mover,(1010,400))
        tela.blit(text_qtdmove,(1100,400))
        tela.blit(text_madeira,(1010,415))
        tela.blit(text_minerio,(1010,430))
        tela.blit(text_qtdMadeira,(1100,415))
        tela.blit(text_qtdMinerio,(1100,430))

        barraVida = pygame.Surface((152,16))
        vidaBranca = pygame.Surface((150,14))
        vidaBranca.fill((255,255,255))
        vida = self.vida/self.vidaMax
        vidaVerde = pygame.Surface((150*vida,14))
        vidaVerde.fill((10,235,10))

        tela.blit(barraVida,[1050,380])
        tela.blit(vidaBranca,[1051,381])
        tela.blit(vidaVerde,[1051,381])

