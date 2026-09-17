import pygame

pygame.init()

pygame.display.set_caption("my_game")

screenwidth = 800
screenhieght = 600

screen = pygame.display.set_mode((screenwidth,screenhieght), pygame.RESIZABLE)


black_square_img = pygame.image.load('black_square.png').convert()

black_square_img = pygame.transform.scale(black_square_img,
                                   (black_square_img.get_width() * 2,
                                    black_square_img.get_height() * 2))


player_img = pygame.image.load('player.png').convert()

player_img = pygame.transform.scale(player_img,
                                   (player_img.get_width() * 2,
                                    player_img.get_height() * 2))

player_img.set_colorkey((255,255,255))

mouse_indicator_img = pygame.image.load('mouse_indicator.png').convert()

mouse_indicator_img = pygame.transform.scale(mouse_indicator_img,
                                   (mouse_indicator_img.get_width() * 2,
                                    mouse_indicator_img.get_height() * 2))

mouse_indicator_img.set_colorkey((0,0,0))

metal_floor_img = pygame.image.load('metal_floor.png').convert()

metal_floor_img = pygame.transform.scale(metal_floor_img,
                                   (metal_floor_img.get_width() * 2,
                                    metal_floor_img.get_height() * 2))


fire_place_img = pygame.image.load('fire_place.png').convert()

fire_place_img = pygame.transform.scale(fire_place_img,
                                   (fire_place_img.get_width() * 2,
                                    fire_place_img.get_height() * 2))

fire_place_img.set_colorkey((0,0,0))

oven_img = pygame.image.load('oven.png').convert()

oven_img = pygame.transform.scale(oven_img,
                                   (oven_img.get_width() * 8,
                                    oven_img.get_height() * 8))

fire_place_img.set_colorkey((0,0,0))

inventory_rectangles = black_square_img

inventory_rectangles = pygame.transform.scale(inventory_rectangles,
                                   (inventory_rectangles.get_width() * 6,
                                    inventory_rectangles.get_height() * 1))


grey_square_img = pygame.image.load('grey_square.png').convert()

grey_square_img = pygame.transform.scale(grey_square_img,
                                   (grey_square_img.get_width() * 2,
                                    grey_square_img.get_height() * 2))


selected_grey_rectangle = grey_square_img

selected_grey_rectangle = pygame.transform.scale(selected_grey_rectangle,
                                   (selected_grey_rectangle.get_width() * 6,
                                    selected_grey_rectangle.get_height() * 1))

metal_wall_img = pygame.image.load('metal_wall.png').convert()

metal_wall_img = pygame.transform.scale(metal_wall_img,
                                   (metal_wall_img.get_width() * 2,
                                    metal_wall_img.get_height() * 2))


# metal_wall_img = pygame.transform.flip(metal_wall_img)


#kjdlsf

zoomed_black_square_img = pygame.image.load('black_square.png').convert()



zoomed_player_img = pygame.image.load('player.png').convert()

zoomed_player_img.set_colorkey((255,255,255))

zoomed_mouse_indicator_img = pygame.image.load('mouse_indicator.png').convert()


zoomed_mouse_indicator_img.set_colorkey((0,0,0))

zoomed_metal_floor_img = pygame.image.load('metal_floor.png').convert()

zoomed_fire_place_img = pygame.image.load('fire_place.png').convert()

zoomed_fire_place_img.set_colorkey((0,0,0))

zoomed_metal_wall_img = pygame.image.load('metal_wall.png').convert()


# zoomed_inventory_rectangles = black_square_img

# zoomed_inventory_rectangles = pygame.transform.scale(inventory_rectangles,
#                                    (inventory_rectangles.get_width() * 3,
#                                     inventory_rectangles.get_height() * 0.5))


# zoomed_grey_square_img = pygame.image.load('grey_square.png').convert()


# zoomed_selected_grey_rectangle = grey_square_img

# zoomed_selected_grey_rectangle = pygame.transform.scale(selected_grey_rectangle,
#                                    (selected_grey_rectangle.get_width() * 3,
#                                     selected_grey_rectangle.get_height() * 0.5))


#kdslfjafkl;




zoomed_in_black_square_img = pygame.image.load('black_square.png').convert()

zoomed_in_black_square_img = pygame.transform.scale(zoomed_in_black_square_img,
                                   (zoomed_in_black_square_img.get_width() * 4,
                                    zoomed_in_black_square_img.get_height() * 4))


