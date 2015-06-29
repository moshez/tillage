.. Copyright (c) Moshe Zadka
   See LICENSE for details.

tillage
-------

Introduction
============

TODO

Hacking
=======

  $ tox

Should DTRT -- if it passes, it means
unit tests are passing, and 100% coverage.

Release
========

* admin/release <next version number>
* gpg --use-agent -u zadka.moshe@gmail.com --detach-sign --armor dist/*.whl
* gpg --use-agent -u zadka.moshe@gmail.com --detach-sign --armor dist/*.zip
* admin/upload

Contributors
=============

Moshe Zadka <zadka.moshe@gmail.com>

License
=======

MIT License
