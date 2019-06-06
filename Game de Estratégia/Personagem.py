import pygame

class Personagem:
    def __init__(self, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vidaMax = 0
        self.vida = 0
        self.move = [0,0]
        self.podeMover = 2
    
    def movimentar(self,pos_x, pos_y,matriz): #o personagem se movimentando
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

    def receberDano(self,dano):
        self.vida -= dano
        if self.vida <= 0:
            return True
        return False

    def receberCura(self,cura):
        self.vida += cura
        if self.vida > self.vidaMax :
            self.vida = self.vidaMax

    def atributoInter(self,tela,fonte):

        text_Vida = fonte.render("Vida",1,(0,0,0))
        text_mover = fonte.render("Mover-se",1,(0,0,0))
        text_qtdmove = fonte.render(str(self.podeMover),1,(0,0,0))
        tela.blit(text_Vida,(1010,380))
        tela.blit(text_mover,(1010,400))
        tela.blit(text_qtdmove,(1100,400))

        barraVida = pygame.Surface((152,16))
        vidaBranca = pygame.Surface((150,14))
        vidaBranca.fill((255,255,255))
        vida = self.vida/self.vidaMax
        vidaVerde = pygame.Surface((150*vida,14))
        vidaVerde.fill((10,235,10))

        tela.blit(barraVida,[1050,380])
        tela.blit(vidaBranca,[1051,381])
        tela.blit(vidaVerde,[1051,381])



    
