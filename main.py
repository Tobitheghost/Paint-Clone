from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Art Util")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRIDE_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for j in range(COLS + 1):
            pygame.draw.line(win, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


def progress_bar(progress, total):
    bar = 0
    percent = (10 / float(total))
    if progress % percent == 0:
        bar += 10
        print(f"█ {bar}%")


run = True
image = Image.new('RGBA', (WIDTH, HEIGHT - TOOLBAR_HEIGHT))
print_image = ImageDraw.Draw(image)
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
drawing_color2 = (255, 255, 254)
numbers = 0
x = 0
LOADING_MAX = COLS * ROWS
LOADING_MAX = LOADING_MAX/10

COLOR_SHIFT1 = 255
COLOR_SHIFT2 = 168
COLOR_SHIFT3 = 126
COLOR_SHIFT4 = 84
COLOR_SHIFT5 = 42
COLOR_SHIFT6 = 0

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
Button_x = 10

buttons = [
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 0)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (7, 7, 7)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (14, 14, 14)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (21, 21, 21)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (28, 28, 28)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (35, 35, 35)),
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (42, 42, 42)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (49, 49, 49)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (56, 56, 56)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (63, 63, 63)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (70, 70, 70)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (77, 77, 77)),
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (84, 84, 84)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (92, 92, 92)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (99, 99, 99)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (106, 106, 106)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (113, 113, 113)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (120, 120, 120)),
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (127, 127, 127)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (134, 134, 134)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (141, 141, 141)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (148, 148, 148)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (155, 155, 155)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (162, 162, 162)),
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (169, 169, 169)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (177, 177, 177)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (184, 184, 184)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (191, 191, 191)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (198, 198, 198)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (205, 205, 205)),
    Button(Button_x * 1, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (212, 212, 212)),
    Button(Button_x * 2, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (219, 219, 219)),
    Button(Button_x * 3, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (226, 226, 226)),
    Button(Button_x * 4, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (233, 233, 233)),
    Button(Button_x * 5, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (240, 240, 240)),
    Button(Button_x * 6, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (247, 247, 247)),

    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (8, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (17, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (25, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (34, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (42, 0, 0)),
    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (51, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (59, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (68, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (76, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (85, 0, 0)),
    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (93, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (102, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (110, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (119, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (127, 0, 0)),
    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (136, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (144, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (153, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (161, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (170, 0, 0)),
    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (178, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (187, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (195, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (204, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (212, 0, 0)),
    Button(Button_x * 7, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (221, 0, 0)),
    Button(Button_x * 8, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (229, 0, 0)),
    Button(Button_x * 9, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (238, 0, 0)),
    Button(Button_x * 10, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (246, 0, 0)),
    Button(Button_x * 11, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (255, 0, 0)),

    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 8, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 17, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 25, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 34, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 42, 0)),
    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 51, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 59, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 68, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 76, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 85, 0)),
    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 93, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 102, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 110, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 119, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 127, 0)),
    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 136, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 144, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 153, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 161, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 170, 0)),
    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 178, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 187, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 195, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 204, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 212, 0)),
    Button(Button_x * 12, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 221, 0)),
    Button(Button_x * 13, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 229, 0)),
    Button(Button_x * 14, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 238, 0)),
    Button(Button_x * 15, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 246, 0)),
    Button(Button_x * 16, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 255, 0)),

    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 8)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 17)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 25)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 34)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 - 25), 10, 10, (0, 0, 42)),
    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 0, 51)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 0, 59)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 0, 68)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 0, 76)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 - 15), 10, 10, (0, 0, 85)),
    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 0, 93)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 0, 102)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 0, 110)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 0, 119)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 - 5), 10, 10, (0, 0, 127)),
    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 0, 136)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 0, 144)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 0, 153)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 0, 161)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 + 5), 10, 10, (0, 0, 170)),
    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 0, 178)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 0, 187)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 0, 195)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 0, 204)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 + 15), 10, 10, (0, 0, 212)),
    Button(Button_x * 17, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 0, 221)),
    Button(Button_x * 18, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 0, 229)),
    Button(Button_x * 19, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 0, 238)),
    Button(Button_x * 20, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 0, 246)),
    Button(Button_x * 21, (HEIGHT - TOOLBAR_HEIGHT / 2 + 25), 10, 10, (0, 0, 255)),
    Button(250, button_y, 50, 50, WHITE, "Erase"),
    Button(310, button_y, 50, 50, WHITE, "Clear"),
    Button(370, button_y, 50, 50, WHITE, "Print")
]


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:

                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color

                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

                    if button.text == "Print":
                        print(f'One second, printing out your image.\n')
                        print("__________")
                        picture_list = []
                        for i, row in enumerate(grid):
                            for j, pixel in enumerate(row):
                                if pixel == (255, 255, 254):
                                    pixel = (255, 255, 254, 0)
                                    print_image.rectangle((((j * PIXEL_SIZE, i * PIXEL_SIZE), (j * PIXEL_SIZE)+PIXEL_SIZE, (i * PIXEL_SIZE)+PIXEL_SIZE)), fill=pixel)
                                    x += 1
                                    pass
                                else:
                                    x += 1
                                    # print(pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                                    pixel2 = (pixel[0],pixel[1],pixel[2],255)
                                    print_image.rectangle((((j * PIXEL_SIZE, i * PIXEL_SIZE), (j * PIXEL_SIZE)+PIXEL_SIZE, (i * PIXEL_SIZE)+PIXEL_SIZE)), fill=pixel2)
                                    image.save('C:/Users/Tobiathan/PycharmProjects/pixel art/boop1.png', 'PNG')
                                if  x % LOADING_MAX == 0:
                                    print("█", end='')
                        drawing_color = BLACK
                        print("\nDone!")
                        image.show()

                    if button.text == "Erase":
                        drawing_color = (255, 255, 254)

        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color2
            except IndexError:
                for button in buttons:

                    if not button.clicked(pos):
                        continue
                    drawing_color2 = button.color

    draw(WIN, grid, buttons)

pygame.quit()