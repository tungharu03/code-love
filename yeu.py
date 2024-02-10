import pygame
from pygame import mixer
import ptext

pygame.init()
clock = pygame.time.Clock()

logo = pygame.image.load('sun.png')
screen = pygame.display.set_mode((906, 800))
pygame.display.set_caption("Mãi iu <3")
pygame.display.set_icon(logo)
img = pygame.image.load('love.jpg')
img = pygame.transform.scale(img, (2416, 1206))
rect = pygame.Rect(20, 100, 860, 340)


class CreateButton():
    def __init__(self, surface):
        self.surface = surface
        self.color = 'white'
        self.posX = 0
        self.posY = 0
        self.btnW = 10
        self.btnH = 10
        self.radius = 0
        self.mPos = []
        self.shadow = 0
        self.shadowColor = 'white'
        self.text = ''
        self.txtColor = 'white'
        self.font = 'Arial'
        self.size = 8

    def drawbutton(self, color, posX, posY, btnW, btnH, radius, shadow, sColor):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.btnW = btnW
        self.btnH = btnH
        self.radius = radius
        self.shadow = shadow
        self.shadowColor = sColor

        pygame.draw.rect(self.surface, self.shadowColor, (self.posX+self.shadow, self.posY+self.shadow,
                                                          self.btnW, self.btnH), border_radius=self.radius)
        btn = pygame.draw.rect(self.surface, self.color, (self.posX, self.posY,
                                                          self.btnW, self.btnH), border_radius=self.radius)
        return (btn)

    def drawtext(self, font, size, text, txtColor):
        self.text = text
        self.txtColor = txtColor
        self.font = font
        self.size = size
        position = (self.posX + self.btnW//2, self.posY + self.btnH//2)
        ptext.draw(self.text, center=position, sysfontname=self.font,
                   fontsize=self.size, color=self.txtColor, surf=screen)


def createText(surface, font, text, size, color):
    ptext.draw(text, surface.topleft,
               sysfontname='Tahoma', fontsize=size, color=color, width=860, shadow=(0.8, 0.8), scolor='grey')


def playSong(song):
    mixer.music.load(song)
    mixer.music.play()


no_posX = 450
no_posY = 450
yes_posX = 150
yes_posY = 450
size = 80
yesColor = 'pink'
yesShadow = 5
textBox = 'Em có yêu anh hông???'
textColor = 'red'
yesClick = False
yesTxtcolor = 'white'
timesClick = 0
run = True
while run:
    clock.tick(60)
    screen.blit(img, (-600, -300))
    for event in pygame.event.get():
        mPos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            yesClick = True
            timesClick += 1

    createText(rect, 'Tahoma', textBox, size, textColor)
    yes_button = CreateButton(screen)
    rect1 = yes_button.drawbutton(
        yesColor, yes_posX, yes_posY, 160, 100, 20, yesShadow, 'grey')
    yes_button.drawtext('Arial', 72, 'CÓ', yesTxtcolor)

    no_button = CreateButton(screen)
    rect2 = no_button.drawbutton(
        'lightblue', no_posX, no_posY, 250, 100, 20, 7, 'grey')
    no_button.drawtext('Arial', 72, 'Khum', 'black')

    if rect2.collidepoint(mPos):
        no_posX = no_posX + mPos[0]
        no_posY = no_posY + mPos[1]
        if no_posX > 900-200:
            no_posX = 300
        if no_posY > 600:
            no_posY = 30
        playSong('no.wav')
    if yesClick and rect1.collidepoint(mPos):
        textBox = 'Ahihi ^^ Anh biết mà <3'
        size = 75
        yesShadow = 0
        yesColor = 'DodgerBlue'
        yesTxtcolor = 'black'
        no_posX = no_posY = -100
        if timesClick == 1:
            playSong('decide.mp3')
            yesClick = False

    pygame.display.update()

pygame.quit()
