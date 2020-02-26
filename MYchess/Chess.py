import pygame


def peao_move_preto(x):
    global lista, pawn, P1, P2, P3, P4, P5, P6, P7, P8
    p0, pp = (x + 9, x + 11), (x + 10, x + 20)
    if pawn[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]]:
        for red in p0:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] != '':
                lista.append(red)
        for red in pp:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] == '':
                lista.append(red)
    if not(pawn[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]]):
        for red in p0:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] != '':
                lista.append(red)
        if x + 10 in menu_duplo and board[(x + 10) // 10 - 1][(x + 10) % 10 - 1] == '':
            lista.append(x + 10)
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def peao_move_branco(x):
    global lista, pawn, p1, p2, p3, p4, p5, p6, p7, p8
    p0, pp = (x - 9, x - 11), (x - 10, x - 20)
    if pawn[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]]:
        for red in p0:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] != '':
                lista.append(red)
        for red in pp:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] == '':
                lista.append(red)
    if not (pawn[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]]):
        for red in p0:
            if red in menu_duplo and board[red // 10 - 1][red % 10 - 1] != '':
                lista.append(red)
        if x - 10 in menu_duplo and board[(x - 10) // 10 - 1][(x - 10) % 10 - 1] == '':
            lista.append(x - 10)
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'branco' and yx in lista:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def bispo_move(x):
    global lista
    xstr = []
    for num in str(x):
        xstr.append(num)
    eixoy = int(xstr[0])
    eixox = int(xstr[1])
    if 8 - eixox <= eixoy - 1:
        cd = 8 - eixox
    else:
        cd = eixoy - 1
    if eixox - 1 <= eixoy - 1:
        ce = eixox - 1
    else:
        ce = eixoy - 1
    if 8 - eixox <= 8 - eixoy:
        bd = 8 - eixox
    else:
        bd = 8 - eixoy
    if eixox - 1 <= 8 - eixoy:
        be = eixox - 1
    else:
        be = 8 - eixoy

    pcd = [x - 9, x - 18, x - 27, x - 36, x - 45, x - 54, x - 63]
    pce = [x - 11, x - 22, x - 33, x - 44, x - 55, x - 66, x - 77]
    pbe = [x + 9, x + 18, x + 27, x + 36, x + 45, x + 54, x + 63]
    pbd = [x + 11, x + 22, x + 33, x + 44, x + 55, x + 66, x + 77]
    for n0 in range(0, cd):
        lista.append(pcd[n0])
    for n1 in range(0, ce):
        lista.append(pce[n1])
    for n2 in range(0, bd):
        lista.append(pbd[n2])
    for n3 in range(0, be):
        lista.append(pbe[n3])
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == bispo:
            lista.remove(yx)
        if validacao[board[yo][xo]] == 'branco' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == bispo_branco:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def cavalo_move(x):
    global lista
    p0 = x - 21, x - 19, x + 21, x + 19, x + 8, x - 8, x + 12, x - 12
    for red in p0:
        if red in menu_duplo:
            lista.append(red)
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == cavalo:
            lista.remove(yx)
        if validacao[board[yo][xo]] == 'branco' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == cavalo_branco:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def rainha_move(x):
    global lista
    xstr = []
    for num in str(x):
        xstr.append(num)
    eixoy = int(xstr[0])
    eixox = int(xstr[1])
    if 8 - eixox <= eixoy - 1:
        cd = 8 - eixox
    else:
        cd = eixoy - 1
    if eixox - 1 <= eixoy - 1:
        ce = eixox - 1
    else:
        ce = eixoy - 1
    if 8 - eixox <= 8 - eixoy:
        bd = 8 - eixox
    else:
        bd = 8 - eixoy
    if eixox - 1 <= 8 - eixoy:
        be = eixox - 1
    else:
        be = 8 - eixoy

    pcd = [x - 9, x - 18, x - 27, x - 36, x - 45, x - 54, x - 63]
    pce = [x - 11, x - 22, x - 33, x - 44, x - 55, x - 66, x - 77]
    pbd = [x + 11, x + 22, x + 33, x + 44, x + 55, x + 66, x + 77]
    pbe = [x + 9, x + 18, x + 27, x + 36, x + 45, x + 54, x + 63]
    for n0 in range(0, cd):
        lista.append(pcd[n0])
    for n1 in range(0, ce):
        lista.append(pce[n1])
    for n2 in range(0, bd):
        lista.append(pbd[n2])
    for n3 in range(0, be):
        lista.append(pbe[n3])

    direita, esquerda, baixo, cima = 8 - eixox, eixox - 1, 8 - eixoy, eixoy - 1

    pdireita = [x + 1, x + 2, x + 3, x + 4, x + 5, x + 6, x + 7]
    pesquerda = [x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7]
    pbaixo = [x + 10, x + 20, x + 30, x + 40, x + 50, x + 60, x + 70]
    pcima = [x - 10, x - 20, x - 30, x - 40, x - 50, x - 60, x - 70]
    for n0 in range(0, direita):
        lista.append(pdireita[n0])
    for n1 in range(0, esquerda):
        lista.append(pesquerda[n1])
    for n2 in range(0, baixo):
        lista.append(pbaixo[n2])
    for n3 in range(0, cima):
        lista.append(pcima[n3])
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == rainha:
            lista.remove(yx)
        if validacao[board[yo][xo]] == 'branco' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == rainha_branca:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def rei_move(x):
    global lista
    p0 = x + 9, x - 9, x + 11, x - 11, x - 10, x + 10, x + 1, x - 1

    for red in p0:
        if red in menu_duplo:
            lista.append(red)
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == rei:
            lista.remove(yx)
        if validacao[board[yo][xo]] == 'branco' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == rei_branco:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def torre_move(x):
    xstr = []
    global lista
    for num in str(x):
        xstr.append(num)
    eixoy = int(xstr[0])
    eixox = int(xstr[1])
    direita, esquerda, baixo, cima = 8 - eixox, eixox - 1, 8 - eixoy, eixoy - 1

    pdireita = [x + 1, x + 2, x + 3, x + 4, x + 5, x + 6, x + 7]
    pesquerda = [x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7]
    pbaixo = [x + 10, x + 20, x + 30, x + 40, x + 50, x + 60, x + 70]
    pcima = [x - 10, x - 20, x - 30, x - 40, x - 50, x - 60, x - 70]
    for n0 in range(0, direita):
        lista.append(pdireita[n0])
    for n1 in range(0, esquerda):
        lista.append(pesquerda[n1])
    for n2 in range(0, baixo):
        lista.append(pbaixo[n2])
    for n3 in range(0, cima):
        lista.append(pcima[n3])

    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        if validacao[board[yo][xo]] == 'preto' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == torre:
            lista.remove(yx)
        if validacao[board[yo][xo]] == 'branco' and yx in lista and \
                diciona222[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == torre_branca:
            lista.remove(yx)
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    for cube in lista:
        screen.blit(red_cube, (menu_duplo[cube]))


def xy_verde():
    global posicao_verde, yverde, xverde
    yverde, xverde = posicao_verde // 10 - 1, posicao_verde % 10 - 1


def turnos():
    global turno
    if validacao[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == 'branco':
        turno = True
    if validacao[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == 'preto':
        turno = False


def draw_screen(d1):
    result = []
    xx, yy = 75, 70
    pygame.draw.rect(screen, ([0, 0, 200]), [50, 50, 600, 600])
    for c in range(50, 601, 150):
        for j in range(50, 601, 150):
            pygame.draw.rect(screen, (255, 255, 255), [c, j, 75, 75])
            pygame.draw.rect(screen, (255, 255, 255), [c + 75, j + 75, 75, 75])
    if d1:
        for n in range(0, 8):
            screen.blit(fonte_coord.render(f'{n + 1}', True, (0, 0, 0)), (25, yy))
            yy += 75
        for n in range(0, 8):
            screen.blit(fonte_coord.render(f'{n + 1}', True, (0, 0, 0)), (xx, 18))
            xx += 75
    linha = 0
    coluna = 0
    for b in range(64):
        yo, xo, yx = linha, coluna, int(str(linha + 1) + str(coluna + 1))
        screen.blit(diciona222[board[yo][xo]], menu_duplo[yx])
        result.append(board[yo][xo])
        if coluna == 7:
            coluna = 0
            linha += 1
        else:
            coluna += 1
    if 'R' not in result:
        pygame.draw.rect(screen, ([0, 0, 0]), [135, 290, 450, 100])
        screen.blit(fonte_coord.render('YOU WIN', True, (255, 0, 0)), (250, 300))
        screen.blit(fonte_coord.render('APERTE ESC PARA SAIR', True, (255, 0, 0)), (150, 350))
    if 'r' not in result:
        pygame.draw.rect(screen, ([0, 0, 0]), [135, 290, 450, 100])
        screen.blit(fonte_coord.render('YOU LOSE', True, (255, 0, 0)), (250, 300))
        screen.blit(fonte_coord.render('APERTE ESC PARA SAIR', True, (255, 0, 0)), (150, 350))


pygame.init()
peao, peao_branco, bispo, bispo_branco, cavalo, cavalo_branco, rainha, rainha_branca, rei, rei_branco, torre, \
     torre_branca, red_cube, green_cube, quadrado_nulo = pygame.image.load('peao.png'), pygame.image.load \
 ('peao_branco.png'), pygame.image.load('bispo.png'), pygame.image.load('bispo_branco.png'), pygame.image.load \
 ('cavalo.png'), pygame.image.load('cavalo_branco.png'), pygame.image.load('rainha.png'), pygame.image.load \
 ('rainha_branca.png'), pygame.image.load('rei.png'), pygame.image.load('rei_branco.png'), pygame.image.load \
 ('torre.png'), pygame.image.load('torre_branca.png'), pygame.image.load('quadrado_vermelho.png'), \
     pygame.image.load('quadrado_verde.png'), pygame.image.load('nulo.png')
P1, P2, P3, P4, P5, P6, P7, P8 = True, True, True, True, True, True, True, True
p1, p2, p3, p4, p5, p6, p7, p8 = True, True, True, True, True, True, True, True
pawn = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6, 'p7': p7, 'p8': p8,
       'P1': P1, 'P2': P2, 'P3': P3, 'P4': P4, 'P5': P5, 'P6': P6, 'P7': P7, 'P8': P8}
menu_duplo = {11: (58,   58), 12: (133,  58), 13: (208,  58), 14: (283,  58), 15: (358,  58),
              16: (433,  58), 17: (508,  58), 18: (583,  58), 21: (58,  133), 22: (133, 133),
              23: (208, 133), 24: (283, 133), 25: (358, 133), 26: (433, 133), 27: (508, 133),
              28: (583, 133), 31: (58,  208), 32: (133, 208), 33: (208, 208), 34: (283, 208),
              35: (358, 208), 36: (433, 208), 37: (508, 208), 38: (583, 208), 41: (58,  283),
              42: (133, 283), 43: (208, 283), 44: (283, 283), 45: (358, 283), 46: (433, 283),
              47: (508, 283), 48: (583, 283), 51: (58,  358), 52: (133, 358), 53: (208, 358),
              54: (283, 358), 55: (358, 358), 56: (433, 358), 57: (508, 358), 58: (583, 358),
              61: (58,  433), 62: (133, 433), 63: (208, 433), 64: (283, 433), 65: (358, 433),
              66: (433, 433), 67: (508, 433), 68: (583, 433), 71: (58,  508), 72: (133, 508),
              73: (208, 508), 74: (283, 508), 75: (358, 508), 76: (433, 508), 77: (508, 508),
              78: (583, 508), 81: (58,  583), 82: (133, 583), 83: (208, 583), 84: (283, 583),
              85: (358, 583), 86: (433, 583), 87: (508, 583), 88: (583, 583)}

board = [['T1', 'C1', 'B1',  'Q',  'R', 'B2', 'C2', 'T2'],
         ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
         ['t1', 'c1', 'b1',  'q',  'r', 'b2', 'c2', 't2']]
dicionario = {'T1': torre_move, 't1': torre_move, 'T2': torre_move, 't2': torre_move, 'C1': cavalo_move,
              'C2': cavalo_move, 'c1': cavalo_move, 'c2': cavalo_move, 'B1': bispo_move, 'B2': bispo_move,
              'b2': bispo_move, 'b1': bispo_move, 'Q': rainha_move, 'q': rainha_move, 'r': rei_move,
              'R': rei_move, 'P1': peao_move_preto, 'P2': peao_move_preto, 'P3': peao_move_preto,
              'P4': peao_move_preto, 'P5': peao_move_preto, 'P6': peao_move_preto, 'P7': peao_move_preto,
              'P8': peao_move_preto, 'p1': peao_move_branco, 'p2': peao_move_branco, 'p3': peao_move_branco,
              'p4': peao_move_branco, 'p5': peao_move_branco, 'p6': peao_move_branco, 'p7': peao_move_branco,
              'p8': peao_move_branco, '': 'nada'}
diciona222 = {'T1': torre, 't1': torre_branca, 'T2': torre, 't2': torre_branca, 'C1': cavalo, 'C2': cavalo,
              'c1': cavalo_branco, 'c2': cavalo_branco, 'B1': bispo, 'B2': bispo, 'b2': bispo_branco,
              'b1': bispo_branco, 'Q': rainha, 'q': rainha_branca, 'r': rei_branco, 'R': rei, 'P1': peao, 'P2': peao,
              'P3': peao, 'P4': peao, 'P5': peao, 'P6': peao, 'P7': peao, 'P8': peao, 'p1': peao_branco,
              'p2': peao_branco, 'p3': peao_branco, 'p4': peao_branco, 'p5': peao_branco, 'p6': peao_branco,
              'p7': peao_branco, 'p8': peao_branco, '': quadrado_nulo}
validacao = {'T1': 'preto', 'C1': 'preto', 'B1': 'preto',  'Q': 'preto',  'R': 'preto', 'B2': 'preto', 'C2': 'preto',
             'T2': 'preto', 'P1': 'preto', 'P2': 'preto', 'P3': 'preto', 'P4': 'preto', 'P5': 'preto', 'P6': 'preto',
             'P7': 'preto', 'P8': 'preto', '': 'nada', 'p1': 'branco', 'p2': 'branco', 'p3': 'branco', 'p4': 'branco',
             'p5': 'branco', 'p6': 'branco', 'p7': 'branco', 'p8': 'branco', 't1': 'branco', 'c1': 'branco',
             'b1': 'branco',  'q': 'branco',  'r': 'branco', 'b2': 'branco', 'c2': 'branco', 't2': 'branco'}
screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption('tabuleiro')
screen.fill([169, 169, 169])

pygame.font.init()
fonte_result = pygame.font.SysFont(pygame.font.get_default_font(), 30)
fonte_coord = pygame.font.SysFont(pygame.font.get_default_font(), 50)
done, v, turno, sapato, lista, posicao_verde, posicao_dps, xverde, yverde = False, True, True, True, [], 44, 44, 4, 4
draw_screen(v)
while not done:
    while not done:
        pygame.time.Clock().tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and sapato:
                draw_screen(v)
                screen.blit(green_cube, (menu_duplo[posicao_verde]))
            if event.type == pygame.KEYDOWN:
                xy_verde()
                try:
                    if event.key == pygame.K_RIGHT and sapato:
                        posicao_verde += 1
                        draw_screen(v)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if event.key == pygame.K_RIGHT and not sapato:
                        posicao_verde += 1
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                    if not turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                except KeyError:
                    posicao_verde -= 1
                    draw_screen(v)
                    screen.blit(green_cube, (menu_duplo[posicao_verde]))
                try:
                    if event.key == pygame.K_LEFT and sapato:
                        posicao_verde -= 1
                        draw_screen(v)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if event.key == pygame.K_LEFT and not sapato:
                        posicao_verde -= 1
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                    if not turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                except KeyError:
                    posicao_verde += 1
                    draw_screen(v)
                    screen.blit(green_cube, (menu_duplo[posicao_verde]))
                try:
                    if event.key == pygame.K_UP and sapato:
                        posicao_verde -= 10
                        draw_screen(v)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if event.key == pygame.K_UP and not sapato:
                        posicao_verde -= 10
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                    if not turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                except KeyError:
                    posicao_verde += 10
                    draw_screen(v)
                    screen.blit(green_cube, (menu_duplo[posicao_verde]))
                try:
                    if event.key == pygame.K_DOWN and not sapato:
                        posicao_verde += 10
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if event.key == pygame.K_DOWN and sapato:
                        posicao_verde += 10
                        draw_screen(v)
                        screen.blit(green_cube, (menu_duplo[posicao_verde]))
                    if turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                    if not turno:
                        pygame.draw.rect(screen, ([0, 0, 0]), [150, 650, 400, 50])
                        screen.blit(fonte_coord.render('Vez da próxima cor', True, (255, 255, 255)), (200, 655))
                except KeyError:
                    posicao_verde -= 10
                    draw_screen(v)
                    screen.blit(green_cube, (menu_duplo[posicao_verde]))
                if (event.key == pygame.K_DELETE or event.key == pygame.K_KP_ENTER) and (posicao_verde in lista) \
                        and not sapato:
                    if dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == peao_move_branco \
                            or dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] == peao_move_preto:
                        pawn[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]] = False
                    if board[yverde][xverde] != '':
                        board[yverde][xverde] = board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]
                    if board[yverde][xverde] == '':
                        board[yverde][xverde] = board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]
                    board[posicao_dps // 10 - 1][posicao_dps % 10 - 1] = ''
                    posicao_dps = 44
                    sapato = True
                    draw_screen(v)
                elif (event.key == pygame.K_DELETE or event.key == pygame.K_KP_ENTER) and sapato and turno:
                    xy_verde()
                    if board[yverde][xverde] != '' and validacao[board[yverde][xverde]] == 'branco':
                        lista = []
                        posicao_dps = posicao_verde
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        sapato, turno = False, False
                elif (event.key == pygame.K_DELETE or event.key == pygame.K_KP_ENTER) and sapato and not turno:
                    xy_verde()
                    if board[yverde][xverde] != '' and validacao[board[yverde][xverde]] == 'preto':
                        lista = []
                        posicao_dps = posicao_verde
                        draw_screen(v)
                        dicionario[board[posicao_dps // 10 - 1][posicao_dps % 10 - 1]](posicao_dps)
                        sapato, turno = False, True
                elif (event.key == pygame.K_DELETE or event.key == pygame.K_KP_ENTER) and not sapato:
                    sapato, turno = True, True
                    draw_screen(v)
                    screen.blit(green_cube, (menu_duplo[posicao_verde]))
                if event.key == pygame.K_ESCAPE:
                    done = True
        pygame.display.flip()
    pygame.quit()