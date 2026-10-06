"""
===================
Dungeon Escape v1.1
===================
 
A small pygame game built around a simple state machine:
 
Game synopsis: Once you are a powerful warlord. Now imprisoned in a dungeon by an evil witch.
               But a rare opportunity has emarged. Once every housand years, a very brief moment 
               in time appears when magical gold coins falls from sky. Collect enough coins and a magical 
               door will appear which may lead to your freedom.
 
    state_title   --    start screen, showing clickable text "buttons"
    state_playing --    the actual game: a monster follows the mouse motion, coins
                        fall from the top and needs to be collected, and a hidden
                        door appears once 10 coins are collected. 
    state_won     --    shown once the player reaches the door with >=10 points
                        before the time runs out
    state_lost    --    shown once the player fails to escape within the time window.
 
The whole file is one class, GameApp, whose 'run()' method is a classic
game loop: read input -> update game state -> draw the current frame,
repeated 60 times a second. Which state the game is in decides which
update/draw method actually runs each frame (see 'update()' and 'draw()').
 
 
 
***N.B. The game start with 1920*1080 window size. If you have smaller monitor 
   Please, adjust the window_width and window_height just below the imports.
 
"""
 
import pygame
from typing import Callable
import random
 
# A bunch of global varibals
window_width = 1920  # adjust if you have smaller screen
window_height = 1080 # adjust if you have smaller screen
 
fill_color = ("grey81")
color_x = ("crimson")
hover_color_x = ("slateblue1")
hover_dim_x = ("slategray2")
 
state_title = "title"
state_playing = "playing"
state_won = "won"
state_lost = "lost"
 
class PsudoButton:
    """A text that can be clicked to initiate an action.
     -- no rectangle/box graphic is drawn, only the label itself,
    and it changes color plus grows an underline when the mouse hovers it.
 
    Instances of this class don't know anything about the game that owns
    them; they only know their own label, position, font, and a callback
    function to run when clicked. That's what lets GameApp reuse the same
    class for "Start Game", "Quit".
    """
 
    def __init__(self, label: str, center: tuple[int, int], font: pygame.font.Font, left_click: Callable[[], None]):
        """
        label      -- the text to display, e.g. "Start Game"
        center     -- (x, y) pixel coordinate the text should be centered on
        font       -- a pygame Font object used to render the label
        left_click -- a zero-argument function to call when this button
                      is clicked (e.g. self.start_game from GameApp)
        """
 
        self.label = label
        self.center = center
        self.font = font
        self.left_click = left_click
        surface = font.render(label, True, color_x) # pygame.Surface (Renders the text and returns a surface)
        rect = surface.get_rect(center=center)      
        self.rect = rect  # stores rectangle -- this is what click/hover checks test against
 
    def draw(self, surface: pygame.Surface, cursor_position: tuple[int, int]):
        """Renders this button onto `surface` for the current frame. """
 
        hovering_true = self.rect.collidepoint(cursor_position)  # checks (collidepoint returns a Boolean) if the cursor currently inside this button (text acting as a button)
        set_color = hover_color_x if hovering_true else color_x
        surf_2 = self.font.render(self.label, True, set_color) 
        rect_2 = surf_2.get_rect(center=self.center)
        surface.blit(surf_2, rect_2)
 
        if hovering_true:
            # Draw a short underline directly beneath the text to make the
            # "this is clickable" affordance clearer than a color change alone.
 
            underline_text = rect_2.bottom + 2
            pygame.draw.line(surface, hover_color_x, (rect_2.left, underline_text), (rect_2.right, underline_text), 2)
            self.rect = rect_2
 
    def is_clicked(self, cursor_position: tuple[int, int]) -> bool:
        '''This is the method that determines whether the button has been clicked'''
 
        if self.rect.collidepoint(cursor_position):
            self.left_click()  # run whatever action this button was built with
            return True
        return False
 
