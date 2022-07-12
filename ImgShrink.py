from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys






if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Set a path to Img and scale in arguments')
        print('Example:\n ImgShrink.py C:\\Img 10')
        exit(0)

    path = sys.argv[1]
    scale = int(sys.argv[2])

    try:
        orig_img = pygame.image.load(path)
        img = pygame.image.load(path)
    except:
        print('Invalid arguments')
        exit(0)
    pygame.init()
    screenWidth = img.get_width()
    screenHeight = img.get_height()

    # screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ImgShrink")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)





    def blur(img: pygame.image):
        for y in range(screenHeight):
            for x in range(screenWidth):
                if x == 0 or y == 0 or x == screenWidth - 1 or y == screenHeight - 1:
                    continue

                r = img.get_at((x - 1, y))[0] + img.get_at((x + 1, y))[0] + img.get_at((x, y + 1))[0] + \
                    img.get_at((x, y - 1))[0]
                g = img.get_at((x - 1, y))[1] + img.get_at((x + 1, y))[1] + img.get_at((x, y + 1))[1] + \
                    img.get_at((x, y - 1))[1]
                b = img.get_at((x - 1, y))[2] + img.get_at((x + 1, y))[2] + img.get_at((x, y + 1))[2] + \
                    img.get_at((x, y - 1))[2]

                pix = (r / 4, g / 4, b / 4)
                # if (x+y) % 2 == 1:
                img.set_at((x, y), pix)
        return img



    def shrink(img: pygame.image, scale: int):

        n = screenWidth//scale
        m = screenHeight//scale

        squares = [[[] for i in range(m)] for j in range(n)]

        for sq_y in range(m):
            for sq_x in range(n):
                col_sum = [0, 0, 0]
                for i in range(scale):
                    for j in range(scale):
                        x = sq_x * scale + j
                        y = sq_y * scale + i
                        col_sum[0] += img.get_at((x, y))[0]
                        col_sum[1] += img.get_at((x, y))[1]
                        col_sum[2] += img.get_at((x, y))[2]
                squares[sq_x][sq_y] = col_sum

        for i in range(len(squares)):
            for j in range(len(squares[0])):
                squares[i][j][0] //= scale**2
                squares[i][j][1] //= scale**2
                squares[i][j][2] //= scale**2

        for y in range(screenHeight):
            for x in range(screenWidth):
                ptr_x = x//scale
                ptr_y = y//scale
                if x//scale >= n:
                    ptr_x -= 1
                if y//scale >= m:
                    ptr_y -= 1
                img.set_at((x, y), squares[ptr_x][ptr_y])

        return img



    img = shrink(img, scale)



    # screen.blit(img, (0, 0))


    pygame.image.save(img, 'NewImg_.jpg')

    print('Image saved successfully as NewImg_.jpg')

    # clock = pygame.time.Clock()
    # fps = 60
    # running = True
    # while running:
    #     # screen.fill(WHITE)
    #
    #     pygame.display.update()
    #     clock.tick(fps)
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_s:
    #                 running = False
    #         if event.type == pygame.QUIT:
    #             running = False
