import pygame

# init
pygame.init()
# variable running game
isRun = True


# membuat display surface object
window = pygame.display.set_mode((500,500))

#object game
x = 250
y = 250

while isRun:
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    # update asset
    # render ke display
pygame.quit()




