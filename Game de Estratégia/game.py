import pygame
from Player import *
from funcoesComplexas import *
from interface import *
from random import *

def main():
    pygame.init()
    tela = pygame.display.set_mode([1280,720])
    pygame.display.set_caption("MedievalGame")
    relogio = pygame.time.Clock()

    #criando a superficie do Campo
    chao_sup = pygame.Surface((1000,600))
    barraVida_sup = pygame.Surface((252,22))
    vidaBranca_sup = pygame.Surface((250,20))

    #Imagens
    chao_image = pygame.image.load("Imagens/chao.png").convert_alpha()
    arvore1_image = pygame.image.load("Imagens/Arvore1.png").convert_alpha()
    arvore2_image = pygame.image.load("Imagens/Arvore2.png").convert_alpha()
    arvore3_image = pygame.image.load("Imagens/Arvore3.png").convert_alpha()
    mina_img = pygame.image.load("Imagens/minaMap.png").convert_alpha()
    castelo1_image = pygame.image.load("Imagens/Castelo1.png").convert_alpha()
    castelo2_image = pygame.image.load("Imagens/Castelo2.png").convert_alpha()
    castelo3_image = pygame.image.load("Imagens/Castelo3.png").convert_alpha()
    castelo4_image = pygame.image.load("Imagens/Castelo4.png").convert_alpha()
    casteloDestroy_image = pygame.image.load("Imagens/CasteloDestroy.png").convert_alpha()
    madeiraMap_img = pygame.image.load("Imagens/madeiraMap.png").convert_alpha()
    minerioMap_img = pygame.image.load("Imagens/minerioMap.png").convert_alpha()
    #testeArvore_img = pygame.image.load("Sem título.png").convert_alpha()
    slogan_image = pygame.image.load("Imagens/slogan.png").convert_alpha()
    escudo_image = pygame.image.load("Imagens/escudo.png").convert_alpha()
    vida_image = pygame.image.load("Imagens/cruz.png").convert_alpha()
    madeira_img = pygame.image.load("Imagens/madeira.png").convert_alpha()
    minerio_img = pygame.image.load("Imagens/minerio.png").convert_alpha()

    #criando os Protagonistas
    guerreiro_image = pygame.image.load("Imagens/Guerreiro.png").convert_alpha()
    arqueiro_image = pygame.image.load("Imagens/Arqueiro.png").convert_alpha()
    explorador_image = pygame.image.load("Imagens/Explorador.png").convert_alpha()
    construtor_image = pygame.image.load("Imagens/Construtor.png").convert_alpha()
    curador_image = pygame.image.load("Imagens/Medico.png").convert_alpha()
    transporte_image = pygame.image.load("Imagens/transporte.png").convert_alpha()
    acampamento_image = pygame.image.load("Imagens/Acampamento1.png").convert_alpha()
    
    testeCard = pygame.Surface((80,100))
    guerreiroCard = pygame.image.load("Imagens/Cartas/guerreiro.jpg")
    arqueiroCard = pygame.image.load("Imagens/Cartas/archer.jpg")
    exploradorCard = pygame.image.load("Imagens/Cartas/explorador.jpg")
    construtorCard = pygame.image.load("Imagens/Cartas/contruct.jpg")
    curadorCard = pygame.image.load("Imagens/Cartas/medico.jpg")
    transporteCard = pygame.image.load("Imagens/Cartas/transporte.jpg")
    acampamentoCard = pygame.image.load("Imagens/Cartas/acampamento.jpg")
    fortCard = pygame.image.load("Imagens/Cartas/fortificacao.jpg")

    #posicionando a imagem a superficie 
    chao_sup.blit(chao_image,(0,0))

    terRect = pygame.Rect(1040,480,200,50)

    #cores
    cor_vermelho = (255,0,0)
    cor_verde = (0,255,0)
    cor_preto = (0,0,0)
    cor_azul = (0,0,255)
    

    #criando Fontes e palavras
    font_padrao = pygame.font.init() # iniciando uma fonte
    fonte_grande = pygame.font.SysFont(font_padrao, 60)    #tamanho da letra
    fonte_media = pygame.font.SysFont(font_padrao, 30)
    fonte_pequena = pygame.font.SysFont(font_padrao, 25)
    text_Info = fonte_media.render("Tempo Restante", 1, cor_preto)
    text_Player = [
                    fonte_grande.render("Player 1", 1, cor_preto),
                    fonte_grande.render("Player 2", 1, cor_preto),
                    fonte_grande.render("Player 3", 1, cor_preto),
                    fonte_grande.render("Player 4", 1, cor_preto),
                   ]
    text_Vida = fonte_media.render("Vida", 1, cor_preto)
    text_Recursos = fonte_media.render("Recursos", 1, cor_preto)
    text_Castelo = fonte_media.render("Castelo", 1, cor_preto)
    text_Ter = fonte_media.render("Terminar Jogada",1,(255,255,255))
    text_Guerreiros = fonte_pequena.render("Qtd Guerreiros:",1, cor_preto)
    text_Arqueiros = fonte_pequena.render("Qtd Arqueiros:",1, cor_preto)
    text_Explorador = fonte_pequena.render("Qtd Exploradores:",1, cor_preto)
    text_Construtor = fonte_pequena.render("Qtd Construtores:",1, cor_preto)
    text_Curador = fonte_pequena.render("Qtd Curadores:",1, cor_preto)
    text_Transporte = fonte_pequena.render("Qtd Transportes:",1, cor_preto)
    text_Acampamento = fonte_pequena.render("Qtd Acampamentos:",1, cor_preto)
    text_Fortificacao = fonte_pequena.render("Qtd Cartas de Fortificação:",1, cor_preto)
    

    #criando mapa
    matriz =    [#1 2 3 4 5 6 7 8 910 1 2 3 4 5 6 7 8 920 1 2 3 4 5 6 7 8 930 1 2 3 4 5 6 7 8 940 1 2 3 4 5 6 7 8 9 50
                 [3,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,3,9,9],#1
                 [9,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,9,9,9],#2
                 [9,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,9,9,9],#3
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#4
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#5
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#6
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#7
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#8
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#9
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#10
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#11
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#12
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#13
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#14
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#15
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#16
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#17
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#18
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#19
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#20
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#21
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#22
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#23
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#24
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#25
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#26
                 [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],#27
                 [3,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,3,9,9],#28
                 [9,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,9,9,9],#29
                 [9,9,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,9,9,9],#30
                ]


    def recMad1():
        x = randint(1,100)
        if x <= 30 :
            return 0
        elif x <= 80 :
            return "m1"
        else:
            return "m3"
    def recMad2():
        x = randint(1,100)
        if x <= 20 :
            return 0
        elif x <= 50 :
            return "m1"
        else:
            return "m3"

    def recFer():
        x = randint(1,100)
        if x <= 70 :
            return "f7"
        else:
            return "f12"

    def defMap():
        x = randint(1,1000)
        #if x <= 100:
        #    return 0
        if x <= 850:
            return 1
        elif x <= 990:
            return 2
        else:
            return 3
    
    matrizRecursos = []
    for x in range(0,len(matriz)):
        matrizRecursos.append([])
        for y in range(0,len(matriz[x])):
            if matriz[x][y] == 1:
                matriz[x][y] = defMap()
                if x < 7 or x > 22 or y < 10 or y > 39:
                    if matriz[x][y] == 3 :
                        matriz[x][y] = 1
                if matriz[x][y] == 1:
                    val = recMad1()
                    matrizRecursos[x].append(val)
                elif matriz[x][y] == 2:
                    val = recMad2()
                    matrizRecursos[x].append(val)
                elif matriz[x][y] == 3:
                        val = recFer()
                        matrizRecursos[x].append(val)
                elif matriz[x][y] == 0:
                    matrizRecursos[x].append(0)
            else:
                matrizRecursos[x].append(0)

    #Musicas e Sons
    musicas = ["Musicas/Medieval Life.ogg","Musicas/bensound-epic.ogg","Musicas/Epic Music 1.ogg","Musicas/Epic Music 2.ogg","Musicas/Soundtrack 05 - Up Is Down.ogg"]

    pygame.mixer.music.load(musicas[0])
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.6)
            
    #instanciando Variaveis e Classes
    matriz[0][0] = "cas1"
    matriz[0][47] = "cas2"
    matriz[27][0] = "cas3"
    matriz[27][47] = "cas4"
    Players = [Player(0,0,[3,3]),Player(0,47,[3,46]), Player(27,0,[26,3]), Player(27,47,[26,46])]

    
    sair = False

    #tempo
    tempo = pygame.time.get_ticks()//1000
    limTempo = tempo
    
    num_play = 0

    tipo = 0
    acabar = True
    
    mus = 0
    def trocarMusic(i):
        if i == 4:
            return 0
        return i+1

