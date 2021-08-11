import sys, pygame, random, time

# Application setup and game information
pygame.init()
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Science SRP - AT2")
bg_img = pygame.image.load('/Users/han_le/Documents/Code/Python/science srp AT2/Reaction Lab/bg.png')
font = pygame.font.Font('Python/science srp AT2/Reaction Lab/8-Bit Madness.ttf', 24)
pygame.mouse.set_visible(False)

# Colors (RGB)
white = (255,255,255)
black = (0,0,0)
customcolor = (75, 0, 130)
custom = (245,245,220)

# Store game data
start_time = time.time()
running = True
eliminated = True
score = 0
time_paused = 0
react_time_start = 0
react_time = 0

# Setup initial rectangle target
global colour 
colour = customcolor
width = 116
height = 116
rand_x = (screen_width // 2) - width // 2        
rand_y = (screen_height // 2) - height // 2      


def drawText(str, position):
    """ (str, [x][y]) -> draw on screen at x,y
    
    Function that draws text to the screen via str and position parameters.
    """
    
    # Assign text contents and position
    text = font.render(str, True, white)
    text_surface = text
    text_rect = text.get_rect()
    text_rect.x = position[0]
    text_rect.y = position[1]
    
    # Draw to screen at specified position
    window.blit(text_surface, text_rect)
    
  
def drawScreen():
    """
    Function that redraws the display with updated game data pertaining to score, time,
    and the placement of objects on the screen.
    """
    
    global react_time_start, eliminated
    
    # Create a blank canvas every frame. 
    window.fill(black)
    window.blit(bg_img, (0,0))
    
    # Compute the total running time for the game
    total_time = round((running_time - start_time) - time_paused, 2)
    total_time = '{0:.2f}'.format(total_time)
    
    # Redraw score, time and reaction time
    drawText("Score: " +str(score), [365, 0])
    drawText("Time: " +str(total_time), [670, 0])

    # Redraw target on the screen
    pygame.draw.rect(window, colour, (rand_x, rand_y, width, height))
    
    # Track the amount of time the target is on the screen before being eliminated.
    if eliminated == True:                      # If target has been eliminated...
        pause()
        react_time_start = time.time()          # ...restart the timer
        eliminated = False                  


def pause():
    """
    Function that pauses the game and 'stops' time for the duration of the pause.
    
    Must use global keyword to refer to the global variable time_paused, else python will create 
    a local variable for time_paused which will result in UnboundLocalError.
    """
    
    global time_paused
    paused = True
    paused_time_start = time.time() 

    while paused:
        drawText("get ready!", [360, 500] )
        pygame.draw.rect(window, (0,0,0), (rand_x, rand_y, width, height))
        pygame.display.update()
        time.sleep(random.randrange(3,10))
        paused = False



# Establish the main game loop
while running:    
    pygame.time.delay(5)
    running_time = time.time()
           
    for event in pygame.event.get():  
        # see if the user quits
        if event.type == pygame.QUIT:
            running = False

        # track cursor position and mouse button
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                # Check if the mouse cursor is hovering over the target (I forgot why this works but it works....)
                if mouse_pos[0] >= rand_x - width//10 and mouse_pos[0] <= rand_x + width and mouse_pos[1] >= rand_y - height//10 and mouse_pos[1] <= rand_y + height:   
                
                    # If so, increment score and update reaction time
                    rand_x = (screen_width // 2) - width // 2
                    rand_y = (screen_height // 2) - height // 2
                    score += 1
                    eliminated = True
                    react_time = str(round((time.time() - react_time_start), 3))
                    
                    # Determine feedback based on reaction time (in ms)
                    print(react_time)

                    

            
                # If user misclicked, manually reset score and time. Reset target to center position 
                else:
                    eliminated = True
                    score = 0
                    time_paused = 0
                    start_time = time.time()
                    react_time = 0
                    rand_x = (screen_width // 2) - width // 2       # Center Position
                    rand_y = (screen_height // 2) - height // 2     # Center Position
        
    # Draw and refresh game every cycle
    drawScreen()
    pygame.display.update()
    
pygame.quit()