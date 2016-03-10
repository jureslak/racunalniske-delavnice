.. tictactoe documentation master file, created by
   sphinx-quickstart on Fri Nov 20 00:29:41 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tic Tac Toe documentation!
==========================


Play a simple **interactive** hotseat game of Tic Tac Toe:

.. warning::

  This game is highly addictive and intelectually challenging.

.. code:: python

	>>> from tictactoe import game
	>>> g = game.Game(2, 3, 3)
	>>> g.mainloop()
	Enter player 1 name: Luke
	Enter player 1 symbol: x
	Enter player 2 name: Leia
	Enter player 2 symbol: o
	Currently on turn: Luke (x).
	+---+---+---+
	| 1 | 2 | 3 |
	+---+---+---+
	| 4 | 5 | 6 |
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	Please input a position: 2
	Currently on turn: Leia (o).
	+---+---+---+
	| 1 | x | 3 |
	+---+---+---+
	| 4 | 5 | 6 |
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	Please input a position: 5
	Currently on turn: Luke (x).
	+---+---+---+
	| 1 | x | 3 |
	+---+---+---+
	| 4 | o | 6 |
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	Please input a position: 3
	Currently on turn: Leia (o).
	+---+---+---+
	| 1 | x | x |
	+---+---+---+
	| 4 | o | 6 |
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	Please input a position: 1
	Currently on turn: Luke (x).
	+---+---+---+
	| o | x | x |
	+---+---+---+
	| 4 | o | 6 |
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	Please input a position: 9
	Currently on turn: Leia (o).
	+---+---+---+
	| o | x | x |
	+---+---+---+
	| 4 | o | 6 |
	+---+---+---+
	| 7 | 8 | x |
	+---+---+---+
	Please input a position: 6
	Currently on turn: Luke (x).
	+---+---+---+
	| o | x | x |
	+---+---+---+
	| 4 | o | o |
	+---+---+---+
	| 7 | 8 | x |
	+---+---+---+
	Please input a position: 7
	Currently on turn: Leia (o).
	+---+---+---+
	| o | x | x |
	+---+---+---+
	| 4 | o | o |
	+---+---+---+
	| x | 8 | x |
	+---+---+---+
	Please input a position: 4
	+---+---+---+
	| o | x | x |
	+---+---+---+
	| o | o | o |
	+---+---+---+
	| x | 8 | x |
	+---+---+---+
	Player Leia (o) won!
	Want to play another round [Y/n]: n
	Thank you for playing.

Modules list
============

.. toctree::
   :maxdepth: 4

   tictactoe

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

