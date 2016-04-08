# Generated by Creer at 11:41PM on April 07, 2016 UTC, git hash: 'e7ec4e35c89d7556b9e07d4331ac34052ac011bd'
# This is a simple class to represent the Nest object in the game. You can extend it by adding utility functions here in this file.

from games.spiders.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Nest(GameObject):
    """The class representing the Nest in the Spiders game.

    A location (node) connected to other Nests via Webs (edges) in the game that Spiders can converge on, regardless of owner.
    """

    def __init__(self):
        """Initializes a Nest with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._spiders = []
        self._webs = []
        self._x = 0
        self._y = 0



    @property
    def spiders(self):
        """All the Spiders currently located on this Nest.

        :rtype: list[Spider]
        """
        return self._spiders


    @property
    def webs(self):
        """Webs that connect to this Nest.

        :rtype: list[Web]
        """
        return self._webs


    @property
    def x(self):
        """The X coordinate of the Nest. Used for distance calculations.

        :rtype: int
        """
        return self._x


    @property
    def y(self):
        """The Y coordinate of the Nest. Used for distance calculations.

        :rtype: int
        """
        return self._y



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
