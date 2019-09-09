import pygame

NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO = [255,255,255]

def escalamiento(ptoPvte,puntos,tamanoEscala):
    x=0
    y=0
    puntosFinal = []
    for value in puntos:
        x=value[0]-ptoPvte[0]
        x=x*tamanoEscala
        x=x+ptoPvte[0]
        y=value[1]-ptoPvte[1]
        y=y*tamanoEscala
        y=y+ptoPvte[1]
        puntosFinal.append([x,y])

    return puntosFinal

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    pygame.display.flip()
    flag = 0
    puntosCapturados =[]
    puntoFin = []
    pos =[]
    fin=False
    while not fin:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if flag < 5:
                    puntosCapturados.append(event.pos)
                    pygame.draw.circle(pantalla,VERDE,event.pos,2)
                    flag+=1
                    pygame.display.flip()

                if flag == 5:
                    puntoFin=escalamiento(puntosCapturados[0],puntosCapturados,2)
                    pygame.draw.polygon(pantalla,BLANCO,puntosCapturados,1)
                    pygame.draw.polygon(pantalla,AZUL,puntoFin,1)
                    puntoFin=[]
                    puntosCapturados=[]
                    flag=0
                    pygame.display.flip()
