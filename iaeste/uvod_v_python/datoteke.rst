Datoteke
========

Pomemben del programiranja je tudi delo z datotekami. Praktično vsak program, ki
ga imate na računalniku uporablja datoteke tako ali drugače, ali so to slike,
ki jih uporablja za izgled, zvok, video, tekst... V tem razdelku se bomo
pogledali, kako se Python obnaša pri delu z datotekami.

Odpiranje in zapiranje datotek
------------------------------

V Pythonu datoteko (kakršna koli že je, od teksta do zipa) odpremo s funkcijo
``open``. Datoteko lahko odpremo za branje, pisanje, oboje ali dodajanje.
Funkcija open sama po sebi ne naredi ničesar, preveri samo če tam datoteka
obstaja, če ne obstaja in smo izbrali pisanje, jo naredi in s sistemom izmenja
podatke za njeno branje. Če želimo brati datoteko, ki ne obstaja, potem Python
vrže izjemo. Odpiranje samo pripravi datoteko za operacije na njej in ne naredi
še nič resnega.

.. py:function:: open(pot_do_datoteke[, način])

  Najde datoteko in vrne objekt za delo z njo. Kaj lahko počne je odvisno od
  ``načina``, ki je ``r`` za branje, ``w`` za pisanje, ``+`` za branje in
  pisanje ter ``a`` za dodajanje. Kratice pomenijo *read*, *write* in *append*.
  Bolj natančno dokumentacijo najdete `tukaj
  <https://docs.python.org/3.4/library/functions.html#open>`_. Na windowsih
  moramo za netekstovne datoteke dodati še ``b``, ki pomeni *binary*. Če način
  ni podan, je enak ``r``.  Pod do datoteke je podana kot zaporedje map ločenih
  s ``/``, kjer ``..`` označuje *en mapo višje*. Npr. ``../slike/solata.jpg``
  pomeni: odpri datoteko ``solata.jpg``, ki se nahaja eno mapo višje v mapi
  slike.

Primer uporabe:

.. code-block:: python

  >>> f = open("besedilo.txt")  # recimo, da obstaja
  >>> f
  <_io.TextIOWrapper name='besedilo.txt' mode='r' encoding='UTF-8'>
  >>> g = open("asdf", "w")     # naredi novo datoteko, če ne obstaja
  >>> g
  <_io.TextIOWrapper name='asdf' mode='w' encoding='UTF-8'>
  >>> h = open("../slike/soalta.jpg")  # jejhata, zatipkali smo se
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  FileNotFoundError: [Errno 2] No such file or directory: '../slike/soalta.jpg'

Datoteko moramo po uporabi tudi zapreti, da sistemu povemo, da smo jo
zaključili uporabljati. Na Windowsih datoteke recimo ne moramo izbrisati, če jo
kakšen program uporablja (če je odprta).

Datoteko zapremo s klicem metode ``close``.

.. py:class:: file

  .. py:method:: close()

    Zapre datoteko in pove sistemu, da smo jo nehali uporabljati. To tudi napiše
    vse morebitne še nenapisane podatke do konca (flusha datoteko).

.. code-block:: python

  >>> f.close()
  >>> g.close()
  >>> h.close()
  >>> f.read()   # ko je datoteka zaprta z njo ne moremo več delati
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: I/O operation on closed file.

Ko delamo z datotekami pazimo, da je vrsti red vedno enak: odpremo, delamo,
zapremo.

Branje datotek
--------------

Privzemimo, da smo datoteko odprli za branje. Za branje imamo na voljo veliko
načinov.

.. py:class:: file

  .. py:method:: read([n])

    Prebere celo datoteko kot niz, skupaj z vsemi posebnimi znaki (recimo
    ``\n``). Če je ``n`` podan, prebere samo prvih ``n`` bajtov.

  .. py:method:: readline()

    Prebere naslednjo vrstico in jo vrne (vključno z ``\n``).

  .. py:method:: realines()

    Prebere vse vrstice in jih vrne kot seznam (vključno z ``\n``)