zoomed_in_player_img = pygame.image.load('player.png').convert()

zoomed_in_player_img = pygame.transform.scale(zoomed_in_player_img,
                                   (zoomed_in_player_img.get_width() * 4,
                                    zoomed_in_player_img.get_height() * 4))

zoomed_in_player_img.set_colorkey((255,255,255))

zoomed_in_mouse_indicator_img = pygame.image.load('mouse_indicator.png').convert()

zoomed_in_mouse_indicator_img = pygame.transform.scale(zoomed_in_mouse_indicator_img,
                                   (zoomed_in_mouse_indicator_img.get_width() * 4,
                                    zoomed_in_mouse_indicator_img.get_height() * 4))

zoomed_in_mouse_indicator_img.set_colorkey((0,0,0))

zoomed_in_metal_floor_img = pygame.image.load('metal_floor.png').convert()

zoomed_in_metal_floor_img = pygame.transform.scale(zoomed_in_metal_floor_img,
                                   (zoomed_in_metal_floor_img.get_width() * 4,
                                    zoomed_in_metal_floor_img.get_height() * 4))


zoomed_in_fire_place_img = pygame.image.load('fire_place.png').convert()

zoomed_in_fire_place_img = pygame.transform.scale(zoomed_in_fire_place_img,
                                   (zoomed_in_fire_place_img.get_width() * 4,
                                    zoomed_in_fire_place_img.get_height() * 4))

zoomed_in_fire_place_img.set_colorkey((0,0,0))

oven_img = pygame.image.load('oven.png').convert()

oven_img = pygame.transform.scale(oven_img,
                                   (oven_img.get_width() * 8,
                                    oven_img.get_height() * 8))


inventory_rectangles = black_square_img

inventory_rectangles = pygame.transform.scale(inventory_rectangles,
                                   (inventory_rectangles.get_width() * 6,
                                    inventory_rectangles.get_height() * 1))


zoomed_in_grey_square_img = pygame.image.load('grey_square.png').convert()

zoomed_in_grey_square_img = pygame.transform.scale(zoomed_in_grey_square_img,
                                   (zoomed_in_grey_square_img.get_width() * 4,
                                    zoomed_in_grey_square_img.get_height() * 4))


zoomed_in_selected_grey_rectangle = grey_square_img

zoomed_in_selected_grey_rectangle = pygame.transform.scale(zoomed_in_selected_grey_rectangle,
                                   (zoomed_in_selected_grey_rectangle.get_width() * 12,
                                    zoomed_in_selected_grey_rectangle.get_height() * 2))


zoomed_in_metal_wall_img = pygame.image.load('metal_wall.png').convert()

zoomed_in_metal_wall_img = pygame.transform.scale(metal_wall_img,
                                   (metal_wall_img.get_width() * 2,
                                    metal_wall_img.get_height() * 2))











side_black_square_img = pygame.image.load('black_square.png').convert()

side_black_square_img = pygame.transform.scale(side_black_square_img,
                                   (side_black_square_img.get_width() * 400,
                                    side_black_square_img.get_height() * 400))







gridwidth = 32
gridhieght = 32

x = 8
y = 8

window_coords = [0,0]

joysticks = []

controller_connected = False

running = True

clock = pygame.time.Clock()

font = pygame.font.Font(None, size=30)

zoom = 1

square_size = 32

speed = 0.1

needs_to_center = 1

move_up = False
move_down = False
move_left = False
move_right = False


menu = 0

inventory_shown = 0

inventory = [[["FOOD",0],["bread",1],["drink",2],["biscuts",6],["cookies",0],["burgers",4],["meat",1],["cheese",3]], [["WEAPONS",0],["sword",1],["revolver",1,[3,2,3]]]]

inventory_armour = []

distance_to_move = 10

cook_able_foods = [["biscut sandwhich",1,3],["burger",1,6],["cheese burger",1,6,7]]

old_width = 0
old_height = 0


wating_for_level_editing = True

# [shape type start_x start_y end_x end_y]

level_editing_stuff = [[0,0,0,0,0,0]]

which_instruction = 0

new_instructions = [[]]

new_instructions = [[0] * 6 for i in range(50)]


pygame.joystick.init()

width, height = screen.get_size()

old_width = width
old_height = height

render_width = 0
render_height = 0

map = [[0] * 100 for i in range(100)]


# fill, type x, y, width, height
# colomn, type x, y, height
# row, type x, y, width
# square, type x, y, width, height




