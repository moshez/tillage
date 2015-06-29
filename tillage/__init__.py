# Copyright (c) Moshe Zadka
# See LICENSE for details.

from tillage._version import get_versions as _get_versions

__version__ = _get_versions()['version']

_long_description = '''\
tillage: Prepare the GitHub soil for your Python code

.. _tillage: https://tillage.rtfd.org
'''

metadata = dict(
    name='tillage',
    description='Till GitHub for Python',
    long_description=_long_description,
    author='Moshe Zadka',
    author_email='zadka.moshe@gmail.com',
    license='MIT',
    copyright='2015',
)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
