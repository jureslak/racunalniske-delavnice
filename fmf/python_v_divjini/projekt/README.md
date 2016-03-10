Tic Tac Toe
===========

Installation
------------

Download the source code, preferably using
```bash
git clone https://github.com/jureslak/racunalniske-delavnice
```

Now run
```bash
python setup.py install
```
and the module should be installed.

Usage
-----

The module provides a `Game` class implementing the game. Tu use it, simpy open your Python
interpreter and run
```Python
>>> from tictactoe import game
>>> g = game.Game(2, 3, 3)  # 3 by 3 board for 2 players
>>> g.mainloop()
```
and have fun.

Detailed documentation is available here.

Jure Slak
<!---
vim: set spell spelllang=en:
-->
