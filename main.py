from turtle import goto
import pygame as pg
import os

imagem_background  = pg.image.load(os.path.join('imgs', 'backg2.png'))
imagem_pac  = [(pg.image.load(os.path.join('imgs', 'pac1.jpg'))),
                (pg.image.load(os.path.join('imgs', 'pac2.jpg'))),
                (pg.image.load(os.path.join('imgs', 'pac3.jpg')))]
imagem_f1  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_azul.png')),(30,30))
imagem_f2  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_vermelho.png')),(30,30))
imagem_f3  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_marron.png')),(30,30))
imagem_f4  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_rosa.png')),(30,30))
imagem_f5  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_doidao.png')),(30,30))
imagem_p1  = (pg.image.load(os.path.join('imgs', 'rect558.png')))
imagem_p2  = (pg.image.load(os.path.join('imgs', 'rect631.png')))
imagem_p3  = (pg.image.load(os.path.join('imgs', 'rect633.png')))
imagem_p4  = (pg.image.load(os.path.join('imgs', 'rect566.png')))
imagem_p5  = (pg.image.load(os.path.join('imgs', 'rect635.png')))
imagem_p6  = (pg.image.load(os.path.join('imgs', 'rect631-1.png')))
imagem_p7  = (pg.image.load(os.path.join('imgs', 'rect564.png')))
imagem_p8  = (pg.image.load(os.path.join('imgs', 'rect560.png')))
imagem_p9  = (pg.image.load(os.path.join('imgs', 'rect568.png')))
imagem_p10 = (pg.image.load(os.path.join('imgs', 'rect574.png')))
imagem_p11 = (pg.image.load(os.path.join('imgs', 'rect570.png')))
imagem_p12 = (pg.image.load(os.path.join('imgs', 'rect576.png')))
imagem_p13 = (pg.image.load(os.path.join('imgs', 'rect572.png')))
imagem_p14 = (pg.image.load(os.path.join('imgs', 'rect618.png')))
imagem_p15 = (pg.image.load(os.path.join('imgs', 'rect620.png')))
imagem_p16 = (pg.image.load(os.path.join('imgs', 'rect626.png')))
imagem_p17 = (pg.image.load(os.path.join('imgs', 'rect570-5.png')))
imagem_p18 = (pg.image.load(os.path.join('imgs', 'rect574-5.png')))
imagem_p19 = (pg.image.load(os.path.join('imgs', 'rect576-4.png')))
imagem_p20 = (pg.image.load(os.path.join('imgs', 'rect572-0.png')))
imagem_p21 = (pg.image.load(os.path.join('imgs', 'rect572-0-0.png')))
imagem_p22 = (pg.image.load(os.path.join('imgs', 'rect570-5-3.png')))
imagem_p23 = (pg.image.load(os.path.join('imgs', 'rect568-2.png')))
imagem_p24 = (pg.image.load(os.path.join('imgs', 'rect604.png')))
imagem_p25 = (pg.image.load(os.path.join('imgs', 'rect603.png')))

