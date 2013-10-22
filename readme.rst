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


For english speaking people
---------------------------

This application allows to search for scientific journals defined in list
published by the Polish Ministry of Science, in form as three long pdf files.