# ------------------------------------ COMEÇA O WHILE DO JOGO ------------
    
    while sair == False :
        tempo = pygame.time.get_ticks()//1000
        limTempo,num_play,fim = passarTempo(tempo, limTempo, Players, num_play, matriz)
        
        vida = Players[num_play].castelo.vida
        if vida < 0:
            vida = 0
        vidaMax = Players[num_play].castelo.vidaMax

        tocou = pygame.mixer.music.get_busy()
        if tocou == False:
            mus = trocarMusic(mus)
            pygame.mixer.music.load(musicas[mus])
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.6)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                tipo = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if 1040 <= pos_mouse[0] <= 1240 and 480 <= pos_mouse[1] <= 530:
                    limTempo , num_play , fim = passarTempo(tempo,-30,Players,num_play,matriz)
                    if fim:
                        sair = True
                        tipo = 1
                if pos_mouse[1] < 600:
                    if pos_mouse[0] < 1000:
                        Personagem,carta = clicarNoPersonagem(pos_mouse,matriz,Players,num_play)
                        if Personagem != False:
                            mover(Personagem,carta,matriz,matrizRecursos,tela,vidaBranca_sup,chao_sup,barraVida_sup,cor_verde,vida,vidaMax,Players,num_play,limTempo,acampamentoCard,fortCard,fonte_grande,fonte_media,fonte_pequena,text_Info,text_Player,text_Vida,text_Castelo,text_Recursos,slogan_image,vida_image,escudo_image,madeira_img,minerio_img,chao_image,arvore1_image,arvore2_image,mina_img,castelo1_image,castelo2_image,castelo3_image,castelo4_image,casteloDestroy_image,madeiraMap_img,minerioMap_img,guerreiro_image,arqueiro_image,explorador_image,construtor_image,curador_image,transporte_image,acampamento_image)
                if 615 <= pos_mouse[1] <= 715 :
                    Players[num_play].pos_respwn(matriz)
                    x,y = Players[num_play].respwn
                    if 20 <= pos_mouse[0] <= 100:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Guerreiro")
                            if criou :
                                matriz[x][y] = "g" + str(num_play)
                    if 160 <= pos_mouse[0] <= 240:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Arqueiro")
                            if criou :
                                matriz[x][y] = "a" + str(num_play)
                    if 300 <= pos_mouse[0] <= 380:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Explorador")
                            if criou :
                                matriz[x][y] = "e" + str(num_play)
                    if 440 <= pos_mouse[0] <= 520:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Construtor")
                            if criou :
                                matriz[x][y] = "c" + str(num_play)
                    if 580 <= pos_mouse[0] <= 660:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Curador")
                            if criou :
                                matriz[x][y] = "s" + str(num_play)
                    if 720 <= pos_mouse[0] <= 800:
                        if matriz[x][y] == 0:
                            criou = Players[num_play].construir("Transporte")
                            if criou :
                                matriz[x][y] = "t" + str(num_play)
                    if 860 <= pos_mouse[0] <= 940:
                        Players[num_play].fortificarCarta("Fortificacao",x,y)
                        


        #posicionando Superficies e cores
        posSuperficie(tela,vidaBranca_sup,chao_sup,barraVida_sup,cor_verde,vida,vidaMax)
        

        #posicioando Cartas
        testeCard.fill(cor_azul)
        posCartas(tela,guerreiroCard,arqueiroCard,exploradorCard,construtorCard,curadorCard,transporteCard,fortCard,fonte_pequena,madeira_img,minerio_img)

        #posicionar imagens
        posImagens(tela,slogan_image,vida_image,escudo_image,madeira_img,minerio_img)


        #Posicioanando Textos na tela
        textosFixos(tela,tempo,limTempo,cor_preto,Players,num_play,fonte_grande,fonte_pequena,text_Info,text_Player,text_Vida,text_Castelo,text_Recursos)
        textosTela(tela,cor_preto,Players,num_play,fonte_pequena,text_Guerreiros,text_Arqueiros,text_Explorador,text_Construtor,text_Curador,text_Transporte,text_Acampamento,text_Fortificacao)

        #Mapa desenho
        
        mapaDes(matriz,matrizRecursos,chao_sup,chao_image,arvore1_image,arvore2_image,mina_img,castelo1_image,castelo2_image,castelo3_image,castelo4_image,casteloDestroy_image,madeiraMap_img,minerioMap_img,guerreiro_image,arqueiro_image,explorador_image,construtor_image,curador_image,transporte_image,acampamento_image)

        pygame.draw.rect(tela,cor_vermelho,terRect)
        tela.blit(text_Ter,(1055,497))

        if tempo > 1500 :
            sair = True
            acabar = False
            tipo = 2

        if fim :
            sair = True
            acabar = False
            tipo = 1

        
        pygame.display.update()
        relogio.tick(30)

    temp = tempo


    maior = 0
    ind = 0
    for i in range(0,4):
        if maior < Players[i].castelo.vida:
            maior = Players[i].castelo.vida
            ind = i

    fundo_img = pygame.image.load("Imagens/fundo_img.jpg").convert_alpha()
    pygame.mixer.music.load("Musicas/Medieval fim.ogg")
    pygame.mixer.music.play()
    while acabar == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                acabar = True
                
        tela.fill((255,255,255))
        tela.blit(fundo_img,[0,0])
        fonte_Giga = pygame.font.SysFont(font_padrao, 120)
        text_vencedor = [
                        fonte_Giga.render("PLAYER 1 Vencedor!!!",1,cor_preto),
                        fonte_Giga.render("PLAYER 2 Vencedor!!!",1,cor_preto),
                        fonte_Giga.render("PLAYER 3 Vencedor!!!",1,cor_preto),
                        fonte_Giga.render("PLAYER 4 Vencedor!!!",1,cor_preto)
                        ]
        tela.blit(text_vencedor[num_play],(100,50))
        if tipo == 1:
            text_motivo = fonte_grande.render("Voce derrotou todos os seus oponentes!!",1,(0,0,0))
            text_motivo2 = fonte_grande.render("no tempo de :",1,cor_preto)
            text_Tempo = fonte_grande.render(str(tempo)+" segundos",1,cor_preto)
            tela.blit(text_motivo,(100,250))
            tela.blit(text_motivo2,(100,300))
            tela.blit(text_Tempo,(400,300))
        if tipo == 2:
            text_motivo = fonte_grande.render("Voce ganhou por ter mais vida que seus adversários!!",1,(0,0,0))
            text_motivo2 = fonte_grande.render("Possuindo apenas :",1,(0,0,0))
            text_life = fonte_grande.render(str(maior)+"  de vida!",1,cor_preto)
            tela.blit(text_motivo,(100,250))
            tela.blit(text_motivo2,(100,300))
            tela.blit(text_life,(500,300))
            
            
        pygame.display.update()
    pygame.quit()    

main()


