import pygame

# init
pygame.init()

# membuat display surface object
window = pygame.display.set_mode((500,500))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

pygame.quit()

# user input, database input
# update asset
# render ke display

