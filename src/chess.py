

import pygame

class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.image = image
        self.killable = killable
def place_pieces():
    bp = Piece('black', 'pawn', 'img/black-pawn.png')
    wp = Piece('white', 'pawn', 'img/white-pawn.png')
    br = Piece('black', 'rook', 'img/black-rook.png')
    wr = Piece('white', 'rook', 'img/white-rook.png')
    bn = Piece('black', 'knight', 'img/black-knight.png')
    wn = Piece('white', 'knight', 'img/white-knight.png')
    bb = Piece('black', 'bishop', 'img/black-bishop.png')
    wb = Piece('white', 'bishop', 'img/white-bishop.png')
    bq = Piece('black', 'queen', 'img/black-queen.png')
    wq = Piece('white', 'queen', 'img/white-queen.png')
    bk = Piece('black', 'king', 'img/black-king.png')
    wk = Piece('white', 'king', 'img/white-king.png')
    board = [['' for i in range(8)] for j in range(8)]
    for i in range(8):
        board[1][i] = bp
        board[6][i] = wp
    



def draw_board():
    # pygame.draw.rect(screen, color, (x,y,width,height)) if on index (0,0) make a 100x100 square and so on
   for rows in range(8):
         for cols in range(8):
            if (rows + cols) % 2 == 0:
               pygame.draw.rect(screen,(238,238,210), (rows * 100 ,cols * 100,100,100)) #light square, 
            else:
               pygame.draw.rect(screen,(118,150,86), (rows * 100, cols *100,100,100)) # dark square
   
def place_images():
    scale_size = (100,100)
    #White pieces
    wr_image1 = pygame.transform.scale(pygame.image.load('img/white-rook.png'), scale_size)
    screen.blit(wr_image1, (0,700))
    wn_image1 = pygame.transform.scale(pygame.image.load('img/white-knight.png'), scale_size)
    screen.blit(wn_image1, (100,700))
    wb_image1 = pygame.transform.scale(pygame.image.load('img/white-bishop.png'), scale_size)
    screen.blit(wb_image1, (200,700))
    wq_image1 = pygame.transform.scale(pygame.image.load('img/white-queen.png'), scale_size)
    screen.blit(wq_image1, (300,700))
    wk_image1 = pygame.transform.scale(pygame.image.load('img/white-king.png'), scale_size)
    screen.blit(wk_image1, (400,700))
    wb_image2 = pygame.transform.scale(pygame.image.load('img/white-bishop.png'), scale_size)
    screen.blit(wb_image2, (500,700))
    wn_image2 = pygame.transform.scale(pygame.image.load('img/white-knight.png'), scale_size)
    screen.blit(wn_image2, (600,700))
    wr_image2 = pygame.transform.scale(pygame.image.load('img/white-rook.png'), scale_size)
    screen.blit(wr_image2, (700,700))
    for i in range(8):
        wp_image = pygame.transform.scale(pygame.image.load('img/white-pawn.png'), scale_size)
        screen.blit(wp_image, (i * 100, 600))
    
    #Black pieces
    br_image1 = pygame.transform.scale(pygame.image.load('img/black-rook.png'), scale_size)
    screen.blit(br_image1, (0,0))
    bn_image1 = pygame.transform.scale(pygame.image.load('img/black-knight.png'), scale_size)
    screen.blit(bn_image1, (100,0))
    bb_image1 = pygame.transform.scale(pygame.image.load('img/black-bishop.png'), scale_size)
    screen.blit(bb_image1, (200,0))
    bq_image1 = pygame.transform.scale(pygame.image.load('img/black-queen.png'), scale_size)
    screen.blit(bq_image1, (300,0))
    bk_image1 = pygame.transform.scale(pygame.image.load('img/black-king.png'), scale_size)
    screen.blit(bk_image1, (400,0))
    bb_image2 = pygame.transform.scale(pygame.image.load('img/black-bishop.png'), scale_size)
    screen.blit(bb_image2, (500,0))
    bn_image2 = pygame.transform.scale(pygame.image.load('img/black-knight.png'), scale_size)
    screen.blit(bn_image2, (600,0))
    br_image2 = pygame.transform.scale(pygame.image.load('img/black-rook.png'), scale_size)
    screen.blit(br_image2, (700,0))
    for i in range(8):
        bp_image = pygame.transform.scale(pygame.image.load('img/black-pawn.png'), scale_size)
        screen.blit(bp_image, (i * 100, 100))
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')
# Draw the board and pieces
draw_board()
place_images()


# Update the display
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
