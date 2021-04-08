import pygame
import sys

# khoi tao pygame
pygame.init()

# khai bao chieu dai va rong: note
width, height = 800, 450

# khai bao khung tro choi
screen = pygame.display.set_mode((width, height))

# tai anh vao mot bien
bg = pygame.image.load("./img/bg.jpg")
# ep khung cho anh: thu nhat : anh can chinh, thu hai : gia tri khung
bg = pygame.transform.scale(bg,(width,height))

# load anh nhan vat
character = pygame.image.load("./img/character.png")
# ep kich thuoc cho nhan vat
character = pygame.transform.scale(character,(200,180))
# tao rect - rectangle
character_rect = character.get_rect(center=(400,225))

while True: # lap vo han
    for event in pygame.event.get(): # lay su kien trong pygame
        if event.type == pygame.QUIT: # so sanh voi gia tri thoat
            pygame.quit()
            sys.exit()

    # dung de hien thi : gia tri 1 : ten anh , gia tri 2 : toa do
    screen.blit(bg, (0,0))

    # hien thi nhan vat
    screen.blit(character, character_rect)

    # init -> loop _> update
    pygame.display.update()
    