class GameApp:
    """
    Owns the entire game: window, assets, game state, and the main loop.
 
    The general shape to keep in mind while reading this class: 'update()'
    and 'draw()' never contain game logic themselves -- they only look at
    'self.state' and hand off to the matching 'update_x' / 'draw_x' method.
    Adding a new screen later means adding one more state constant and one
    more pair of methods, without touching the dispatch logic itself.
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Welcome to your worst nightmare")
 
        #************ Tunable gameplay conditions **************************
        self.points = 0
        self.coin_speed = 2      # how fast the coin disappears
        self.monster_speed = 3   # how fast the sprit moves
        self.spawn_chance = 0.01 # probability of raining coins from nowhere
        self.time_limit = 25.0   # time to escape your grave 
 
        self.display = pygame.display.set_mode((window_width, window_height))
 
        #******** Fonts, one per distinct text size/weight used in the UI *****
        self.title_font = pygame.font.SysFont("Arial", 58, bold=True)
        self.button_font = pygame.font.SysFont("Arial", 38)
        self.hud_font = pygame.font.SysFont("Arial", 20)
        self.score_font = pygame.font.SysFont("Arial", 20)
        self.message_font = pygame.font.SysFont("Arial", 40, bold=True)
 
        # Sprite images, loaded once here and reused every frame.
        # convert_alpha() converts each image to the display's own pixel
        # format (and keeps transparency), which makes blit() noticeably
        # faster than blitting a freshly-loaded, unconverted surface.
        self.monster = pygame.image.load("src/monster.png").convert_alpha()
        self.coin = pygame.image.load("src/coin.png").convert_alpha()
        self.door = pygame.image.load("src/door.png").convert_alpha()
 
        # state machine tracking
        self.state: str = state_title
        self.running: bool = True    # run() keeps looping while this is True
        self.buttons: list[PsudoButton] = []
        self.coins = []  # each entry is [x, y] for one falling coin
 
        # Monster position and where it's currently sliding towards.
        # target_x/y get updated on mouse movement; monster_x/y chase them
        # a few pixels per frame in update_playing()
        self.monster_x = 0
        self.monster_y = 0
        self.target_x  = 0
        self.target_y  = 0
 
        # Timer / end of run "game over" tracking
        self.remaining_time = self.time_limit
        self.surplus_time = 0
        self.escape_time = 0
        self.final_score = 0
 
        self.build_title_buttons()
 
    def build_title_buttons(self):
        """
        (Re)creates the title screen's two clickable text buttons.
        Called once from __init__, and again from go_to_title() every time
        the player returns to the title screen, since start_game() clears
        self.buttons out when entering state_playing.
        """
        c_window = window_width // 2
        self.buttons = [
            PsudoButton("Start Game", (c_window, 340), self.button_font, self.start_game),
            PsudoButton("Quit", (c_window, 400), self.button_font, self.quit_game),
        ]
 
    def start_game(self):
        """
        Button callback for "Start Game". Resets every piece of
        per-run state to a fresh value and switches into state_playing.
 
        This is the single place a new run gets set up, so it's also
        where the timer's reference point (self.start_ticks) gets taken --
        see get_remaining_time() for how that reference point gets used.
        """
        self.state = state_playing
        self.buttons = []
 
        self.points = 0
        self.coins = []
        self.remaining_time = self.time_limit
        self.start_ticks = pygame.time.get_ticks() # reference point (time) for current run
 
        # Center the monster in the window, with no motion queued up yet
        # target starts equal to the monster's own position, so it won't
        # drift anywhere until the first MOUSEMOTION event arrives.
        self.monster_x = window_width // 2 - self.monster.get_width() / 2
        self.monster_y = window_height // 2 - self.monster.get_height() / 2
        self.target_x = self.monster_x
        self.target_y = self.monster_y
 
        # Door is placed somewhere random each run, with a 100px margin from
        # every edge so it can never spawn partially off-screen.
        self.door_x = random.randint(100, (window_width - self.door.get_width()))
        self.door_y = random.randint(100, (window_height - self.door.get_height()))
 
    def quit_game(self):
        """
        Button callback for "Quit". Doesn't call pygame.quit() directly 
        that only happens once, after run()'s loop exits cleanly.
        """
        self.running = False
 
    def go_to_title(self):
        """
        Sends the player back to the title screen from any other state
        (called when Esc is pressed during playing/won/lost).
        """
        self.state = state_title
        self.build_title_buttons()
 
    #************  MAIN LOOP *******************************
 
    def run(self):
        """
        The actual game loop: handle input, advance game state, draw the
        frame, then wait out whatever's left of this frame's time budget so
        the whole loop runs at a steady 60 frames per second. Exits once
        self.running becomes False (Quit button, window close, etc.).
        """
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)
        pygame.quit()
 
    def handle_events(self):
        """
        Drains pygame's event queue once per frame and reacts to each
        event as it comes in: window close, left mouse clicks (checked
        against every current button), mouse movement (which only matters
        while playing, since that's what sets the monster's chase target),
        and key presses (delegated to handle_key).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for b in self.buttons:
                    if b.is_clicked(event.pos): # event.pos - contains the mouse's position when the click occurred
                        break  # stop checking once a button has actually been hit
                """
    This block handles a left mouse click and checks whether the 
    user clicked one of the buttons. This is where start_game()/quit_game() is called.
    When the buttons are created self.start_game/self.quit_game was passed
    Therefore, inside PsudoButton self.left_click = left_click means self.left_click = self.start_game/quit_game
    Hence, self.left_click() effectively calls self.start_game()/quit_game()
                
                """
 
            elif event.type == pygame.MOUSEMOTION:
                if self.state == state_playing:
                    # Offset by half the sprite's size so the monster centers
                    # on the cursor instead of the cursor sitting at its
                    # top-left corner.
                    self.target_x = event.pos[0] - self.monster.get_width() / 2
                    self.target_y = event.pos[1] - self.monster.get_height() / 2
            elif event.type == pygame.KEYDOWN:
                self.handle_key(event.key)
 
 
    def handle_key(self, key: int):
        """
        Currently only Esc does anything: it returns to the title screen
        from playing/won/lost, or quits outright if already on the title
        screen. 
        """
        if key == pygame.K_ESCAPE:
            if self.state in (state_playing, state_won, state_lost):
                self.go_to_title()
            else:
                self.quit_game()
 
    #******************** UPDATE *************************
 
    def update(self):
        """
        Per-frame state dispatch: only state_playing has anything that
        needs updating every frame (monster movement, coins, the timer).
        state_won and state_lost are static end screens -- once reached,
        nothing about them changes until the player leaves via Esc.
        """
        if self.state == state_playing:
            self.update_playing()
 
    def get_remaining_time(self):
        """
        Returns how many seconds are left in the current run.
        
        Based on real elapsed time (pygame.time.get_ticks(),
        milliseconds since pygame.init()) 
        """
        elapsed_mil_sec = pygame.time.get_ticks() - self.start_ticks
        return max(0.0, self.time_limit - elapsed_mil_sec / 1000.0)
        # max() is being used to make sure the remaining time never becomes negative.
 
    def finish_game(self, remaining: float, won: bool):
        """
        Freezes the current run and pre-computes everything the end
        screen needs to display, so draw_won()/draw_lost() only ever have
        to read these values, never calculate anything themselves.
 
        remaining -- seconds left on the clock at the moment the run ended
        won       -- True if the player reached the door in time, False if
                     the timer ran out first
        """
        self.surplus_time = round(remaining)
        self.escape_time = int(self.time_limit) - self.surplus_time
        self.final_score = self.surplus_time * 10
        self.state = state_won if won else state_lost
 
    def update_playing(self):
        """
        Runs every frame while state_playing is active: refreshes the
        timer, checks the two ways a run can end (reaching the door with
        enough points, or the clock hitting zero), and -- only if neither
        of those happened -- moves the monster toward its target and
        updates the falling coins.
 
        The door-reached check runs *before* the timeout check on purpose:
        if both would be true on the exact same frame (door reached right
        as the clock hits 0), the player still gets the win.
        """
        remaining = self.get_remaining_time()
        self.remaining_time = remaining  # for HUD countdown display
 
        monster_rect = pygame.Rect(self.monster_x, self.monster_y, self.monster.get_width(), self.monster.get_height())
        door_rect = pygame.Rect(self.door_x, self.door_y, self.door.get_width(), self.door.get_height())
 
        if self.points >= 10 and monster_rect.colliderect(door_rect):
            self.finish_game(remaining, won=True)
            return
        if remaining <= 0:
            self.finish_game(remaining, won=False)
            return
 
         # Simple "step toward the target" chase: move one increment per
        # frame in whichever direction closes the gap, on each axis
        # independently.
        if self.monster_x > self.target_x:
            self.monster_x -= self.monster_speed
        if self.monster_x < self.target_x:
            self.monster_x += self.monster_speed
        if self.monster_y > self.target_y:
            self.monster_y -= self.monster_speed
        if self.monster_y < self.target_y:
            self.monster_y += self.monster_speed
 
        self.update_coins()
 
 
    def update_coins(self):
        """
        Runs once per frame (from update_playing): rolls the dice on
        spawning a new coin at the top, then moves every existing coin
        down and decides its fate -- collected (removed, scores a point),
        fallen off the bottom (removed, no point), or still falling
        (kept for next frame). 
        """
        if random.random() < self.spawn_chance:
            coin_x = random.randint(0, window_width - self.coin.get_width())
            self.coins.append([coin_x, 0])
 
        monster_position = pygame.Rect(self.monster_x, self.monster_y, self.monster.get_width(), self.monster.get_height())
 
        survived_coins = []
        for c in self.coins:
            c[1] += self.coin_speed # fall as per coin speed specified
            coin_position = pygame.Rect(c[0], c[1], self.coin.get_width(), self.coin.get_height())
 
            if monster_position.colliderect(coin_position):
                self.points += 1
                continue  # collected -- not carried into survived_coins, so it disappears
 
            if c[1] < window_height:
                survived_coins.append(c)
            # else: fell past the bottom edge uncollected -- also dropped,
            # simply by not being appended above.
            
        self.coins = survived_coins
 
    #********************  DRAWING ***********************
 
    def draw(self):
        """
        Per-frame drawing dispatch, mirroring update()'s state check.
        Clears the window to the background color first (otherwise old
        frames would smear, since pygame doesn't auto-clear), draws
        whatever the current state calls for, then flips the result to
        the visible screen.
        """
        self.display.fill(fill_color)
        cursor_position = pygame.mouse.get_pos()
 
        if self.state == state_title:
            self.draw_title(cursor_position)
        elif self.state == state_playing:
            self.draw_playing()
        elif self.state == state_won:
            self.draw_won()
        elif self.state == state_lost:
            self.draw_lost()
 
        pygame.display.flip()
 
    def draw_title(self, cursor_position: tuple[int, int]):
        """
        Draws the game's title text plus both title-screen buttons.
        """
        surface_title = self.title_font.render("DUNGEON ESCAPE", True, color_x)
        rect_title = surface_title.get_rect(center=(window_width // 2, 220))
        self.display.blit(surface_title, rect_title)
 
        for b in self.buttons:
            b.draw(self.display, cursor_position)
 
    def draw_playing(self):
        """
        Draws everything visible during an active run: the monster,
        every coin currently falling, the points/time HUD in the top-left
        corner, and the door -- which only actually gets drawn once the
        player has 10+ points, even though its position was already
        chosen back in start_game().
        """
        self.display.blit(self.monster, (self.monster_x, self.monster_y))
        for c in self.coins:
            self.display.blit(self.coin, (c[0], c[1]))
 
        display_score = self.score_font.render(f"Coins collected: {self.points}", True, ("darkblue"))
        self.display.blit(display_score, (10, 10))
 
        display_timer = self.score_font.render(f"Time: {self.remaining_time:.1f}", True, ("darkblue"))
        self.display.blit(display_timer, (10, 45))
 
        if self.points >= 10: 
            self.display.blit(self.door, (self.door_x, self.door_y))
 
    def draw_middle_lines(self, lines, start_y, color, line_gap=55):
        """
        Shared helper for both end screens: renders a list of strings
        as separate lines, each horizontally centered in the window and
        stacked vertically 'line_gap' pixels apart starting at 'start_y'.
        An empty string in 'lines' just renders as blank vertical space,
        used below to separate the message from the "press Esc" hint.
        """
        for i, line in enumerate(lines):
            surf = self.message_font.render(line, True, color)
            rect = surf.get_rect(center=(window_width // 2, start_y + i * line_gap))
            self.display.blit(surf, rect)
 
    def draw_won(self):
        """
        End screen shown after successfully reaching the door with
        enough points before time ran out.
        """
        lines = [
            "Congratulations!",
            "You have successfully escaped the dungeon",
            f"Your final score: {self.final_score}",
            "",
            "Prss 'ESC' to return to the title screen"
        ]
        self.draw_middle_lines(lines, window_height // 2 - 150, color_x)
 
    def draw_lost(self):
        """
        End screen shown once the timer reaches zero before the player
        has reached the door with enough points.
        """
        lines = [
            "Game Over!",
            "You have lost your opportunity of escape",
            "Your fate is in the hands of random",
            "So, be patient and keep on trying",
            "",
            "Prss 'ESC' to return to the title screen"
        ]
        self.draw_middle_lines(lines, window_height // 2 - 150, ("black"))
 
if __name__ == "__main__":
    GameApp().run()