"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in the Alien
Invaders game.  Instances of Wave represent a single wave.  Whenever you move to a
new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on screen.
These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts on screen.
    It animates the laser bolts, removing any aliens as necessary. It also marches the
    aliens back and forth across the screen until they are all destroyed or they reach
    the defense line (at which point the player loses). When the wave is complete, you
    should create a NEW instance of Wave (in Invaders) if you want to make a new wave of
    aliens.

    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 24 for an example.  This class will be similar to
    than one in how it interacts with the main class Invaders.

    #UPDATE ME LATER
    INSTANCE ATTRIBUTES:
        _ship:   the player ship to control [Ship]
        _aliens: the 2d list of aliens in the wave [rectangular 2d list of Alien or None]
        _bolts:  the laser bolts currently on screen [list of Bolt, possibly empty]
        _dline:  the defensive line being protected [GPath]
        _lives:  the number of lives left  [int >= 0]
        _time:   The amount of time since the last Alien "step" [number >= 0]

    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Invaders. It is okay if you do, but you MAY NOT ACCESS
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that
    you need to access in Invaders.  Only add the getters and setters that you need for
    Invaders. You can keep everything else hidden.

    You may change any of the attributes above as you see fit. For example, may want to
    keep track of the score.  You also might want some label objects to display the score
    and number of lives. If you make changes, please list the changes with the invariants.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getAlien(self):
        """
        Return the 2d list of aliens in the waveself.
        """
        return self._aliens
    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        """
        This method initializes the aliens dimensions.
        """
        self._aliens = self.create_Aliens()
        self._ship = Ship()
        self._dline = GPath(points=[0,DEFENSE_LINE,GAME_WIDTH,DEFENSE_LINE],
                            linewidth=1,linecolor='red')
        self._time = 0


    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self,input,dt):
        x = 0
        if input.is_key_down('left'):
            x = x - SHIP_MOVEMENT
        elif input.is_key_down('right'):
            x = x + SHIP_MOVEMENT
        self._ship._move(x)


        self.time(dt)
    # DRAW METHOD TO
    def draw(self,view):
        """
        DRAWs THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS.
        """
        for m in range(len(self._aliens)):
            for n in range(len(self._aliens[m])):
                self._aliens[m][n].draw(view)
        self._ship.draw(view)
        self._dline.draw(view)
    # HELPER METHODS FOR COLLISION DETECTION
    def create_Aliens(self):
        """
        Creates rows of aliens and puts it in a 2d list.
        """
        # The x position of the next alien
        # The y position of the next alien
        # The image of the next alien
        a =  (ALIEN_WIDTH/2) + ALIEN_H_SEP
        x =  (ALIEN_WIDTH/2) + ALIEN_H_SEP
        y = GAME_HEIGHT - (ALIEN_CEILING + (ALIEN_HEIGHT/2))
        pic = ['alien1.png','alien1.png','alien2.png','alien2.png','alien3.png','alien3.png']
        q = 0
        column = []
        for n in range(ALIEN_ROWS):
            row= []
            q = q+1
            for b in range(ALIENS_IN_ROW):
                row.append(Alien(x = x ,y = y,
                        source=pic[q]))
                x = x + ((ALIEN_WIDTH) + ALIEN_H_SEP)
            column.append(row)
            pic.append(pic[q])
            x = a
            y = y - ((ALIEN_HEIGHT/2) + ALIEN_V_SEP)
        return column

    def time(self,dt):
        "Updates the time attribute and moves the alien Wave according to speed."
        self._time = self._time + dt
        if self._time > ALIEN_SPEED:
            self.move()
            self._time = 0

    def move(self):
        x =  (ALIEN_WIDTH/2) + ALIEN_H_SEP
        for m in range(len(self._aliens)):
            for n in range(len(self._aliens[m])):
                self._aliens[m][n].x = self._aliens[m][n].x + ALIEN_H_WALK
                if self._aliens[m][n].x >= GAME_WIDTH - ALIEN_WIDTH :
                    self._aliens[m][n].x = x
                    self._aliens[m][n].y = self._aliens[m][n].y - ALIEN_V_WALK



                # self._aliens[m][n].y = self._aliens[m][n].x + ALIEN_V_WALK