class PAC:
    IMGS = imagem_pac
    Tempo_Animacao = 5
    Rotacao = 90
    desloc_pac = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x_ant = x
        self.y_ant = y
        self.angulo = 0
        self.velocidadex = 0
        self.velocidadey = 0
        self.velocidadex_ant = 0
        self.velocidadey_ant = 0
        self.angulo_ant = 0
        self.tempo = 0
        self.imagem = self.IMGS[0]
        self.contagem = 0

    def mudar_direita(self):
        self.velocidadex = self.desloc_pac
        self.velocidadey = 0
        self.angulo = 0

    def mudar_esquerda(self):
        self.velocidadex = -self.desloc_pac
        self.velocidadey = 0
        self.angulo = 180

    def mudar_sobe(self):
        self.velocidadex = 0
        self.velocidadey = -self.desloc_pac
        self.angulo = 90

    def mudar_desce(self):
        self.velocidadex = 0
        self.velocidadey = self.desloc_pac
        self.angulo = -90

    def mover(self):
        self.x +=  self.velocidadex
        self.y += self.velocidadey

    def desenhar(self,tela):
        self.contagem += 1
        if self.contagem < self.Tempo_Animacao:
            self.imagem = self.IMGS[0]
        elif self.contagem < self.Tempo_Animacao * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem < self.Tempo_Animacao * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem < self.Tempo_Animacao * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem >= self.Tempo_Animacao * 4:
            self.imagem = self.IMGS[0]
            self.contagem = 0

        imagem_rotacionada = pg.transform.rotate(self.imagem, self.angulo)
        pos_center = self.imagem.get_rect(topleft = (self.x,self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = pos_center)
        tela.blit(imagem_rotacionada, retangulo)
    
    def get_mask(self):
        return pg.mask.from_surface(self.imagem)

class FANTASMA_1:
    IMGS = imagem_f5
    desloc = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x_ant = x
        self.y_ant = y
        self.velocidadex = 0
        self.velocidadey = 0
        self.angulo = 0
        self.tempo = 0
        self.imagem = self.IMGS

    def mudar_direita(self):
        self.velocidadex = self.desloc
        self.velocidadey = 0
        self.angulo = 0

    def mudar_esquerda(self):
        self.velocidadex = -self.desloc
        self.velocidadey = 0
        self.angulo = 180
    def mudar_sobe(self):
        self.velocidadex = 0
        self.velocidadey = -self.desloc
        self.angulo = 90
    def mudar_desce(self):
        self.velocidadex = 0
        self.velocidadey = self.desloc
        self.angulo = -90
    def mover(self):
        self.x += self.velocidadex
        self.y += self.velocidadey

    def desenhar(self,tela):
        pos_center = self.imagem.get_rect(topleft = (self.x,self.y)).center
        retangulo = self.imagem.get_rect(center = pos_center)
        tela.blit(self.imagem, retangulo)
        
    def get_mask(self):
        return pg.mask.from_surface(self.imagem)

    def colidir(self, PAC):
        PAC_mask = PAC.get_mask()
        Fantasma1_mask = pg.mask.from_surface(self.imagem)
        distancia = (self.x - PAC.x, self.y - PAC.y)
        Fantasma1_ponto = PAC_mask.overlap(Fantasma1_mask,distancia)

        if Fantasma1_ponto:
            return True
        else:
            return False
class PAREDE():

    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.imagem = img

    def desenhar(self,tela):
        pos_center = self.imagem.get_rect(topleft = (self.x,self.y)).center
        retangulo = self.imagem.get_rect(center = pos_center)
        tela.blit(self.imagem, retangulo)
    
    def colidir(self, PAC):
        PAC_mask = PAC.get_mask()
        Fantasma1_mask = pg.mask.from_surface(self.imagem)
        distancia = (self.x - PAC.x, self.y - PAC.y)
        Parede_ponto = PAC_mask.overlap(Fantasma1_mask,distancia)

        if Parede_ponto:
            return True
        else:
            return False
def desenhar_tela(tela, PAC, FANSTAMA_1,paredes):
    tela.blit(imagem_background, (0,0))
    for PAC in PAC:
        PAC.desenhar(tela)
    for FANSTAMA_1 in FANSTAMA_1:
        FANSTAMA_1.desenhar(tela)
    for parede in paredes:
        parede.desenhar(tela)
    pg.display.update()

def main():
    pacs = [PAC(230,223)]
    fantasmas = [FANTASMA_1(300,280)]
    tela = pg.display.set_mode((578,640))
    relogio = pg.time.Clock()

    paredes = [PAREDE(0,0,imagem_p1),PAREDE(0,624,imagem_p1),PAREDE(0,0,imagem_p2),PAREDE(562,0,imagem_p2),PAREDE(0,192,imagem_p3),PAREDE(0,266,imagem_p3),PAREDE(458,192,imagem_p3),PAREDE(458,266,imagem_p3),PAREDE(0,316,imagem_p3),PAREDE(0,390,imagem_p3),PAREDE(458,316,imagem_p3),PAREDE(458,390,imagem_p3),PAREDE(50,50,imagem_p4),PAREDE(458,50,imagem_p4),PAREDE(104,192,imagem_p5),PAREDE(458,192,imagem_p5),PAREDE(104,316,imagem_p5),PAREDE(458,316,imagem_p5),PAREDE(0,390,imagem_p6),PAREDE(562,390,imagem_p6),PAREDE(154,50,imagem_p7),PAREDE(331,50,imagem_p7),PAREDE(281,0,imagem_p8),PAREDE(50,126,imagem_p9),PAREDE(458,126,imagem_p9),PAREDE(212,126,imagem_p10),PAREDE(154,126,imagem_p11),PAREDE(400,126,imagem_p11),PAREDE(281,126,imagem_p12),PAREDE(154,192,imagem_p13),PAREDE(331,192,imagem_p13),PAREDE(212,258,imagem_p14),PAREDE(306,258,imagem_p14),PAREDE(212,258,imagem_p15),PAREDE(350,258,imagem_p15),PAREDE(212,329,imagem_p16),PAREDE(154,316,imagem_p17),PAREDE(400,316,imagem_p17),PAREDE(212,379,imagem_p18),PAREDE(212,501,imagem_p18),PAREDE(275,379,imagem_p19),PAREDE(275,501,imagem_p19),PAREDE(154,440,imagem_p20),PAREDE(337,440,imagem_p20),PAREDE(50,440,imagem_p21),PAREDE(458,440,imagem_p21),PAREDE(84,440,imagem_p22),PAREDE(458,440,imagem_p22),PAREDE(0,501,imagem_p23),PAREDE(528,501,imagem_p23),PAREDE(50,562,imagem_p24),PAREDE(337,562,imagem_p24),PAREDE(154,501,imagem_p25),PAREDE(400,501,imagem_p25)]

    rodando = True
    while rodando:
        relogio.tick(60)
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
                pg.quit()
                quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_a:
                    for pac in pacs:

                        pac.mudar_esquerda()
               
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_s:
                    for pac in pacs:

                        pac.mudar_desce()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_d:
                    for pac in pacs:

                        pac.mudar_direita()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_w:
                    for pac in pacs:

                        pac.mudar_sobe()   

            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_LEFT:
                    for fantasma in fantasmas:
                        fantasma.mudar_esquerda()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_DOWN:
                    for fantasma in fantasmas:
                        fantasma.mudar_desce()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RIGHT:
                    for fantasma in fantasmas:
                        fantasma.mudar_direita()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_UP:
                    for fantasma in fantasmas:
                        fantasma.mudar_sobe()     
        for pac in pacs:
            pac.mover()
        for fantasma in fantasmas:
            fantasma.mover()
        for fantasma in fantasmas:
            for i, pac in enumerate(pacs):
                if fantasma.colidir(pac):
                    pacs.pop(i)
        for parede in paredes:
            for i, pac in enumerate(pacs):
                if parede.colidir(pac):                
                    if pacs[i].angulo == 180:
                        pacs[i].x += pacs[i].desloc_pac 
                    if pacs[i].angulo == 90:
                        pacs[i].y += pacs[i].desloc_pac
                    if pacs[i].angulo == 0:
                        pacs[i].x -= pacs[i].desloc_pac
                    if pacs[i].angulo == -90:
                        pacs[i].y -= pacs[i].desloc_pac
 
        for parede in paredes:
            for i, fantasma in enumerate(fantasmas):
                if parede.colidir(fantasma):
                    if fantasmas[i].angulo == 180:
                        fantasmas[i].x += fantasmas[i].desloc 
                    if fantasmas[i].angulo == 90:
                        fantasmas[i].y += fantasmas[i].desloc 
                    if fantasmas[i].angulo == 0:
                        fantasmas[i].x -= fantasmas[i].desloc 
                    if fantasmas[i].angulo == -90:
                        fantasmas[i].y -= fantasmas[i].desloc 

            for i, fantasma in enumerate(fantasmas):
                if parede.colidir(fantasma):
                    fantasmas.pop(i) 
        desenhar_tela(tela,pacs,fantasmas,paredes)
if __name__ == '__main__':
    main()