import pygame
from Guerreiro import *
from Arqueiro import *
from Explorador import *
from Construtor import *
from Curador import *
from Acampamento import *
from Transporte import *
from Castelo import *
from funcoesComplexas import *

class Player:
    def __init__(self,pos_x,pos_y,respwn):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.respwn = respwn
        self.castelo = Castelo(pos_x,pos_y)
        self.expansao = 0
        self.qtdMadeira = 10
        self.qtdMinerio = 10
        self.ListGuerreiro = []
        self.ListArqueiro = []
        self.ListExplorador = []
        self.ListConstrutor = []
        self.ListCurador = []
        self.ListFortificacao = 0
        self.ListAcampamento = []
        self.ListTransporte =[]
        self.morreu = False

    def construir(self,carta):
        if carta == "Guerreiro" :
            if self.qtdMadeira >= 2 and self.qtdMinerio > 1:
                guerreiro = Guerreiro(self.respwn[0],self.respwn[1])
                self.ListGuerreiro.append(guerreiro)
                self.qtdMadeira -= 2
                self.qtdMinerio -= 1
                audio_respwn = pygame.mixer.Sound("Audios/respwnPersonagem.wav")
                audio_respwn.play()
                return True
            return False
        if carta == "Arqueiro" :
            if self.qtdMadeira >= 5 and self.qtdMinerio >= 1:
                arqueiro = Arqueiro(self.respwn[0],self.respwn[1])
                self.ListArqueiro.append(arqueiro)
                self.qtdMadeira -= 5
                self.qtdMinerio -= 1
                audio_respwn = pygame.mixer.Sound("Audios/respwnPersonagem.wav")
                audio_respwn.play()
                return True
            return False
        if carta == "Explorador" :
            if self.qtdMadeira >= 1:
                explorador = Explorador(self.respwn[0],self.respwn[1])
                self.ListExplorador.append(explorador)
                self.qtdMadeira -= 1
                audio_respwn = pygame.mixer.Sound("Audios/respwnPersonagem.wav")
                audio_respwn.play()
                return True
            return False
        if carta == "Construtor":
            if self.qtdMadeira >= 3 and self.qtdMinerio >= 1:
                construtor = Construtor(self.respwn[0],self.respwn[1])
                self.ListConstrutor.append(construtor)
                self.qtdMadeira -= 3
                self.qtdMinerio -= 1
                audio_respwn = pygame.mixer.Sound("Audios/respwnPersonagem.wav")
                audio_respwn.play()
                return True
            return False
        if carta == "Curador":
            if self.qtdMadeira >= 2:
                curador = Curador(self.respwn[0],self.respwn[1])
                self.ListCurador.append(curador)
                self.qtdMadeira -= 2
                audio_respwn = pygame.mixer.Sound("Audios/respwnPersonagem.wav")
                audio_respwn.play()
                return True
            return False
        if carta == "Transporte":
            if self.qtdMadeira >= 5 and self.qtdMinerio >= 2:
                tranporte = Transporte(self.respwn[0],self.respwn[1])
                self.ListTransporte.append(tranporte)
                self.qtdMadeira -= 5
                self.qtdMinerio -= 2
                audio_respwn = pygame.mixer.Sound("Audios/ConstruirTrans.wav")
                audio_respwn.play()
                return True
            return False
                

    def fortificarCarta(self,carta,x,y):
        if self.qtdMadeira >= 20 and self.qtdMinerio >= 10:
            if carta == "Fortificacao" :
                self.castelo.fortificar()
                self.qtdMadeira -= 20
                self.qtdMinerio -= 10
            if carta == "Acampamento":
                if self.qtdMadeira >= 20 and self.qtdMinerio >= 10:
                    for i in range(0,len(self.ListAcampamento)):
                        if self.ListAcampamento[i].pos_x == x and self.ListAcampamento[i].pos_y == y:
                            self.ListAcampamento[i].fortificar()
                            self.qtdMadeira -= 20
                            self.qtdMinerio -= 10
            audio_fortificar = pygame.mixer.Sound("Audios/fortificar.wav")
            audio_fortificar.play()
            

    def construirAcampamento(self,construtor):
        if self.qtdMadeira >= 25 and self.qtdMinerio >= 5:
            x = construtor.pos_x
            y = construtor.pos_y
            self.ListConstrutor.remove(construtor)
            acampamento = Acampamento(x,y)
            area = acampamento.defExpansao(self.pos_x,self.pos_y)
            if area > self.expansao :
                self.expansao = area
            self.ListAcampamento.append(acampamento)
            self.castelo.vidaMax += acampamento.vidaMax
            self.castelo.vida += acampamento.vida
            self.qtdMadeira -= 25
            self.qtdMinerio -= 5
            audio_acampamento = pygame.mixer.Sound("Audios/ConstruirTorre.wav")
            audio_acampamento.play()
            return True
        return False
        
    def pos_respwn(self,matriz):
            x,y = self.respwn
            if matriz[x][y] == 0:
                return
            else :
                num = identificarCastelo(self.pos_x,self.pos_y)
                if num == 0:
                    for i in range(0,4):
                        if matriz[i][3] == 0:
                            self.respwn = [i,3]
                            return
                        if matriz[3][i] == 0:
                            self.respwn = [3,i]
                            return
                elif num == 1:
                    for i in range(0,4):
                        if matriz[i][46] == 0:
                            self.respwn = [i,46]
                            return
                        if matriz[3][46+i] == 0:
                            self.respwn = [3,46+i]
                            return
                elif num == 2:
                    for i in range(0,4):
                        if matriz[26+i][3] == 0:
                            self.respwn = [26+i,3]
                            return
                        if matriz[26][i] == 0:
                            self.respwn = [26,i]
                            return
                elif num == 3:
                    for i in range(0,4):
                        if matriz[26+i][46] == 0:
                            self.respwn = [26+i,46]
                            return
                        if matriz[26][46+i] == 0:
                            self.respwn = [26,46+i]
                            return
                            
    def atacar(self,matriz,Players,amigo):
        tot = len(self.ListGuerreiro) + len(self.ListArqueiro)
        if tot > 0:
            audio_ataque = pygame.mixer.Sound("Audios/Ataque.wav")
            audio_ataque.play()
            
        for x in range(0,len(self.ListGuerreiro)):
            self.ListGuerreiro[x].causarDano(matriz,Players,amigo)
            
        for y in range(0,len(self.ListArqueiro)):
            self.ListArqueiro[y].causarDano(matriz,Players,amigo)
            

    def curar(self,matriz,Players,amigo):
        for i in range(0,len(self.ListCurador)):
            self.ListCurador[i].oferecerCura(matriz,Players,amigo)
        for i in range(0,len(self.ListConstrutor)):
            self.ListConstrutor[i].curarEstrutura(matriz,Players,amigo)

    def descarregar(self,castelo):
        for i in range(0,len(self.ListTransporte)):
            madeira , minerio = self.ListTransporte[i].descarregar(castelo)
            self.qtdMadeira += madeira
            self.qtdMinerio += minerio

    def resete(self):
        for i in range(0,len(self.ListGuerreiro)):
            self.ListGuerreiro[i].podeMover = 2
        for i in range(0,len(self.ListArqueiro)):
            self.ListArqueiro[i].podeMover = 2
        for i in range(0,len(self.ListExplorador)):
            self.ListExplorador[i].podeMover = 2
        for i in range(0,len(self.ListConstrutor)):
            self.ListConstrutor[i].podeMover = 2
        for i in range(0,len(self.ListCurador)):
            self.ListCurador[i].podeMover = 2
        for i in range(0,len(self.ListTransporte)):
            self.ListTransporte[i].podeMover = 2
        self.qtdMadeira += 1
        self.qtdMinerio += 1

    def curarAtributo(self,matriz,personagem,x,y,cura):
        if personagem == "Guerreiro":
            for i in range(0,len(self.ListGuerreiro)):
                if self.ListGuerreiro[i].pos_x == x and self.ListGuerreiro[i].pos_y == y:
                    self.ListGuerreiro[i].receberCura(cura)
        if personagem == "Arqueiro":
            for i in range(0,len(self.ListArqueiro)):
                if self.ListArqueiro[i].pos_x == x and self.ListArqueiro[i].pos_y == y:
                    self.ListArqueiro[i].receberCura(cura)
        if personagem == "Explorador":
            for i in range(0,len(self.ListExplorador)):
                if self.ListExplorador[i].pos_x == x and self.ListExplorador[i].pos_y == y:
                    self.ListExplorador[i].receberCura(cura)
        if personagem == "Construtor":
            for i in range(0,len(self.ListConstrutor)):
                if self.ListConstrutor[i].pos_x == x and self.ListConstrutor[i].pos_y == y:
                    self.ListConstrutor[i].receberCura(cura)
        if personagem == "Curador":
            for i in range(0,len(self.ListCurador)):
                if self.ListCurador[i].pos_x == x and self.ListCurador[i].pos_y == y:
                    self.ListCurador[i].receberCura(cura)

        if personagem == "Acampamento":
            for i in range(0,len(self.ListAcampamento)):
                if self.ListAcampamento[i].pos_x == x and self.ListAcampamento[i].pos_y == y:
                    self.ListAcampamento[i].receberCura(cura)
            
    def damage(self,matriz,personagem,x,y,dano): 
        if personagem == "Guerreiro":
            for i in range(0,len(self.ListGuerreiro)):
                if self.ListGuerreiro[i].pos_x == x and self.ListGuerreiro[i].pos_y == y:
                    morreu = self.ListGuerreiro[i].receberDano(dano)
                    if morreu:
                        self.ListGuerreiro.remove(self.ListGuerreiro[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Arqueiro":
            for i in range(0,len(self.ListArqueiro)):
                if self.ListArqueiro[i].pos_x == x and self.ListArqueiro[i].pos_y == y:
                    morreu = self.ListArqueiro[i].receberDano(dano)
                    if morreu:
                        self.ListArqueiro.remove(self.ListArqueiro[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Explorador":
            for i in range(0,len(self.ListExplorador)):
                if self.ListExplorador[i].pos_x == x and self.ListExplorador[i].pos_y == y:
                    morreu = self.ListExplorador[i].receberDano(dano)
                    if morreu:
                        self.ListExplorador.remove(self.ListExplorador[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Construtor":
            for i in range(0,len(self.ListConstrutor)):
                if self.ListConstrutor[i].pos_x == x and self.ListConstrutor[i].pos_y == y:
                    morreu = self.ListConstrutor[i].receberDano(dano)
                    if morreu:
                        self.ListConstrutor.remove(self.ListConstrutor[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Curador":
            for i in range(0,len(self.ListCurador)):
                if self.ListCurador[i].pos_x == x and self.ListCurador[i].pos_y == y:
                    morreu = self.ListCurador[i].receberDano(dano)
                    if morreu:
                        self.ListCurador.remove(self.ListCurador[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Transporte":
            for i in range(0,len(self.ListTransporte)):
                if self.ListTransporte[i].pos_x == x and self.ListTransporte[i].pos_y == y:
                    morreu = self.ListTransporte[i].receberDano(dano)
                    if morreu:
                        self.ListTransporte.remove(self.ListTransporte[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/morrer.wav")
                        audio_morrer.play()
                        return
        if personagem == "Acampamento":
            for i in range(0,len(self.ListAcampamento)):
                if self.ListAcampamento[i].pos_x == x and self.ListAcampamento[i].pos_y == y:
                    morreu = self.ListAcampamento[i].receberDano(dano)
                    if morreu:
                        self.ListAcampamento.remove(self.ListAcampamento[i])
                        matriz[x][y] = 0
                        audio_morrer = pygame.mixer.Sound("Audios/DestruirTorre.wav")
                        audio_morrer.play()
                        return
            
                        
    def derrota(self,matriz):
        if self.morreu == True:
            return
        for i in range(0,len(self.ListGuerreiro)):
            x = self.ListGuerreiro[i].pos_x
            y = self.ListGuerreiro[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListArqueiro)):
            x = self.ListArqueiro[i].pos_x
            y = self.ListArqueiro[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListExplorador)):
            x = self.ListExplorador[i].pos_x
            y = self.ListExplorador[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListConstrutor)):
            x = self.ListConstrutor[i].pos_x
            y = self.ListConstrutor[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListCurador)):
            x = self.ListCurador[i].pos_x
            y = self.ListCurador[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListAcampamento)):
            x = self.ListAcampamento[i].pos_x
            y = self.ListAcampamento[i].pos_y
            matriz[x][y] = 0
        for i in range(0,len(self.ListTransporte)):
            x = self.ListTransporte[i].pos_x
            y = self.ListTransporte[i].pos_y
            matriz[x][y] = 0
        self.morreu = True
        matriz[self.pos_x][self.pos_y] = "casdestroy"
        audio_destruir = pygame.mixer.Sound("Audios/DestruirCastelo.wav")
        audio_destruir.play()
        return

        