#  0       1     2   3      4       5
# shape   type   x   y   height   width

# map_instructions = [["square",2 ,0,0, 10,5],["row",1,10,10,10],["colomn",1,20,20,10],["fill",1,10,0,10,5]]


map_instructions = [["fill",0,0,0,100,100],["fill",0,8,8,12,7],["square",1,0,0,100,100],["fill",2,14,16,1,1]]




def gen_area(map_instructions):
    
    for t in range(len(map_instructions)):
        if map_instructions[t][0] == "fill":
            for c in range(map_instructions[t][5]):
                for r in range(map_instructions[t][4]):
                    map[c+map_instructions[t][3]][r+map_instructions[t][2]] = int(map_instructions[t][1])
        
        if map_instructions[t][0] == "square":
            for c in range(map_instructions[t][5]):
                for r in range(map_instructions[t][4]):
                
                    if c == 0:
                        map[c+map_instructions[t][3]][r+map_instructions[t][2]] = int(map_instructions[t][1])
                
                    if c == (map_instructions[t][5]) - 1:
                        map[c+map_instructions[t][3]][r+map_instructions[t][2]] = int(map_instructions[t][1])

                    if r == 0:
                        map[c+map_instructions[t][3]][r+map_instructions[t][2]] = int(map_instructions[t][1])
                    
                    if r == (map_instructions[t][4] - 1):
                        map[c+map_instructions[t][3]][r+map_instructions[t][2]] = int(map_instructions[t][1])

            
gen_area(map_instructions)



def draw_inventory(x,y,items_list,inventory):

    color = [255,255,255]
    c = 0
    d = c

    for c in range((len(items_list))):
        
        for r in range((len(items_list[c]))):

            screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))
            if x < mouse_pos[0] < (x + (32 * 6)):
                if ((y + (30 * d)) + 16) > mouse_pos[1] > ((y + (30 * d)) - 16):
                    screen.blit(selected_grey_rectangle,(x,(y + (30 * d)) - 10))



            if inventory[c][r][0] == "FOOD":
                screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))

                text = font.render(inventory[c][r][0], True, (color[0],color[1],color[2]))

                screen.blit(text, (x + 40,y + (30 * d)))

                d += 1
                # r += 1


            if inventory[c][r][0] == "WEAPONS":
                screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))

                text = font.render(inventory[c][r][0], True, (color[0],color[1],color[2]))

                screen.blit(text, (x + 40,y + (30 * d)))

                d += 1
                # r += 1

            if inventory[c][r][1] >= 1:    
                # screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))

                text = font.render(inventory[c][r][0], True, (color[0],color[1],color[2]))

                screen.blit(text, (x + 40,y + (30 * d)))

                text = font.render(str(inventory[c][r][1]), True, (color[0],color[1],color[2]))

                if inventory[c][r][1] < 10:
                    screen.blit(text, (x + 20,y + (30 * d)))
                if inventory[c][r][1] >= 10:
                    if inventory[c][r][1] < 100:
                        screen.blit(text, (x + 10,y + (30 * d)))
                if inventory[c][r][1] >= 100:
                    screen.blit(text, (x,y + (30 * d)))
            else:
                d -= 1
                # r -= 1

            
            d += 1
            # r += 1
            

def draw_menu_oven(x,y,list_of_foods,inventory_items):
    screen.blit(oven_img,(x - 350,200))
    color = [0,255,0]

    c = 0
    d = c

    for c in range((len(list_of_foods))):
        
        for r in range((len(list_of_foods[c]))):

            if r == 0:

                screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))
                if x < mouse_pos[0] < (x + (32 * 6)):
                    if ((y + (30 * d)) + 16) > mouse_pos[1] > ((y + (30 * d)) - 16):
                        screen.blit(selected_grey_rectangle,(x,(y + (30 * d)) - 10))
                                    

                text = font.render(cook_able_foods[c][0], True, (color[0],color[1],color[2]))

                screen.blit(text, (x + 10,y + (30 * d)))

                d += 1
                # r += 1


            if inventory_items[0][r][1] >= 1:    


                screen.blit(inventory_rectangles,(x,(y + (30 * d)) - 10))

                


                text = font.render(inventory_items[0][cook_able_foods[c][r]][0], True, (color[0],color[1],color[2]))

                screen.blit(text, (x + 40,y + (30 * d)))

                text = font.render(str(inventory_items[0][r][1]), True, (color[0],color[1],color[2]))

                if inventory_items[0][r][1] < 10:
                    screen.blit(text, (x + 20,y + (30 * d)))
                if inventory_items[0][r][1] >= 10:
                    if inventory_items[c][r][1] < 100:
                        screen.blit(text, (x + 10,y + (30 * d)))
                if inventory_items[0][r][1] >= 100:
                    screen.blit(text, (x,y + (30 * d)))
            else:
                d -= 1
                # r -= 1

            
            d += 1
            # r += 1

