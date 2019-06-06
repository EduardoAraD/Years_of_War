import pygame
from Player import *
from funcoesComplexas import *

def passarTempo(tempo, limTempo, Players, num_play, matriz):
    def trocarJogador(x):
        if x == 3 :
            x = 0
        else:
            x += 1
        return x
    
    if (tempo - limTempo) > 30:
        Players[num_play].atacar(matriz,Players,num_play)
        Players[num_play].curar(matriz,Players,num_play)
        Players[num_play].descarregar(num_play)
        Players[num_play].resete()
        novoPlay = trocarJogador(num_play)
        while Players[novoPlay].morreu:
            novoPlay = trocarJogador(novoPlay)

        if novoPlay == num_play:
            return tempo,novoPlay,True
        return tempo,novoPlay,False
    return limTempo,num_play,False

def passarTempoM(tempo,limTempo):
    if tempo >= 1500:
        return limTempo, True
    elif (tempo - limTempo) >= 30:
        return tempo, True
    return limTempo,False

def mostrarMovimento(pos_x,pos_y,move,chao_sup):
    quadrado = pygame.Surface((20,20))
    quadrado.set_alpha(50)
    quadrado.fill((0,0,255))
    for x in range(pos_x-move[0],pos_x+move[0]+1):
        for y in range(pos_y-move[1],pos_y+move[1]+1):
            if x >= 0 and x < 50:
                if y >= 0 and y < 30:
                    chao_sup.blit( quadrado, [x*20, y*20])

def posSuperficie(tela, vidaBranca_sup,chao_sup,barraVida_sup,cor,vida,vidaMax):
    tela.fill((255,255,255))
    vidaBranca_sup.fill((255,255,255))
    tela.blit(chao_sup,[0,0])
    tela.blit(barraVida_sup,[1013,210])
    barraVerde = pygame.Surface((250*(vida/vidaMax),20))
    barraVerde.fill(cor)
    barraVida_sup.blit(vidaBranca_sup,[1,1])
    barraVida_sup.blit(barraVerde,[1,1])

def posCartas(tela,GuerreiroCard,ArqueiroCard,ExploradorCard,ConstrutorCard,CuradorCard,TransporteCard,FortCard,fonte,madeira_img,minerio_img):
    cor = (0,0,0)
    val0 = fonte.render("0",1,cor)
    val1 = fonte.render("1",1,cor)
    val2 = fonte.render("2",1,cor)
    val3 = fonte.render("3",1,cor)
    val5 = fonte.render("5",1,cor)
    val10 = fonte.render("10",1,cor)
    val20 = fonte.render("20",1,cor)
    #val25 = fonte.render("25",1,cor)
    
    
    

    tela.blit(madeira_img,[105,640])
    tela.blit(val2,[130,642])
    tela.blit(minerio_img,[105,663])
    tela.blit(val1,[130,665])
    tela.blit(GuerreiroCard,[20,615])

    tela.blit(madeira_img,[245,640])
    tela.blit(val5,[270,642])
    tela.blit(minerio_img,[245,663])
    tela.blit(val1,[270,665])
    tela.blit(ArqueiroCard,[160,615])

    tela.blit(madeira_img,[385,640])
    tela.blit(val1,[410,642])
    tela.blit(minerio_img,[385,663])
    tela.blit(val0,[410,665])
    tela.blit(ExploradorCard,[300,615])

    tela.blit(madeira_img,[525,640])
    tela.blit(val3,[550,642])
    tela.blit(minerio_img,[525,663])
    tela.blit(val1,[550,665])
    tela.blit(ConstrutorCard,[440,615])

    tela.blit(madeira_img,[665,640])
    tela.blit(val2,[690,642])
    tela.blit(minerio_img,[665,663])
    tela.blit(val0,[690,665])
    tela.blit(CuradorCard,[580,615])

    tela.blit(madeira_img,[805,640])
    tela.blit(val5,[830,642])
    tela.blit(minerio_img,[805,663])
    tela.blit(val2,[830,665])
    tela.blit(TransporteCard,[720,615])

    tela.blit(madeira_img,[945,640])
    tela.blit(val20,[970,642])
    tela.blit(minerio_img,[945,663])
    tela.blit(val10,[970,665])
    tela.blit(FortCard,[860,615])

def posImagens(tela,slogan_img,vida_img,escudo_img,madeira_img,minerio_img):
    tela.blit(slogan_img,(1060,560,200,200))
    tela.blit(vida_img,(1010,269,20,20))
    tela.blit(escudo_img,(1010,297,20,20))
    tela.blit(madeira_img,[1140,270])
    tela.blit(minerio_img,[1140,297])

def textosNumTela(fonte,val,cor):
    return fonte.render(str(val),1,cor)

def textosFixos(tela,tempo,limTempo,cor,Players,num_play,fonte,fonte2,text_Info,text_Player,text_Vida,text_Castelo,text_Recursos):
    text_Tempo = fonte.render(str(30-(tempo - limTempo)),1,cor)
    text_TempoJogo = fonte.render(str(tempo),1,(92,155,207))
    text_Limite = fonte2.render("Tempo Limite de 1500s",1,(92,155,207))
    text_qtdMadeira = fonte2.render(str(Players[num_play].qtdMadeira),1,cor)
    text_qtdMinerio = fonte2.render(str(Players[num_play].qtdMinerio),1,cor)
    text_qtdVida = fonte2.render(str(Players[num_play].castelo.vida),1,cor)
    text_qtdDefesa = fonte2.render(str(Players[num_play].castelo.defesa),1,cor)

    tela.blit(text_Player[num_play],(1010,30))
    tela.blit(text_Info,(1005,90))
    tela.blit(text_Tempo,(1050,125))
    tela.blit(text_TempoJogo,(1170,125))
    tela.blit(text_Limite,(1080,185))
    tela.blit(text_Vida,(1010,185))
    tela.blit(text_Castelo,(1010,240))
    tela.blit(text_Recursos,(1130,240))
    tela.blit(text_qtdVida,(1050,272))
    tela.blit(text_qtdDefesa,(1050,302))
    tela.blit(text_qtdMadeira,(1200,272))
    tela.blit(text_qtdMinerio,(1200,302))