Lahko beremo tudi s ``for`` zanko. Pri branju si datoteka zapomni, do kam smo jo
prebrali in naslednjič, ko kličemo kakšno funkcijo za branje nadaljuje, kjer
smo na zadnje ostali. To pomeni, da datoteko ponavadi preberemo le enkrat (dva
zaporedna klica ``.read()`` bosta povzročila da drugi vrne prazen niz, saj je
bilo vse že prebrano). Enako se obnašajo tudi druge metode za branje, če ni
ničesar več za prebrati, potem vrnejo prazen niz. Vsebino datoteke si moramo, če
jo želimo uporabljati celo, shraniti v spremenljivko.

.. warning::

  Pri uporabi ``.read()`` mentode je potrebno paziti na velikost datoteke, ne
  poskušajte prebrati celega filma, saj verjetno nimate 4GB prostega spomina, pa
  tudi če, bo to verjetno delovalo zelo počasi.

Primer:

.. code-block:: python

  >>> f = open("besedilo.txt")
  >>> f.readline()
  'Romeo: O, Julija!\n'
  >>> for line in f:
  ...     print(line)
  Julija: O, Romeo, zakaj si Romeo?

  Romeo: Ženska, to ni mel smisla.

  THE END

Vsebina datoteke ``besedilo.txt`` je seveda::

  Romeo: O Julija!
  Julija: O, Romeo, zakaj si Romeo?
  Romeo: Ženska, to ni mel smisla.
  THE END

.. hint::

  Če se želimo znebiti nadležnih ``\n`` na koncu prebrane vrstice, uporabimo
  metodo ``strip`` na stringih.

  .. py:class:: str

    .. py:method:: strip([znaki])

      Poreže vse znake, ki se nahajajo v nizu ``znaki`` z začetka in konca
      niza. Če ``znaki`` niso podani, potem poreče ves whitespace (presledke,
      tabulatorje, ``\n`` in ostalo)

      Obstajata tudi metodi ``lstrip`` in ``rstrip``, ki delujeta samo na levi
      in desni strani niza.


Pisanje v datoteke
------------------

V datoteko, ki je odprta za pisanje, lahko pišemo. Duh. Če je ta datoteka že
obstajala, se njena prejšnja vsebina prepiše, kar je bilo prej noter je
izgubljeno. Če datoteka še ni obstajala, potem se ustvari nova datoteka.

Pišemo lahko na dva načina, z uporabo metode ``write`` ali ``writelines``.

.. py:class:: file

  .. py:method:: write(niz)

    Napiše niz v datoteko. Ne doda nobenih posebnih znakov.

  .. py:method:: writelines(seznam_nizov)

    Napiše seznam nizov v datoteko, niz po niz. Ne doda nobenih vmesnih znakov.

Primer:

.. code-block:: python

  f = open("stevila.txt", "w")
  f.write(str(0))
  f.write(str(1))
  f.writelines(["to", "so", "stevila"])
  f.write("\nAja, treba je dodajati nove vrstice!")
  f.close()

Vsebina datoteke je sedaj::

  01tosostevila
  Aja, treba je dodajati nove vrstice!


Stavek ``with``
---------------

Kot smo videli je postopek za delo z datotekami vedno enak, odpri, delaj,
zapri. Python ta postopek malo poenostavi, z uporabo ``with`` stavka.

Namesto::

  f = open("asdf")
  # beremo in pišemo
  f.close()

lahko uporabljamo::

  with f as open("asdf"):
      # beremo in pišemo

Datoteka uporabljena v ``with`` stavku se avtomatsko zapre, ne glede na to, kaj
se dogaja v telesu stavka. To je bolje kot lahko trdimo za prvi primer, če se
tam nekje na sredi zgodi izjema, bo program prekinjen, datoteka pa bo ostala
nesrečno odprta. Zaradi tega je ``with`` stavek najboljši način za delo z
datotekami.


Dodatek: ``stdin`` in ``stdout`` kot datoteki
---------------------------------------------

Tudi standardni vhod in izhod se obnašata kot datoteki, vhod je odprt za
branje, izhod pa za pisanje. Če želimo bolj natančno kontrolo nad branjem in
pisanjem lahko namesto ``input`` in ``print`` uporabimo "datoteki"
``sys.stdin`` in ``sys.stdout``. Teh dveh "datotek" ni treba odpirati ali
zapirati, podpirata pa običajne metode za branje in pisanje. Če želite to
uporabljati, ne pozabite na začetku programa dodati ``import sys``, da boste
imeli dostop do teh dveh objektov.

.. vim: spell spelllang=sl