def level_editor():
    print (level_editing_stuff,wating_for_level_editing,int((mouse_pos[0] + window_coords[0]) / 32),int((mouse_pos[1] + window_coords[1]) / 32),zoom,square_size)


def size_texutres(width,height,g_width,g_height):

    print("testing")
        
    black_square_img = pygame.image.load('black_square.png').convert()

    black_square_img = pygame.transform.scale(black_square_img,
                                    (black_square_img.get_width() * 2,
                                        black_square_img.get_height() * 2))


    player_img = pygame.image.load('player.png').convert()

    player_img = pygame.transform.scale(player_img,
                                    (player_img.get_width() * 2,
                                        player_img.get_height() * 2))

    player_img.set_colorkey((255,255,255))

    mouse_indicator_img = pygame.image.load('mouse_indicator.png').convert()

    mouse_indicator_img = pygame.transform.scale(mouse_indicator_img,
                                    (mouse_indicator_img.get_width() * 2,
                                        mouse_indicator_img.get_height() * 2))

    mouse_indicator_img.set_colorkey((0,0,0))

    metal_floor_img = pygame.image.load('metal_floor.png').convert()

    metal_floor_img = pygame.transform.scale(metal_floor_img,
                                    (metal_floor_img.get_width() * ((width / g_width) / 8),
                                        metal_floor_img.get_height() * 2))


    fire_place_img = pygame.image.load('fire_place.png').convert()

    fire_place_img = pygame.transform.scale(fire_place_img,
                                    (fire_place_img.get_width() * 2,
                                        fire_place_img.get_height() * 2))

    fire_place_img.set_colorkey((0,0,0))

    oven_img = pygame.image.load('oven.png').convert()

    oven_img = pygame.transform.scale(oven_img,
                                    (oven_img.get_width() * 8,
                                        oven_img.get_height() * 8))

    fire_place_img.set_colorkey((0,0,0))

    inventory_rectangles = black_square_img

    inventory_rectangles = pygame.transform.scale(inventory_rectangles,
                                    (inventory_rectangles.get_width() * 6,
                                        inventory_rectangles.get_height() * 1))


    grey_square_img = pygame.image.load('grey_square.png').convert()

    grey_square_img = pygame.transform.scale(grey_square_img,
                                    (grey_square_img.get_width() * 2,
                                        grey_square_img.get_height() * 2))


    selected_grey_rectangle = grey_square_img

    selected_grey_rectangle = pygame.transform.scale(selected_grey_rectangle,
                                    (selected_grey_rectangle.get_width() * 6,
                                        selected_grey_rectangle.get_height() * 1))

    metal_wall_img = pygame.image.load('metal_wall.png').convert()

    metal_wall_img = pygame.transform.scale(metal_wall_img,
                                    (metal_wall_img.get_width() * 2,
                                        metal_wall_img.get_height() * 2))







def textrue_size(width,height):
    if height >= ((width / 4) * 3):
        render_width = width
        render_height = ((width / 4) * 3)
        print("tall")
    else:
        render_height = height
        render_width = ((height / 3) * 4)
        print("wide")
    return render_width,render_height





def draw_field(window_x,window_y,render_width,render_height):
    
    c = 0
    r = 0

    grid = 0
    
    for c in range(100):

        for r in range(100):

            if zoom == 2:
                if int(map[c][r]) == 0:
                    area_img = zoomed_metal_floor_img

                    
                elif int(map[c][r]) == 1:
                    area_img = zoomed_black_square_img


                elif int(map[c][r]) == 2:
                    area_img = zoomed_fire_place_img
                
                elif int(map[c][r]) == 3:
                    area_img = zoomed_metal_wall_img



            elif zoom == 1:        
                if int(map[c][r]) == 0:
                    area_img = metal_floor_img

                    
                elif int(map[c][r]) == 1:
                    area_img = black_square_img


                elif int(map[c][r]) == 2:
                    area_img = fire_place_img
                
                elif int(map[c][r]) == 3:
                    area_img = metal_wall_img
                    

            if zoom == 3:
                if int(map[c][r]) == 0:

                    area_img = zoomed_in_metal_floor_img
                    
                elif int(map[c][r]) == 1:
                    area_img = zoomed_in_black_square_img


                elif int(map[c][r]) == 2:
                    area_img = zoomed_in_fire_place_img
                
                elif int(map[c][r]) == 3:
                    area_img = zoomed_in_metal_wall_img

                    
            screen.blit(area_img, ((square_size * r) - window_x,(square_size * c) - window_y))

    # screen.blit(side_black_square_img,(((width - render_width) / 2) - (16 * 400),0))


    






    

