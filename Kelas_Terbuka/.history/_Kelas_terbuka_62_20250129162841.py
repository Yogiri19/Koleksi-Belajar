import pygame

# init
pygame.init()
# variable running game
isRun = True


# membuat display surface object
window = pygame.display.set_mode((500,500))

#object game
# posisi
x = 250 # horizontal
y = 250 # vertikal

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while isRun:
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window(255,0,0),(x,y,lebar,panjang))
    # render ke display
    pygame.display.update()

pygame.quit()




