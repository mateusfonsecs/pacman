import pygame as pg
import os

imagem_background  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'backg1.jpg')),(500,500))
imagem_pac  = [pg.transform.scale(pg.image.load(os.path.join('imgs', 'pac1.jpg')),(30,30)),
                pg.transform.scale(pg.image.load(os.path.join('imgs', 'pac2.jpg')),(30,30)),
                pg.transform.scale(pg.image.load(os.path.join('imgs', 'pac3.jpg')),(30,30))]
imagem_f1  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_azul.png')),(30,30))
imagem_f2  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_vermelho.png')),(50,50))
imagem_f3  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_marron.png')),(200,200))
imagem_f4  = pg.transform.scale(pg.image.load(os.path.join('imgs', 'fantasma_rosa.png')),(200,200))

class PAC:
    IMGS = imagem_pac
    Tempo_Animacao = 5
    Rotacao = 90
    desloc = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidadex = 0
        self.velocidadey = 0
        self.tempo = 0
        self.imagem = self.IMGS[0]
        self.contagem = 0

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
    IMGS = imagem_f1
    desloc = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocidadex = 0
        self.velocidadey = 0
        self.tempo = 0
        self.imagem = self.IMGS

    def mudar_direita(self):
        self.velocidadex = self.desloc
        self.velocidadey = 0

    def mudar_esquerda(self):
        self.velocidadex = -self.desloc
        self.velocidadey = 0

    def mudar_sobe(self):
        self.velocidadex = 0
        self.velocidadey = -self.desloc

    def mudar_desce(self):
        self.velocidadex = 0
        self.velocidadey = self.desloc

    def mover(self):
        self.x += self.velocidadex
        self.y += self.velocidadey

    def desenhar(self,tela):
        pos_center = self.imagem.get_rect(topleft = (self.x,self.y)).center
        retangulo = self.imagem.get_rect(center = pos_center)
        tela.blit(self.imagem, retangulo)
    
    def colidir(self, PAC):
        PAC_mask = PAC.get_mask()
        Fantasma1_mask = pg.mask.from_surface(self.imagem)
        distancia = (self.x - PAC.x, self.y - PAC.y)
        Fantasma1_ponto = PAC_mask.overlap(Fantasma1_mask,distancia)

        if Fantasma1_ponto:
            return True
        else:
            return False

def desenhar_tela(tela, PAC, FANSTAMA_1):
    tela.blit(imagem_background, (0,0))
    for PAC in PAC:
        PAC.desenhar(tela)
    for FANSTAMA_1 in FANSTAMA_1:
        FANSTAMA_1.desenhar(tela)
    pg.display.update()

def main():
    pacs = [PAC(230,230)]
    fantasmas = [FANTASMA_1(300,300)]
    tela = pg.display.set_mode((500,500))
    relogio = pg.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)
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
        desenhar_tela(tela,pacs,fantasmas)
if __name__ == '__main__':
    main()