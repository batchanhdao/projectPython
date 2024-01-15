
def Demo2():
    import pygame as pg
    from random import randint
    import pyttsx3
    import codecs

    troLy_assistant = pyttsx3.init()  # tạo đối tượng
    def NoiEnglish(text,i):
        assistant_say = text
        troLy_assistant.setProperty('rate', 120)  # thiết lập tốc độ giọng nói mới
        troLy_assistant.setProperty('volume', 1.0)
        voices = troLy_assistant.getProperty('voices')
        troLy_assistant.setProperty('voice', voices[i].id)
        # Save(assistant_say,"test.mp3")

        # dung ham say(x) de noi
        troLy_assistant.say(assistant_say)
        try:
            troLy_assistant.runAndWait()
        except:
            print('error')

    def draw_key():
        x = 50
        y = 330
        xuong_dong=0
        for key in keys:
            if key =="_!" and xuong_dong > 0:
                xuong_dong+=1
                x = 50 + 25*(xuong_dong-1)
                y += 60
            elif key =="_!" and xuong_dong == 0:
                x = 50 + 25*(xuong_dong)
                y += 60
                xuong_dong+=1
            elif key=="**":
                break
            else:
                x += draw_key_k(key,keys_K.get(key)[0],x,y,50,50,keys_K.get(key)[1],x+18,y+18)
        
        draw_key_k("SHIFT",keys_K.get("SHIFT")[0],10,510,80,50,keys_K.get("SHIFT")[1],10+12,510+18)
        draw_key_k("SHIFT",keys_K.get("SHIFT.")[0],700,510,80,50,keys_K.get("SHIFT.")[1],700+12,510+18)
        x = 75
        y += 60
        x += draw_key_k("CTRL",keys_K.get("CTRL")[0],x,y,80,50,keys_K.get("CTRL")[1],x+15,y+18)
        x += draw_key_k("ALT",keys_K.get("ALT")[0],x,y,80,50,keys_K.get("ALT")[1],x+20,y+18)
        x += draw_key_k("SPACE",keys_K.get("SPACE")[0],x,y,200,50,keys_K.get("SPACE")[1],x+60,y+18)
        x += draw_key_k("ALT",keys_K.get("ALT.")[0],x,y,80,50,keys_K.get("ALT.")[1],x+20,y+18)
        x += draw_key_k("CTRL",keys_K.get("CTRL.")[0],x,y,80,50,keys_K.get("CTRL.")[1],x+15,y+18)
        x += draw_key_k("BACK",keys_K.get("BACK")[0],x,y,80,50,keys_K.get("BACK")[1],x+13,y+18)

    def draw_key_k(key,color,x,y,weight,height,vien,x_key,y_key):
        font = pg.font.Font(None, 30)
        pg.draw.rect(screen,color,(x,y,weight,height),vien)
        text = font.render(key, True, black)
        screen.blit(text,(x_key,y_key))
        return weight+10

    def draw_text(key,color,x,y):
        font = pg.font.Font("D:\\tai lieu\\key_board\\arial-unicode-ms.ttf", 25)
        text = font.render(key, True, color)
        screen.blit(text,(x,y))
    def draw_text_viet(key,color,x,y):
        font = pg.font.Font("D:\\tai lieu\\key_board\\arial-unicode-ms.ttf", 25)
        key = key.encode("utf-8")
        text = font.render(key, True, color)
        screen.blit(text,(x,y))

    def draw_text_box(key,color,x,y,weight,height,vien,x_key,y_key):
        font = pg.font.Font("D:\\tai lieu\\key_board\\arial-unicode-ms.ttf", 25)
        pg.draw.rect(screen,color,(x,y,weight,height),vien)
        text = font.render(key, True, black)
        screen.blit(text,(x_key,y_key))
    
    # Initialize pg
    pg.init()

    # Set the window size
    size = (800, 650)
    screen = pg.display.set_mode(size)

    # Set the title of the window
    pg.display.set_caption("Keyboard Program")

    # Define some colors
    white = (255, 255, 255)
    # bg_picture = ['picture4', 'picture6', 'picture7', 'picture3', 'picture13', 'picture16', 'picture23', 'picture26', 'picture27']
    # change_pic = 0
    # check_change_pic = False
    # (218,165,32) (224,255,255) (255,255,224) (255,250,250) 
    tim = (255,153,255)
    black = (0, 0, 0)
    red = (255,0,0)
    green = (0,255,0)

    gif2 = pg.image.load(f'D:\\tai lieu\\key_board\\gif3.jpg').convert()
    gif3 = pg.image.load(f'D:\\tai lieu\\key_board\\gif4.jpg').convert()
    
    # gif1 = pg.image.load(f'D:\\tai lieu\\key_board\\gif5.gif').convert()
    # gif1 = pg.transform.scale2x(gif1)
    # screen.blit(gif1,(100,0))

    # Load the font
    # font = pg.font.Font("D:\\tai lieu\\key_board\\arial-unicode-ms.ttf", 18)

    # Create a list of the keys
    keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","_-", "+=", "_!", 
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "_!", 
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ": ;", "\" '", "_!", 
    "z", "x", "c", "v", "b", "n", "m", "<,", ">.", "?/",
    "**", "CTRL", "ALT", "SPACE", "SHIFT", "BACK","CTRL.", "ALT.", "SHIFT."]
    keys_K = {}
    for key in keys:
        keys_K[key] = [black,1]


    # Create a list to store the pressed keys
    pressed_keys = []

    # Create the "OK" button
    ok_button = pg.Rect(700, 500, 80, 50)

    # Create the text box
    text_box = pg.Rect(300, 250, 200, 50)

    # Create the entered text
    entered_text = ""
    # Run the game loop
    running = False
    # read file data_keyboard.txt
    english = []
    vietnamese = []
    with codecs.open("D:\\tai lieu\\key_board\\data_keyboard.txt",'r',encoding="utf-8") as file:
        while(True):
            words1 = file.readline().strip('\n').strip()
            words2 = file.readline().strip('\n').strip()
            if words1 == "": break
            vietnamese.append(words1)
            # print(words1)
            english.append(words2)
    ram = randint(0,len(english)-1)
    ds_tu = english[ram].split()
    tu_dung = []
    while not running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = True
            elif event.type == pg.KEYDOWN:
                for key in keys:
                    keys_K[key] = [black,1]
                if (event.unicode.isalpha() or event.unicode.isdigit()):
                    pressed_keys.append(event.unicode)
                    if len(entered_text) < 15:
                        entered_text += event.unicode
                    else: 
                        entered_text = entered_text[1:]
                        entered_text += event.unicode
                    keys_K[event.unicode.lower()] = [tim,10]

                elif event.key == pg.K_BACKSPACE:
                    entered_text = entered_text[:-1]
                    keys_K["BACK"] = [tim,10]

                elif event.key == pg.K_SPACE:
                    # entered_text += " "
                    if entered_text==ds_tu[0]:
                        tu_dung.append(ds_tu[0])
                        ds_tu.remove(ds_tu[0])
                        entered_text = ""
                    keys_K["SPACE"] = [tim,10]
                
                elif event.key == pg.K_LEFTBRACKET or event.key == pg.K_RIGHTBRACKET:
                    if event.key == pg.K_LEFTBRACKET: 
                        entered_text += "["
                        keys_K["["] = [tim,10]
                    else: 
                        entered_text +="]"
                        keys_K["]"] = [tim,10]
                
                elif event.key == pg.K_SEMICOLON or event.key == pg.K_QUOTE:
                    if event.mod & pg.KMOD_LSHIFT and event.key == pg.K_SEMICOLON: 
                        entered_text += ":"
                        keys_K[": ;"] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    elif event.key == pg.K_SEMICOLON: 
                        entered_text += ";"
                        keys_K[": ;"] = [tim,10]
                    elif event.mod & pg.KMOD_LSHIFT and  event.key == pg.K_QUOTE: 
                        entered_text += "\""
                        keys_K["\" '"] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    else: 
                        entered_text += "'"
                        keys_K["\" '"] = [tim,10]
                
                elif event.key == pg.K_COMMA or event.key == pg.K_PERIOD or event.key == pg.K_SLASH:
                    if event.mod & pg.KMOD_LSHIFT and event.key == pg.K_COMMA: 
                        entered_text += "<"
                        keys_K["<,"] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    elif event.key == pg.K_COMMA: 
                        entered_text += ","
                        keys_K["<,"] = [tim,10]
                    elif event.mod & pg.KMOD_LSHIFT and event.key == pg.K_PERIOD: 
                        entered_text += ">"
                        keys_K[">."] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    elif event.key == pg.K_PERIOD: 
                        entered_text += "."
                        keys_K[">."] = [tim,10]
                    elif event.mod & pg.KMOD_LSHIFT and event.key == pg.K_SLASH: 
                        entered_text += "?"
                        keys_K["?/"] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    else: 
                        entered_text += "/"
                        keys_K["?/"] = [tim,10]
            
                elif event.key == pg.K_MINUS or event.key == pg.K_EQUALS:
                    if event.mod & pg.KMOD_LSHIFT and event.key == pg.K_MINUS: 
                        entered_text += "_"
                        keys_K["_-"] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    elif event.key == pg.K_MINUS: 
                        entered_text += "-"
                        keys_K["_-"] = [tim,10]
                    elif event.mod & pg.KMOD_LSHIFT and  event.key == pg.K_EQUALS: 
                        entered_text += "+"
                        keys_K["+="] = [tim,10]
                        keys_K["SHIFT"] = [tim,10]
                    else: 
                        entered_text += "="
                        keys_K["+="] = [tim,10]

                elif event.key == pg.K_LCTRL:
                    keys_K["CTRL"] = [tim,10]
                    NoiEnglish(english[ram],0)
                elif event.key == pg.K_LALT:
                    keys_K["ALT"] = [tim,10]
                    ram = randint(0,len(english)-1)
                    ds_tu = english[ram].split()
                    tu_dung.clear()
                elif event.key == pg.K_LSHIFT:
                    keys_K["SHIFT"] = [tim,10]
                elif event.key == pg.K_RCTRL:
                    keys_K["CTRL."] = [tim,10]
                    NoiEnglish(english[ram],2)
                elif event.key == pg.K_RALT:
                    keys_K["ALT."] = [tim,10]
                    ram = randint(0,len(english)-1)
                    ds_tu = english[ram].split()
                    tu_dung.clear()
                    # check_change_pic = True
                    # change_pic += 1
                    
                elif event.key == pg.K_RSHIFT:
                    keys_K["SHIFT."] = [tim,10]

            elif event.type == pg.MOUSEBUTTONDOWN:
                if ok_button.collidepoint(event.pos):
                    print("OK button pressed")
                    print("Entered text:", entered_text)
                    entered_text = ""
                    pressed_keys = []

        # Clear the screen
        screen.fill(white)
        screen.blit(gif2,(30,50))
        screen.blit(gif3,(550,50))
        
        # if check_change_pic:
        #     bg = pg.image.load(f'D:\\tai lieu\\key_board\\picture\\{bg_picture[change_pic%len(bg_picture)]}.jpg').convert()
        #     bg = pg.transform.scale2x(bg)
        #     screen.blit(bg,(0,0))

        # Draw the keyboard
        draw_key()
        
        # Draw the text
        if len(tu_dung)>=7:
            draw_text(" ".join(tu_dung[:int(len(tu_dung)/2)]),green,400-len(" ".join(tu_dung[:int(len(tu_dung)/2)]))*10/2,120)
            draw_text(" ".join(tu_dung[int(len(tu_dung)/2):]),green,400-len(" ".join(tu_dung[int(len(tu_dung)/2):]))*10/2,150)
        else: draw_text(" ".join(tu_dung),green,400-len(" ".join(tu_dung))*10/2,150)
        if len(ds_tu)==0:
            ds_tu = vietnamese[ram].split()
            if len(ds_tu)>=7:
                draw_text_viet(" ".join(ds_tu[:int(len(ds_tu)/2)]),red,400-len(" ".join(ds_tu[:int(len(ds_tu)/2)]))*10/2,180)
                draw_text_viet(" ".join(ds_tu[int(len(ds_tu)/2):]),red,400-len(" ".join(ds_tu[int(len(ds_tu)/2):]))*10/2,210)
            else: draw_text_viet(" ".join(ds_tu),red,400-len(" ".join(ds_tu))*10/2,200)
        else:
            if len(ds_tu)>=7:
                draw_text(" ".join(ds_tu[:int(len(ds_tu)/2)]),red,400-len(" ".join(ds_tu[:int(len(ds_tu)/2)]))*10/2,180)
                draw_text(" ".join(ds_tu[int(len(ds_tu)/2):]),red,400-len(" ".join(ds_tu[int(len(ds_tu)/2):]))*10/2,210)
            else: draw_text(" ".join(ds_tu),red,400-len(" ".join(ds_tu))*10/2,200)
        # draw_text(" ".join(tu_dung),green,400-len(" ".join(tu_dung))*10/2,150)        

        # # Draw the "OK" button
        # pg.draw.rect(screen, black, ok_button, 1)
        # text = font.render("Nghe", True, black)
        # screen.blit(text, (725, 520))

        # Draw the text box
        draw_text_box(entered_text,tim,250,250,350,50,3,300,255)

        # Update the screen
        pg.display.update()


    # Close the window and quit.
    pg.quit()


Demo2()

