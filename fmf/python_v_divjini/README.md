# Računalniske delavnice

A sample repository for a workshop on Python projects.

## Preparation guide

You must have `python3`, `pip` and `git` installed.  You can check this by
typing their names in the command line.

Clone this repository to your `U:` drive.
```
git clone https://github.com/jureslak/racunalniske-delavnice.git
```
You do not need to look at anything yet, *especially not the solutions*. Those
are there only in case you get lost along the way.

## A normal coding process

It looks somewhat like this:
```
      ________________________<<<________________________________
     /______________<<<______________________                    \
    /_______<<<____________________          \                    \
   /___<<<_______                  \          \                    \
  /               \                 \          \                    \
read ---> {write, test, doc} ---> review ---> test ---> commit ---> fix
                                           stylecheck   deploy
```

### Task 1
If we are all excellent developers that make 1 bug per month, how often is
something broken?

## Testing
Why do we need it? (Did you solve task 1?) More proof needed?

### History of bugs

* Millenium bug: year 2000 caused a lot of problems
* Intel: division bug
* Apple: SSL
```C
if ((err = SSLHashSHA1.update(&hashCtx, &serverRandom)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
    goto fail;
    goto fail;
if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)
    goto fail;
```
* Heartbleed: buffer overflow
* Shellshock: evaluating user input
* Nasa: spacecraft crashes to Mars, because a team used imperial units (of course).
* Nasa #2: a spacecraft gets shut down over Atlantic ocean -- wrong formula
* Gas pipeline explosion in Russia
* North American blackout: race condition -- hard bugs, Heisenbug :)
* US army: patriot missile
* Therac-25: radiation therapy device fails -- race condition.
* Donald Knuth: *Beware of bugs in the above code; I have only proved it
  correct, not tried it.*

A lot of code is library code. We test the functions and classes, if they do,
what they are supposed to.

Such tests are called **unit tests**, because they test a single unit.

### Task 2
Go to  `samples/` folder and write a `to_binary` function, that
converts an integer to a binary string.

Unit tests in python are written using the built in `unittest` package. Usually
every `something.py` file is accompanied by a `test_something.py` file that
tests its functionality.

Purpose of tests:
* ensure correctness
* define behaviour
* document usage cases
* force decent code design

Example from python's `unittest`:
```Python
from math import factorial
import unittest

class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(13.0), 6227020800)

    def test_invalid(self):
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, 1.6)
        self.assertRaises(TypeError, factorial, '23')
        self.assertRaises(TypeError, factorial, [12])
        self.assertRaises(OverflowError, factorial, 1348123481273489123493423)

if __name__ == '__main__':
    unittest.main()
```

Good tests should test for edge cases, be reproducible, deterministic, complete, fast, independent
amongst themselves and from the implementation they are testing.

### Task 3
Test your `to_binary` function.

## Mocks
A lot of code is not pure library code. Libraries deal with files, databases, user IO, servers...
How to test those?

We use **mocks**, objects that mock the other side.
Now, look at the file `project/tictactoe/ioutil.py` and the corresponding test file.

### Task 4
Write your own function `get_number` that begs the
user for a number, unit he inputs one.
Test the function as well as the output that user sees.
*Hint:* you may need `StringIO` from `io` module to simulate an
output stream.

Other kind of tests:
* integration tests
* end to end tests

How to test reported bugs?

Also mention concepts of TDD and fuzz testing.

Python project structure:
```
.
|- LICENSE
|- README.md
|- TODO.md
|- docs/
|- requirements.txt
|- project_name/
|   |-- __init__.py
|   |-- code.py
|- test/
|   |-- test_code.py
|- setup.py
```

Test runner: `nose`
```Bash
pip install nose
```
and use `nosetests` in your project root.

## Documentation

### Final task -- as motivation
Update the package so that Players keep scores after multiple rounds. Print
them after every round.

Use docstrings!

```Python
def function(x):
    """Just like this."""
	pass
```

Hmm, we would like some documentation. Docstrings look promising.

### Task 5
Write docstrings for `to_binary` function.
Include python examples in docstrings -- examples are the best documentation.

How to keep them up to date?

### Doctest module
Tests interactive python examples in docstrings -- it is pure magic.
Just add
```Python
if __name__ == '__main__':
	import doctest
	doctest.testmod()
```
to the end of file.

### Task 6
Write doctests for `to_binary`. Test for exceptions as well.

### Sphinx and documentation generation
If you do not have it, you should install `sphinx` with:
```bash
pip install sphinx
```

Go to `project/docs/` folder and run
```bash
sphinx-quickstart
```
Answer the questions, make sure you answer yes to `autodoc`.

Now edit `conf.py` to setup your path and theme.
Run
```bash
make html
```
when you want to generate html files.

Sphinx is very powerful: it uses reST syntax and supports
* Doctests
* Coverage
* Math
* Automatic docs generation
* HTML and PDF output

## Style checking
Consistency is important. Style checkers assure that, and the guard from errors.
Python code usually follows [PEP8](https://www.python.org/dev/peps/pep-0008/).

### Task 7
Run
```
pylint tictactoe/
```
and look at the results. Fix some of them.

### Final task
Update the package so that Players keep scores after multiple rounds. Print
them after every round. Write tests and documentation for your code.

If you need a bigger challenge, implement a joker. Each player
has one joker, that he can use to make a move anytime, without paying respect
to game order. Test and document all added features.

If you need an even greater challenge, make a game multiplayer,
by connecting more instances via sockets to a common 'server' where the game
is acually played. Test and document all added features.

## Conclusion
If there is some time left, we will look at the `setup.py` script and `requrements.txt` file. Maybe
also `virtualenv`.

FMF, 4. dec 2015

Jure Slak

<!---
vim: set spell spelllang=en:
-->