def textosTela(tela,cor,Players,num_play,fonte,text_Guerreiros,text_Arqueiros,text_Explorador,text_Construtor,text_Curador,text_Transporte,text_Acampamento,text_Fortificacao):

    text_qtdGuerreiros = fonte.render(str(len(Players[num_play].ListGuerreiro)),1,cor)
    text_qtdArqueiros = fonte.render(str(len(Players[num_play].ListArqueiro)),1,cor)
    text_qtdExplorador = fonte.render(str(len(Players[num_play].ListExplorador)),1,cor)
    text_qtdConstrutor = fonte.render(str(len(Players[num_play].ListConstrutor)),1,cor)
    text_qtdCurador = fonte.render(str(len(Players[num_play].ListCurador)),1,cor)
    text_qtdTransporte = fonte.render(str(len(Players[num_play].ListTransporte)),1,cor)
    text_qtdAcampamento = fonte.render(str(len(Players[num_play].ListAcampamento)),1,cor)
    text_qtdFortificacao = fonte.render(str(Players[num_play].ListFortificacao),1,cor)

    tela.blit(text_Guerreiros,(1010,330))
    tela.blit(text_qtdGuerreiros,(1250,330))
    tela.blit(text_Arqueiros,(1010,345))
    tela.blit(text_qtdArqueiros,(1250,345))
    tela.blit(text_Explorador,(1010,360))
    tela.blit(text_qtdExplorador,(1250,360))
    tela.blit(text_Construtor,(1010,375))
    tela.blit(text_qtdConstrutor,(1250,375))
    tela.blit(text_Curador,(1010,390))
    tela.blit(text_qtdCurador,(1250,390))
    tela.blit(text_Transporte,(1010,405))
    tela.blit(text_qtdTransporte,(1250,405))
    tela.blit(text_Acampamento,(1010,420))
    tela.blit(text_qtdAcampamento,(1250,420))
    tela.blit(text_Fortificacao,(1010,435))
    tela.blit(text_qtdFortificacao,(1250,435))

def mapaDes(matriz,matrizRec,chao_sup,chao_image,arvore1_image,arvore2_image,mina_img,castelo1_image,castelo2_image,castelo3_image,castelo4_image,casteloDestroy_image,madeiraMap,minerioMap,guerreiro_image,arqueiro_image,explorador_image,construtor_image,curador_image,transporte_image,acampamento_image):
    chao_sup.blit(chao_image,(0,0,1000,600))
    for x in range(0,len(matriz)):
            for y in range(0,len(matriz[x])):
                if matriz[x][y] != 9:
                    if matriz[x][y] == 0:
                        material = matrizRec[x][y]
                        if material != 0:
                            if material[0] == "m":
                                chao_sup.blit(madeiraMap,(y*20,x*20,20,20))
                            if material[0] == "f":
                                chao_sup.blit(minerioMap,(y*20,x*20,20,20))
                    if matriz[x][y] == 1:
                        chao_sup.blit(arvore1_image,(y*20,((x*20)-2),20,20))
                    if matriz[x][y] == 2:
                        chao_sup.blit(arvore2_image,(y*20,((x*20)-10),20,40))
                    if matriz[x][y] == 3:
                        chao_sup.blit(mina_img,(y*20,x*20,20,20))
                    if matriz[x][y] == "cas1":
                        chao_sup.blit(castelo1_image,(y*20,x*20,60,60))
                    if matriz[x][y] == "cas2":
                        chao_sup.blit(castelo2_image,(y*20,x*20,60,60))
                    if matriz[x][y] == "cas3":
                        chao_sup.blit(castelo3_image,(y*20,x*20,60,60))
                    if matriz[x][y] == "cas4":
                        chao_sup.blit(castelo4_image,(y*20,x*20,60,60))
                    if matriz[x][y] == "casdestroy":
                        chao_sup.blit(casteloDestroy_image,(y*20,x*20,60,60))
                    if matriz[x][y] == "g0" or matriz[x][y] == "g1" or matriz[x][y] == "g2" or matriz[x][y] == "g3":    #Guerreiro
                        chao_sup.blit(guerreiro_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "a0" or matriz[x][y] == "a1" or matriz[x][y] == "a2" or matriz[x][y] == "a3":    #Arqueiro
                        chao_sup.blit(arqueiro_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "e0" or matriz[x][y] == "e1" or matriz[x][y] == "e2" or matriz[x][y] == "e3":    #Explorador
                        chao_sup.blit(explorador_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "c0" or matriz[x][y] == "c1" or matriz[x][y] == "c2" or matriz[x][y] == "c3":    #Construtor
                        chao_sup.blit(construtor_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "s0" or matriz[x][y] == "s1" or matriz[x][y] == "s2" or matriz[x][y] == "s3":    #Curador(Suporte)
                        chao_sup.blit(curador_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "t0" or matriz[x][y] == "t1" or matriz[x][y] == "t2" or matriz[x][y] == "t3":    #Transporte
                        chao_sup.blit(transporte_image,(y*20,x*20,20,20))
                    if matriz[x][y] == "p0" or matriz[x][y] == "p1" or matriz[x][y] == "p2" or matriz[x][y] == "p3":    #Acampamento
                        chao_sup.blit(acampamento_image,(y*20,x*20,20,20))
             

    