while running:
    # player_coords_init(player.x,player.y)

    

    mouse_pos = pygame.mouse.get_pos()

    
    old_width = width
    old_height = height

    render_width = 0
    render_height = 0

    width, height = screen.get_size()


    if width == old_width:
        pass
    else:
        if height == old_height:
            pass
        else:
            render_w,render_h = textrue_size(width,height)
            size_texutres(render_w,render_h,gridwidth,gridhieght)
            print("test")

    screen.fill((255,255,255))

    if zoom == 1: # normal zoom
        square_size = 32
        
        gridwidth = 24
        gridhieght = 18

        speed = 0.2

        distance_to_move == 5
    
    elif zoom == 3: # zoomed in
        square_size = 64
        
        gridwidth = 12
        gridhieght = 9

        speed = 0.2

        distance_to_move == 2

    elif zoom == 2: # zoomed out
            square_size = 16
            
            gridwidth = 48
            gridhieght = 36

            # speed = 1.5
            speed = 0.5

            distance_to_move == 10

    if needs_to_center == 1:
        window_coords[0] =  ((x * square_size) - (width / 2))
        window_coords[1] = ((y * square_size) - (height / 2))
        needs_to_center = 0


    if window_coords[0] < 0:
        window_coords[0] = 0
    
    if window_coords[1] < 0:
        window_coords[1] = 0   

    if ((window_coords[0] + width) / square_size) > 100:
        window_coords[0] = (square_size * 100) - width

    if ((window_coords[1] + height) / square_size) > 100:
        window_coords[1] = (square_size * 100) - height




    draw_field(window_coords[0],window_coords[1],render_width,render_height)






    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            running = False
        

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
            controller_connected = True

        if event.type == pygame.JOYDEVICEREMOVED:
            controller_connected == False

        


        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu == 0:
                if map[int((mouse_pos[1] + window_coords[1]) / square_size)][int((mouse_pos[0] + window_coords[0]) / square_size)] == 2:
                    menu = 1
                elif map[int((mouse_pos[1] + window_coords[1]) / square_size)][int((mouse_pos[0] + window_coords[0]) / square_size)] == 2:
                    menu = 3


            elif menu == 2:
                if wating_for_level_editing == True:
                    level_editing_stuff[0][3] = int((mouse_pos[1] + window_coords[1]) / square_size)
                    level_editing_stuff[0][2] = int((mouse_pos[0] + window_coords[0]) / square_size)
                    wating_for_level_editing = 0
                else:
                    level_editing_stuff[0][5] = ((int((mouse_pos[1] + window_coords[1]) / square_size)) - level_editing_stuff[0][3]) + 1
                    level_editing_stuff[0][4] = ((int((mouse_pos[0] + window_coords[0]) / square_size)) - level_editing_stuff[0][2]) + 1
                    gen_area(level_editing_stuff)
                    level_editing_stuff = [[0,0 ,0,0, 0,0]]
                    new_instructions[which_instruction] = level_editing_stuff
                    which_instruction += 1
                    wating_for_level_editing = 1
                    


                    


        if not menu == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True
                
                # if event.key == pygame.K_f:

                if event.key == pygame.K_e:
                    if inventory_shown == 1:
                        inventory_shown = 0
                    else:
                        inventory_shown = 1

                if event.key == pygame.K_f:
                    inventory[0][2][1] += 1
                if event.key == pygame.K_g:
                    if inventory[0][2][1] > 0:
                        inventory[0][2][1] -= 1
                
                if event.key == pygame.K_z:
                    wating_for_level_editing = 1

                if event.key == pygame.K_b:
                    level_editing_stuff = [[0,0,0,0,0,0]]
                    wating_for_level_editing = 1

                

                if event.key == pygame.K_0:
                    level_editing_stuff[0][1] = 0
                if event.key == pygame.K_1:
                    level_editing_stuff[0][1] = 1
                if event.key == pygame.K_2:
                    level_editing_stuff[0][1] = 2
                if event.key == pygame.K_3:
                    level_editing_stuff[0][1] = 3


                if event.key == pygame.K_x:
                    level_editing_stuff[0][0] = "fill"
                if event.key == pygame.K_c:
                    level_editing_stuff[0][0] = "square"

                if event.key == pygame.K_p:
                    print(new_instructions)

                if event.key == pygame.K_g:
                    if zoom == 1:
                        zoom = 2
                    elif zoom == 2:
                        zoom = 3
                    elif zoom == 3:
                        zoom = 1
                    needs_to_center = 1


                if event.key == pygame.K_h:
                    menu = 0
                if event.key == pygame.K_j:
                    window_coords[0] =  ((x * square_size) - (width / 2))
                    window_coords[1] = ((y * square_size) - (height / 2))
                if event.key == pygame.K_k:
                    menu = 2
                
                

                        
                    
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                # if event.key == pygame.K_f:

        else:
            move_up = False
            move_down = False
            move_left = False
            move_right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = 0
            # if event.key == pygame.K_e:
                # menu = 0


            
    # if not zoom == 2:
    if map[int(y - 0.75)][int(x)] == 0:
        if move_up == True:
            y -= speed

    if map[int(y + 0.75)][int(x)] == 0:
        if move_down == True:
            y += speed

    if map[int(y)][int(x - 0.75)] == 0:
        if move_left == True:
            x -= speed

    if map[int(y)][int(x + 0.75)] == 0:
        if move_right == True:
            x += speed
    # else:
            # if move_up == True:
            #     y -= speed

            # if move_down == True:
            #     y += speed

            # if move_left == True:
            #     x -= speed

            # if move_right == True:
            #     x += speed

    
    if (x * square_size) > (window_coords[0] + (width * 0.8)):
        if ((window_coords[0] + width) / square_size) < 100:
            window_coords[0] += 10

    if (x * square_size) < (window_coords[0] + (width * 0.2)):
        if window_coords[0] > 0:
            window_coords[0] -= 10

    
    if (y * square_size) > (window_coords[1] + (height * 0.8)):
        if ((window_coords[1] + height) / square_size) < 100:
            window_coords[1] += 10

    if (y * square_size) < (window_coords[1] + (height * 0.2)):
        if window_coords[1] > 0:
            window_coords[1] -= 10

    




    if controller_connected == True:
        print (joy.get_axis(0)) 
        print (joy.get_axis(1))

        x += joy.get_axis(0) * speed
        y += joy.get_axis(1) * speed

                

    

    if zoom == 1: mouse_display = mouse_indicator_img
    elif zoom == 2: mouse_display = zoomed_mouse_indicator_img
    elif zoom == 3: mouse_display = zoomed_in_mouse_indicator_img

    screen.blit(mouse_display, ((square_size * level_editing_stuff[0][2]) - window_coords[0],(square_size * level_editing_stuff[0][3]) - window_coords[1]))
    
    if controller_connected == True:print (str(joy.get_name())," ",str(joy.get_numaxes()))
    # print(pygame.joystick.Joystick())

    


    if zoom == 1: player_display = player_img
    elif zoom == 2: player_display = zoomed_player_img
    elif zoom == 3: player_display = zoomed_in_player_img

    screen.blit(player_display,((((x * square_size) - (square_size / 2)) - window_coords[0]),(((y * square_size) - (square_size / 2)) - window_coords[1])))
   

    if menu == 1: 
        draw_menu_oven(width - 200,200,cook_able_foods,inventory)
        draw_inventory(30,30,inventory,inventory)
    elif menu == 2:level_editor()
    elif menu == 3:draw_menu_oven(width - 200,200,cook_able_foods,inventory)

    if inventory_shown == 1:draw_inventory(30,30,inventory,inventory)
    
    screen.blit(mouse_indicator_img,(mouse_pos[0] - 16,mouse_pos[1] - 16))
    


    
    # print (int((mouse_pos[0] + window_coords[0]) / square_size))    
    # print (int((mouse_pos[1] + window_coords[1]) / square_size))    


    # print (int(x),int(y))

    pygame.display.flip()

    clock.tick(60)
    # print (int(clock.get_fps()))
    # print ((clock.get_fps()))


pygame.quit()