Co to robi
==========

Generalnie Ministerstwo Nauki i Szkolnictwa Wyższego publikuje listę czasopism
jako trzy wielkie pliki pdf. Ponieważ przeszukiwanie czegoś takiego jest
trudne i niewygodne, a ja musiałem jakić czas dość dokładnie to przeszukać
stworzyłem aplikację która:

* Parsuje te pliki (parsowanie dokonane jest za pomocą:
  https://github.com/ashima/pdf-table-extract (niestety trwa to długo, ale
  ta paczka bardzo dokłandnie wyciąga te tabele!).
* Zapisuje je do bazy danch
* Wystawia interfejs WWW, który pozwala na przeszukiwanie tych baz danych.

W najbliższym czasie postaram się to wystawić gdzieś na publicznym serwerze.

Dane w tej aplikacji zostały zaimportowane 19 września.

Plik `setup.py` nie jest testowany --- produkcyjnie działa po prostu klon z gita.

Uwagi
-----

#. Używacie aplikacji na własną odpowiedzialność, **problem importu danych
   z plików pdf jest skomplikowany**.
#. Wiem że kilkanaście czasopism jest źle zaimportowanych.
#. Zachęcam wszystkich (w tym osoby nie programujące w Pythonie) do przesylania
   udoskonaleń programu.
#. W jakimś rozsądnym czasie opublikuję wersję online tej aplikacji pod adresem:
   `lfitj.if.pw.edu.pl/listy <http://lfitj.if.pw.edu.pl/listy/>`_

For english speaking people
---------------------------

This application allows to search for scientific journals defined in list
published by the Polish Ministry of Science, in form as three long pdf files.

