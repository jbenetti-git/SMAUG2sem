import pygame

# ------BLOCO de Celas----------


def desenhar_bg1():
    background1 = [
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "AAAAAAAAAAAAAAAAABAAAAABAAAAAAAAAAAAAAAA",
        "AAAAAAAAAAAAAAAAABAAAAABAAAAAAAAAAAAAAAA",
        "........................................",
        "........................................",
        "........................................",
        ".....BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        ".....BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        ".....AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        ".....AAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA",
        ".....AAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA",
        "........................................",
        "........................................",
        "........................................",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))
            elif letra == 'B':
                tela.blit(background_black, (x, y))


def desenhar_prop1():
    global torch_count
    background1 = [
        ".........................#..............",
        ".a..hh.hh.hh.hh.h..hh.h..#..............",
        ".........................#..............",
        ".........................#..............",
        ".........................#..............",
        ".........................#..............",
        ".........................#..............",
        ".........................#..............",
        ".........................#..............",
        "......hh.hh.hh.hh.h..hh..#..............",
        ".........................#..............",
        ".........................#..............",
        "............A............#..............",
        ".........................#..............",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == 'a':
                tela.blit(door, (x, y))
            elif letra == 'h':
                tela.blit(bars_l, (x, y))

    if torch_count + 1 >= 36:
        torch_count = 0
    tela.blit(torch[torch_count // 6], (180, 100))
    tela.blit(torch[torch_count // 6], (575, 100))
    tela.blit(torch[torch_count // 6], (960, 100))
    tela.blit(torch[torch_count // 6], (705, 605))
    torch_count += 1

    tela.blit(bodies, (-100, 500))
    tela.blit(body7, (1375, 150))


def desenhar_luz1():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    #luz_surface.blit(luz_g, (-350, -250))
    luz_surface.blit(luz_a, (-230, -320))
    luz_surface.blit(luz_a, (160, -320))
    luz_surface.blit(luz_a, (545, -320))
    luz_surface.blit(luz_a, (280, 200))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_1():
    global sound_control, interaction, chat_count, char_pos_x, char_pos_y, char_mov_direita, char_mov_esquerda, char_mov_baixo, char_mov_cima, level, spawn, teclas

    if char_pos_x <= 0:
        char_pos_x = 1
    if char_pos_x >= 1540:
        char_pos_x = 1539
    if char_pos_y <= 130:
        char_pos_y = 131
    if char_pos_y >= 832:
        char_pos_y = 831
    if char_pos_y >= 320 and char_pos_y <= 645 and char_pos_x >= 260:
        if char_pos_y <= 480 and not char_mov_direita:
            char_pos_y = 319
        if char_pos_y >= 480 and not char_mov_direita:
            char_pos_y = 644
        if char_pos_y <= 480 and char_mov_direita and char_pos_x <= 270:
            char_pos_x = 259
        if char_pos_y >= 480 and char_mov_direita and char_pos_x <= 270:
            char_pos_x = 259
    if char_pos_y >= 640 and char_pos_y <= 712 and char_pos_x >= 1144 and char_pos_x <= 1256:
        if teclas[pygame.K_e]:
            level = 1
            spawn = 2
            sound_control = 0
    if char_pos_x >= 1000 and char_pos_x <= 1124 and char_pos_y <= 170 and char_pos_y >= 128:
        if teclas[pygame.K_e]:
            level = 3
            spawn = 2
            sound_control = 0
    if char_pos_x >= 1380 and char_pos_x <= 1500 and char_pos_y <= 170 and char_pos_y >= 128:
        if teclas[pygame.K_e]:
            level = 4
            spawn = 2
            sound_control = 0
    if char_pos_x >= 30 and char_pos_x <= 161 and char_pos_y <= 170 and char_pos_y >= 128:
        if teclas[pygame.K_e] and chave1_c == 1:
            level = 5
            spawn = 2
            sound_control = 0
        elif teclas[pygame.K_e] and chave1_c == 0 and chave2_c == 0:
            interaction = 1
        elif teclas[pygame.K_e] and chave1_c == 0 and chave2_c == 1:
            interaction = 2


def interaction_1():
    global teclas, chave1_c, interaction, chat_count, sound_control

    if char_pos_x <= 192 and char_pos_y >= 666 and char_pos_y <= 780:
        if teclas[pygame.K_e]:
            chave1_c = 1

    if interaction == 1:
        if sound_control == 0:
            door_lock_sound.play()
            print(sound_control)
            sound_control = 1
            print(sound_control)
        if chat_count <= 300:
            tela.blit(chat_interaction[1], (0, 524))
            chat_count += 1
            print(chat_count)
        else:
            chat_count = 0
            interaction = 0

    if interaction == 2:
        if sound_control == 0:
            door_lock_sound.play()
            print(sound_control)
            sound_control = 1
            print(sound_control)
        if chat_count <= 300:
            tela.blit(chat_interaction[2], (0, 524))
            chat_count += 1
            print(chat_count)
        else:
            chat_count = 0
            interaction = 0

# ------Cela1----------


def desenhar_cela1():
    background1 = [
        "........................................",
        "........................................",
        "..........AAAAAA........................",
        "..........AAAAAA........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "............BB..........................",
        "............BB..........................",
        "........................................",
        "........................................",
        "........................................",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background_black, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))
            elif letra == 'B':
                tela.blit(background, (x, y))


def desenhar_luz_cela1():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    luz_surface.blit(luz_vela, (540, - 150))
    luz_surface.blit(luz_vela, (500, - 170))
    luz_surface.blit(luz_vela, (550, - 100))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_cela1():
    global sound_control, char_pos_x, char_pos_y, level, spawn, teclas

    if char_pos_x <= 627:
        char_pos_x = 628
    if char_pos_x >= 973:
        char_pos_x = 972
    if char_pos_y <= 211:
        char_pos_y = 212
    if char_pos_x <= 756 or char_pos_x >= 848:
        if char_pos_y >= 512:
            char_pos_y = 513
    if char_pos_x >= 757 and char_pos_x <= 847:
        if char_pos_y >= 512:
            if char_pos_x <= 800:
                if char_pos_x <= 760:
                    char_pos_x = 761
            if char_pos_x > 800:
                if char_pos_x >= 844:
                    char_pos_x = 843
        if char_pos_y >= 638:
            char_pos_y = 637
    if char_pos_y <= 304 and char_pos_x <= 697:
        char_pos_x = 696

    if char_pos_y > 620:
        level = 2
        spawn = 1
        sound_control = 0


def desenhar_prop_cela1():
    tela.blit(bed1, (610, 228))
    #tela.blit(chest_l, (968, 500))
    tela.blit(candle_s, (910, 228))
    tela.blit(candle_s, (930, 200))
    tela.blit(candle_s, (940, 255))
    tela.blit(candle_s, (890, 190))
    tela.blit(crack1, (700, 130))


def desenhar_cutscene1():
    global chat_count, cutscene, teclas, count

    count += 4
    print(count)
    if count <= 2180:
        tela.blit(full_black, (0, 0))
    if count > 500:
        tela.blit(intro_chat[chat_count//1600], (0, 524))
        chat_count += 4

        if chat_count + 1 >= 20080:
            chat_count = 0
            cutscene = 1
        if count >= 2180:
            tela.blit(char_parado, (696, 240))
            tela.blit(culprit, (char_pos_x + 100, char_pos_y))

    pygame.display.update()

    # for e in pygame.event.get():
    #     if e.type == pygame.KEYUP:
    #         if teclas[pygame.K_SPACE]:
    #             chat_count += 1600

# ------Cela2----------


def desenhar_cela2():
    background1 = [
        "........................................",
        "........................................",
        "..........AAAAAA........................",
        "..........AAAAAA........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "............BB..........................",
        "............BB..........................",
        "........................................",
        "........................................",
        "........................................",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background_black, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))
            elif letra == 'B':
                tela.blit(background, (x, y))


def desenhar_luz_cela2():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_cela2():
    global sound_control, char_pos_x, char_pos_y, level, spawn, teclas

    if char_pos_x <= 627:
        char_pos_x = 628
    if char_pos_x >= 973:
        char_pos_x = 972
    if char_pos_y <= 211:
        char_pos_y = 212
    if char_pos_x <= 756 or char_pos_x >= 848:
        if char_pos_y >= 512:
            char_pos_y = 513
    if char_pos_x >= 757 and char_pos_x <= 847:
        if char_pos_y >= 512:
            if char_pos_x <= 800:
                if char_pos_x <= 760:
                    char_pos_x = 761
            if char_pos_x > 800:
                if char_pos_x >= 844:
                    char_pos_x = 843
        if char_pos_y >= 638:
            char_pos_y = 637
    if char_pos_y <= 304 and char_pos_x <= 697:
        char_pos_x = 696

    if char_pos_y > 620:
        level = 2
        spawn = 3
        sound_control = 0


def desenhar_prop_cela2():
    tela.blit(bed1, (610, 228))
    tela.blit(saco2, (900, 150))
    tela.blit(body1, (800, 50))
    tela.blit(blood1, (800, 110))


# ------Cela3----------

def desenhar_cela3():
    background1 = [
        "........................................",
        "........................................",
        "..........AAAAAA........................",
        "..........AAAAAA........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "..........BBBBBB........................",
        "............BB..........................",
        "............BB..........................",
        "........................................",
        "........................................",
        "........................................",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background_black, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))
            elif letra == 'B':
                tela.blit(background, (x, y))


def desenhar_luz_cela3():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_cela3():
    global sound_control, char_pos_x, char_pos_y, level, spawn, teclas

    if char_pos_x <= 627:
        char_pos_x = 628
    if char_pos_x >= 973:
        char_pos_x = 972
    if char_pos_y <= 211:
        char_pos_y = 212
    if char_pos_x <= 756 or char_pos_x >= 848:
        if char_pos_y >= 512:
            char_pos_y = 513
    if char_pos_x >= 757 and char_pos_x <= 847:
        if char_pos_y >= 512:
            if char_pos_x <= 800:
                if char_pos_x <= 760:
                    char_pos_x = 761
            if char_pos_x > 800:
                if char_pos_x >= 844:
                    char_pos_x = 843
        if char_pos_y >= 638:
            char_pos_y = 637
    if char_pos_y <= 304:
        char_pos_y = 305
    if char_pos_y <= 520 and char_pos_y >= 460:
        if char_pos_x >= 938:
            char_pos_x = 937

    if char_pos_y > 620:
        level = 2
        spawn = 4
        sound_control = 0


def desenhar_prop_cela3():
    tela.blit(chest_l, (970, 510))
    tela.blit(body4, (665, 75))
    tela.blit(body8, (700, 250))


def interaction_2():
    global teclas, chave2_c

    if char_pos_x >= 890 and char_pos_y >= 430:
        if teclas[pygame.K_e]:
            chave2_c = 1

# -------Sala 2 -----------


def desenhar_bg2():
    background1 = [
        "BBBBBBBBAAAAAAAAABBBBBBBB.",
        "BBBBBBBBAAAAAAAAABBBBBBBB.",
        "BBBBBBBBAAAAAAAAABBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBB.........BBBBBBBB.",
        "BBBBBBBBBBB...BBBBBBBBBBB.",
        "BBBBBBBBBBB...BBBBBBBBBBB.",
        "BBBBBBBBBBB...BBBBBBBBBBB.",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))


def desenhar_prop2():
    global torch_count
    if torch_count + 1 >= 36:
        torch_count = 0
    tela.blit(torch[torch_count // 6], (675, 100))
    tela.blit(torch[torch_count // 6], (855, 100))
    torch_count += 1

    tela.blit(door, (730, 64))
    tela.blit(body2, (900, -40))
    tela.blit(body3, (600, 200))
    tela.blit(body5, (500, 450))
    tela.blit(body6, (800, 100))


def desenhar_luz2():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    luz_surface.blit(luz_a, (260, -320))
    luz_surface.blit(luz_a, (440, -320))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_2():
    global interaction, sound_control, char_pos_x, char_pos_y, char_mov_direita, char_mov_esquerda, char_mov_baixo, char_mov_cima, level, spawn, teclas

    if char_pos_x <= 501:
        char_pos_x = 500
    if char_pos_x >= 1039:
        char_pos_x = 1038
    if char_pos_y <= 130:
        char_pos_y = 131
    if char_pos_x > 848 or char_pos_x < 659:
        if char_pos_y >= 636:
            char_pos_y = 635
    elif char_pos_x <= 848 and char_pos_x >= 659:
        if char_pos_y > 800:
            level = 2
            spawn = 5
            sound_control = 0
    if char_pos_x >= 712 and char_pos_x <= 810 and char_pos_y <= 170:
        if teclas[pygame.K_e] and chave2_c == 1:
            level = 6
            spawn = 2
            sound_control = 0
        elif teclas[pygame.K_e] and chave2_c == 0:
            interaction = 2

# -------Sala 3 -----------


def desenhar_bg3():
    background1 = [
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "BBBBBBBBBBB...BBBBBBBBBBB...............",
        "BBBBBBBBBBB...BBBBBBBBBBB...............",
        "BBBBBBBBBBB...BBBBBBBBBBB...............",
    ]
    for linha in range(len(background1)):
        for coluna in range(len(background1[linha])):
            letra = background1[linha][coluna]
            x = coluna * tile_largura
            y = linha * tile_altura
            if letra == '.':
                tela.blit(background, (x, y))
            elif letra == 'A':
                tela.blit(wall_brick1, (x, y))


def desenhar_prop3():
    # global torch_count
    # if torch_count + 1 >= 36:
    #     torch_count = 0
    # tela.blit(torch[torch_count // 6], (180, 100))
    # tela.blit(torch[torch_count // 6], (575, 100))
    # tela.blit(torch[torch_count // 6], (960, 100))
    # tela.blit(torch[torch_count // 6], (705, 605))
    # torch_count += 1

    tela.blit(pentagram, (365, -50))

    tela.blit(candle_s, (440, 255))
    tela.blit(candle_s, (1000, 255))
    tela.blit(candle_s, (720, 140))
    tela.blit(candle_s, (540, 500))
    tela.blit(candle_s, (925, 520))
    tela.blit(candle_s, (620, 240))
    tela.blit(candle_s, (824, 230))
    tela.blit(candle_s, (881, 350))
    tela.blit(candle_s, (724, 415))
    tela.blit(candle_s, (568, 346))


def desenhar_luz3():
    luz_surface = pygame.Surface((tela_largura, tela_altura))
    luz_surface.fill(pygame.color.Color('Black'))
    luz_surface.blit(luz_m, (char_pos_x - 400, char_pos_y - 400))
    luz_surface.blit(luz_a, (50, -120))
    luz_surface.blit(luz_a, (610, -120))
    luz_surface.blit(luz_a, (330, -235))
    luz_surface.blit(luz_a, (150, 125))
    luz_surface.blit(luz_a, (535, 145))
    luz_surface.blit(luz_a, (230, -135))
    luz_surface.blit(luz_a, (434, -125))
    luz_surface.blit(luz_a, (491, -25))
    luz_surface.blit(luz_a, (334, 40))
    luz_surface.blit(luz_a, (178, -29))
    tela.blit(luz_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def boundaries_3():
    global velocidade, sound_control, char_pos_x, char_pos_y, char_mov_direita, char_mov_esquerda, char_mov_baixo, char_mov_cima, level, spawn, teclas

    if char_pos_x <= 0:
        char_pos_x = 1
    if char_pos_x >= 1540:
        char_pos_x = 1539
    if char_pos_y <= 608:
        char_pos_y = 607
    if char_pos_x > 848 or char_pos_x < 659:
        if char_pos_y >= 636:
            char_pos_y = 635
    elif char_pos_x <= 848 and char_pos_x >= 659:
        if char_pos_y > 800:
            level = 5
            spawn = 3
            sound_control = 0
            velocidade = 4


def desenhar_bloodlust():
    global blood_lust_count, bloodlust_pos_x, bloodlust_pos_y, end_count, level, sound_control


    sound_control += 1
    if sound_control <= 10:
        surprise_sound.play()
        door_close_sound.play()
        bloodlust_passos.play()

    end_count += 1
    if bloodlust_pos_y <= 250:
        if blood_lust_count + 1 >= 24:
            blood_lust_count = 0
        tela.blit(bloodlust[blood_lust_count // 6], (bloodlust_pos_x, bloodlust_pos_y))
        blood_lust_count += 1
        print(blood_lust_count)

        bloodlust_pos_y += 2.5
    else:
        tela.blit(bloodlust[1], (bloodlust_pos_x, 255))
        bloodlust_passos.stop()
    if end_count >= 180:
        print(end_count)
        if end_count <= 190:
            bloodlust_roar.play()
        elif end_count >= 250:
            level = 7
            end_count = 0
            bloodlust_roar.stop()


def interaction_3():
    global teclas, interaction, chat_count, sound_control

    if interaction == 2:
        if sound_control == 0:
            door_lock_sound.play()
            print(sound_control)
            sound_control = 1
            print(sound_control)
        if chat_count <= 300:
            tela.blit(chat_interaction[2], (0, 524))
            chat_count += 1
            print(chat_count)
        else:
            chat_count = 0
            interaction = 0


# ------Geral----------

def consulta():
    global chat_count, em_consulta

    if chat_count <200:
        tela.blit(char_parado, (char_pos_x, char_pos_y))
        tela.blit(culprit, (char_pos_x + 100, char_pos_y))
        if level == 1:
            tela.blit(chat_cons[3], (0, 524))
        elif level == 3:
            tela.blit(chat_cons[1], (0, 524))
        elif level == 2 and chave1_c == 0:
            tela.blit(chat_cons[2], (0, 524))
        elif level == 2 and (chave1_c == 1 or chave2_c == 1):
            tela.blit(chat_cons[4], (0, 524))
        elif level == 4:
            tela.blit(chat_cons[5], (0, 524))
        else:
            tela.blit(chat_cons[0], (0, 524))
        chat_count += 1
    if chat_count >= 200:
        em_consulta = False
        chat_count = 0

    print(chat_count)
    pygame.display.update()


def desenhar_char():
    global passos_sound_control, char_passos, teclas, char_pos_x, char_pos_y,char_mov_direita, char_mov_esquerda, char_mov_baixo, char_mov_cima

    if teclas[pygame.K_LEFT]:
        char_pos_x -= velocidade
        char_mov_esquerda = True
        char_mov_direita = False
        #print(char_pos_x, char_pos_y)
    elif teclas[pygame.K_RIGHT]:
        char_pos_x += velocidade
        char_mov_esquerda = False
        char_mov_direita = True
        #print(char_pos_x, char_pos_y)
    elif teclas[pygame.K_UP]:
        char_pos_y -= velocidade
        char_mov_baixo = False
        char_mov_cima = True
        #print(char_pos_x, char_pos_y)
    elif teclas[pygame.K_DOWN]:
        char_pos_y += velocidade
        char_mov_baixo = True
        char_mov_cima = False
        #print(char_pos_x, char_pos_y)
    else:
        char_mov_esquerda = False
        char_mov_direita = False
        char_mov_baixo = False
        char_mov_cima = False
        char_passos = 0
        print(char_pos_x, char_pos_y)

    if char_passos + 1 >= 20:
        char_passos = 0

    if char_mov_esquerda:
        tela.blit(char_esquerda[char_passos//5], (char_pos_x, char_pos_y))
        char_passos += 1
        #print('esquerda')
    elif char_mov_direita:
        tela.blit(char_direita[char_passos//5], (char_pos_x, char_pos_y))
        char_passos += 1
        #print('direita')
    elif char_mov_cima:
        tela.blit(char_cima[char_passos//5], (char_pos_x, char_pos_y))
        char_passos += 1
        #print('cima')
    elif char_mov_baixo:
        tela.blit(char_baixo[char_passos//5], (char_pos_x, char_pos_y))
        char_passos += 1
        #print('baixo')
    else:
        tela.blit(char_parado, (char_pos_x, char_pos_y))

    if char_mov_cima or char_mov_direita or char_mov_baixo or char_mov_esquerda:
        passos_sound_control = 0
        if passos_sound_control == 0 and (not pygame.mixer.get_busy()):
            passos_sound.play()
    else:
        passos_sound.stop()
        passos_sound_control = 1


def desenharslash_d():
    global char_slash

    if char_slash > 9:
        char_slash = 0

    if char_slash <= 4:
        tela.blit(slash_d[0], (260, 220))
        char_slash += 1
        print('slash1')
    elif char_slash >= 5:
        tela.blit(slash_d[1], (260, 220))
        char_slash += 1
        print('slash2')

    pygame.display.update()


def desenharslash_e():
    global char_slash

    if char_slash > 9:
        char_slash = 0

    if char_slash <= 4:
        tela.blit(slash_e[0], (180, 220))
        char_slash += 1
        print('slash1')
    elif char_slash >= 5:
        tela.blit(slash_e[1], (180, 220))
        char_slash += 1
        print('slash2')

    pygame.display.update()


def draw_ending():
    global end_count, cred_pos_y, rodando
    end_count += 1
    tela.blit(full_black, (0, 0))

    if end_count >= 600:
        tela.blit(creditos, (0, cred_pos_y))
        cred_pos_y -= 0.5

    if cred_pos_y <= -1000:
        rodando = False



pygame.init()
tela_largura = 1600
tela_altura = 900
tile_largura = tela_largura // 25
tile_altura = tela_altura // 14
tela = pygame.display.set_mode((tela_largura, tela_altura), 0)
pygame.display.set_caption("SMAUG_ALPHA1")
rodando = True
em_consulta = False


# ------IMAGENS----------
background = pygame.image.load('sprites/floor3.png').convert()
background_black = pygame.image.load('sprites/black.png').convert()
wall_brick1 = pygame.image.load('sprites/wall_brick.png').convert()
char_direita = [pygame.image.load('sprites/Player Right1.png').convert_alpha(),
                pygame.image.load('sprites/Player Right2.png').convert_alpha(),
                pygame.image.load('sprites/Player Right3.png').convert_alpha(),
                pygame.image.load('sprites/Player Right2.png').convert_alpha()]
char_esquerda = [pygame.image.load('sprites/Player Left1.png').convert_alpha(),
                 pygame.image.load('sprites/Player Left2.png').convert_alpha(),
                 pygame.image.load('sprites/Player Left3.png').convert_alpha(),
                 pygame.image.load('sprites/Player Left2.png').convert_alpha()]
char_cima = [pygame.image.load('sprites/Player Up1.png').convert_alpha(),
             pygame.image.load('sprites/Player Up2.png').convert_alpha(),
             pygame.image.load('sprites/Player Up3.png').convert_alpha(),
             pygame.image.load('sprites/Player Up2.png').convert_alpha()]
char_baixo = [pygame.image.load('sprites/Player Down1.png').convert_alpha(),
              pygame.image.load('sprites/Player Down2.png').convert_alpha(),
              pygame.image.load('sprites/Player Down3.png').convert_alpha(),
              pygame.image.load('sprites/Player Down2.png').convert_alpha()]
char_parado = pygame.image.load('sprites/Player Down2.png').convert_alpha()
slash_d = [pygame.image.load('sprites/slash_1.png').convert_alpha(), pygame.image.load('sprites/slash_2.png').convert_alpha()]
slash_e = [pygame.image.load('sprites/slash_1_e.png').convert_alpha(), pygame.image.load('sprites/slash_2_e.png').convert_alpha()]
luz_m = pygame.image.load('sprites/luz3.png').convert_alpha()
luz_g = pygame.image.load('sprites/luz4.png').convert_alpha()
luz_p = pygame.image.load('sprites/luz5.png').convert_alpha()
luz_a = pygame.image.load('sprites/luz6.png').convert_alpha()
luz_vela = pygame.image.load('sprites/luz7.png').convert_alpha()
armor1 = pygame.transform.scale(pygame.image.load('sprites/armor1.png').convert_alpha(), (160, 160))
armor2 = pygame.transform.scale(pygame.image.load('sprites/armor2.png').convert_alpha(), (160, 160))
saco1 = pygame.transform.scale2x(pygame.image.load('sprites/sack.png').convert_alpha())
saco2 = pygame.image.load('sprites/sack2.png').convert_alpha()
mesa1 = pygame.transform.scale2x(pygame.image.load('sprites/table_vase.png').convert_alpha())
mesa2 = pygame.transform.scale2x(pygame.image.load('sprites/table_round.png').convert_alpha())
shelfe1 = pygame.transform.scale2x(pygame.image.load('sprites/shelfe1.png').convert_alpha())
bars_l = pygame.transform.scale2x(pygame.image.load('sprites/bars_l.png').convert_alpha())
menu1 = pygame.image.load('sprites/menu1.png').convert()
door = pygame.transform.scale2x(pygame.image.load('sprites/door1.png').convert_alpha())
culprit = pygame.transform.scale(pygame.image.load('sprites/culprit1.png').convert_alpha(), (40, 80))
chat_cons = [pygame.image.load('sprites/chat_teste.png').convert_alpha(),
             pygame.image.load('sprites/chat/ghost_cela_2.png').convert_alpha(),
             pygame.image.load('sprites/chat/ghost_sala1_1.png').convert_alpha(),
             pygame.image.load('sprites/chat/ghost_cela1.png').convert_alpha(),
             pygame.image.load('sprites/chat/ghost_with_key.png').convert_alpha(),
             pygame.image.load('sprites/chat/ghost_cela_3.png').convert_alpha()]
torch = [pygame.image.load('sprites/torch1.png').convert_alpha(),
         pygame.image.load('sprites/torch2.png').convert_alpha(),
         pygame.image.load('sprites/torch3.png').convert_alpha(),
         pygame.image.load('sprites/torch4.png').convert_alpha(),
         pygame.image.load('sprites/torch5.png').convert_alpha(),
         pygame.image.load('sprites/torch6.png').convert_alpha()]
table = pygame.transform.scale(pygame.image.load('sprites/table1.png').convert_alpha(), (192, 192))
bed1 = pygame.transform.scale2x(pygame.image.load('sprites/bed.png').convert_alpha())
chest_l = pygame.image.load('sprites/side_chest.png').convert_alpha()
candle_s = pygame.transform.scale2x(pygame.image.load('sprites/candle2.png').convert_alpha())
candle_m = pygame.image.load('sprites/candle1.png').convert_alpha()
crack1 = pygame.transform.scale(pygame.image.load('sprites/crack1.png').convert_alpha(), (128, 128))
intro_chat = [pygame.image.load('sprites/intro_chat_1.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_2.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_3.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_4.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_5.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_6.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_7.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_8.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_9.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_10.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_11.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_12.png').convert_alpha(),
              pygame.image.load('sprites/intro_chat_13.png').convert_alpha()]
full_black = pygame.image.load('sprites/full_black.png').convert()
bodies = pygame.transform.scale(pygame.image.load('sprites/bodies1.png').convert_alpha(), (437, 315))
bonepile = pygame.image.load('sprites/BonePile.png').convert_alpha()
body1 = pygame.transform.scale(pygame.image.load('sprites/body1.png').convert_alpha(), (250, 250))
body2 = pygame.transform.scale(pygame.image.load('sprites/body2.png').convert_alpha(), (250, 250))
body3 = pygame.transform.scale(pygame.image.load('sprites/body3.png').convert_alpha(), (250, 250))
body4 = pygame.transform.scale(pygame.image.load('sprites/body4.png').convert_alpha(), (350, 350))
body5 = pygame.transform.scale(pygame.image.load('sprites/body5.png').convert_alpha(), (250, 250))
body6 = pygame.transform.scale(pygame.image.load('sprites/body6.png').convert_alpha(), (250, 250))
body7 = pygame.transform.scale(pygame.image.load('sprites/body7.png').convert_alpha(), (250, 250))
body8 = pygame.transform.scale(pygame.image.load('sprites/body8.png').convert_alpha(), (250, 500))
blood1 = pygame.transform.scale(pygame.image.load('sprites/blood1.png').convert_alpha(), (250, 250))
chave1 = pygame.transform.scale(pygame.image.load('sprites/key1.png').convert_alpha(), (50, 50))
chave2 = pygame.transform.scale(pygame.image.load('sprites/key2.png').convert_alpha(), (50, 50))
chat_interaction = [pygame.image.load('sprites/chat/kid_find_key_1.png').convert(),
                    pygame.image.load('sprites/chat/door_lock1.png').convert(),
                    pygame.image.load('sprites/chat/door_lock2.png').convert(),
                    pygame.image.load('sprites/chat/kid_find_key_2.png').convert()]
pentagram = pygame.transform.scale(pygame.image.load('sprites/pentagram.png').convert_alpha(), (800, 800))
bloodlust = [pygame.transform.scale(pygame.image.load('sprites/b_lust/B-lust_Down1.png').convert_alpha(), (192, 192)),
             pygame.transform.scale(pygame.image.load('sprites/b_lust/B-lust_Down2.png').convert_alpha(), (192, 192)),
             pygame.transform.scale(pygame.image.load('sprites/b_lust/B-lust_Down3.png').convert_alpha(), (192, 192)),
             pygame.transform.scale(pygame.image.load('sprites/b_lust/B-lust_Down2.png').convert_alpha(), (192, 192))]
creditos = pygame.image.load('sprites/creditos.png').convert_alpha()

#---------AUDIO---------------

door_lock_sound = pygame.mixer.Sound('sprites/doorlock.wav')
door_close_sound = pygame.mixer.Sound('sprites/doorclose.wav')
passos_sound = pygame.mixer.Sound('sprites/passos2.wav')
surprise_sound = pygame.mixer.Sound('sprites/surprise.wav')
bloodlust_passos = pygame.mixer.Sound('sprites/bloodlust_passos.wav')
bloodlust_roar = pygame.mixer.Sound('sprites/bloodlust_roar.wav')

door_close_sound.set_volume(0.1)
passos_sound.set_volume(0.5)
surprise_sound.set_volume(0.25)
bloodlust_passos.set_volume(0.25)
bloodlust_roar.set_volume(0.1)




# ------VARIAVEIS--------
clock = pygame.time.Clock()
chat_count = 0
char_pos_x = 1216
char_pos_y = 642
char_largura = 64
char_altura = 64
velocidade = 4
char_mov_direita = False
char_mov_esquerda = False
char_mov_cima = False
char_mov_baixo = False
char_passos = 0
char_slash = 0
torch_count = 0
torch_x = 0
torch_y = 0
level = 0
spawn = 0
cutscene = 0
count = 0
chave1_c = 0
chave2_c = 0
k_count = 0
k2_count = 0
event_count = 0
interaction = 0
sound_control = 0
passos_sound_control = 0
blood_lust_count = 0
bloodlust_pos_x = 700
bloodlust_pos_y = -100
end_count = 0
cred_pos_y = 900

# --------LOOP-PRINCIPAL--------

while rodando:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    # ------------------LEVEL0 - Menu--------------------

    if level == 0:
        tela.blit(menu1, (0, 0))
        pygame.display.update()
        if teclas[pygame.K_SPACE]:
            level = 1
            spawn = 1

    # ------------------LEVEL1 - Cela1--------------------

    if level == 1:
        if spawn == 1:
            char_pos_x = 696
            char_pos_y = 240
            spawn = 0
        if spawn == 2:
            char_pos_x = 793
            char_pos_y = 505
            spawn = 0

        desenhar_cela1()
        desenhar_prop_cela1()
        desenhar_luz_cela1()
        boundaries_cela1()
        if cutscene == 1:
            if not em_consulta:
                desenhar_char()
                if teclas[pygame.K_c]:
                    em_consulta = True
                    print("em consulta")
            elif em_consulta:
                consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 600 and char_pos_y >= 392:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 524))
            else:
                k_count = 610

        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 600:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 524))
            else:
                k2_count = 610

        if cutscene == 1:
            pygame.display.update()

        if cutscene == 0:
            desenhar_cutscene1()


    # ------------------LEVEL2 - Bloco de Celas--------------------

    if level == 2:
        if spawn == 1:
            char_pos_x = 1216
            char_pos_y = 642
            spawn = 0
        if spawn == 3:
            char_pos_x = 1084
            char_pos_y = 151
            spawn = 0
        if spawn == 4:
            char_pos_x = 1465
            char_pos_y = 151
            spawn = 0
        if spawn == 5:
            if sound_control == 0:
                door_close_sound.play()
                sound_control = 1
            char_pos_x = 100
            char_pos_y = 156
            spawn = 0

        desenhar_bg1()
        desenhar_prop1()
        desenhar_luz1()
        boundaries_1()
        interaction_1()

        if not em_consulta:
            desenhar_char()
            if teclas[pygame.K_c]:
                em_consulta = True
        elif em_consulta:
            consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 1000:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 0))
            else:
                k_count = 1010
        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 1000:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 524))
            else:
                k2_count = 1010

        pygame.display.update()

    # ------------------LEVEL3 - Cela2--------------------

    if level == 3:
        if spawn == 1:
            char_pos_x = 696
            char_pos_y = 240
            spawn = 0
        if spawn == 2:
            char_pos_x = 793
            char_pos_y = 505
            spawn = 0

        desenhar_cela2()
        desenhar_prop_cela2()
        desenhar_luz_cela2()
        boundaries_cela2()

        if not em_consulta:
            desenhar_char()
            if teclas[pygame.K_c]:
                em_consulta = True
                print("em consulta")
        elif em_consulta:
            consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 1000:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 524))
            else:
                k_count = 1010
        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 1000:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 524))
            else:
                k2_count = 1010

        pygame.display.update()

    # ------------------LEVEL4 - Cela3--------------------

    if level == 4:
        if spawn == 1:
            char_pos_x = 696
            char_pos_y = 240
            spawn = 0
        if spawn == 2:
            char_pos_x = 793
            char_pos_y = 505
            spawn = 0

        desenhar_cela3()
        desenhar_prop_cela3()
        desenhar_luz_cela3()
        boundaries_cela3()
        interaction_2()

        if not em_consulta:
            desenhar_char()
            if teclas[pygame.K_c]:
                em_consulta = True
                print("em consulta")
        elif em_consulta:
            consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 1000:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 524))
            else:
                k_count = 1010
        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 1000:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 0))
            else:
                k2_count = 1010

        pygame.display.update()

    # ------------LEVEL5 - SALA2------------

    if level == 5:
        if sound_control == 0:
            door_close_sound.play()
            sound_control = 1
        if spawn == 2:
            char_pos_x = 772
            char_pos_y = 727
            spawn = 0
        if spawn == 3:
            char_pos_x = 772
            char_pos_y = 175
            spawn = 0

        desenhar_bg2()
        desenhar_prop2()
        boundaries_2()
        desenhar_luz2()
        interaction_3()

        if not em_consulta:
            desenhar_char()
            if teclas[pygame.K_c]:
                em_consulta = True
        elif em_consulta:
            consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 1000:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 524))
            else:
                k_count = 1010
        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 1000:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 524))
            else:
                k2_count = 1010

        pygame.display.update()

    # ------------LEVEL6 - SALA3------------

    if level == 6:
        velocidade = 8
        if sound_control == 0:
            door_close_sound.play()
            sound_control = 1
        if spawn == 2:
            char_pos_x = 772
            char_pos_y = 727
            spawn = 0

        desenhar_bg3()
        desenhar_prop3()
        boundaries_3()
        desenhar_bloodlust()
        desenhar_luz3()

        if not em_consulta:
            desenhar_char()
            if teclas[pygame.K_c]:
                em_consulta = True
        elif em_consulta:
            consulta()

        if chave1_c == 1:
            tela.blit(chave1, (50, 800))
            k_count += 4
            if k_count <= 1000:
                tela.blit(chave1, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[0], (0, 524))
            else:
                k_count = 1010
        if chave2_c == 1:
            tela.blit(chave2, (100, 800))
            k2_count += 4
            if k2_count <= 1000:
                tela.blit(chave2, (char_pos_x + 50, char_pos_y - 50))
                tela.blit(chat_interaction[3], (0, 524))
            else:
                k2_count = 1010

        pygame.display.update()

    if level == 7:
        draw_ending()
        pygame.display.update()
