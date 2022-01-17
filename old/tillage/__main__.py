# Copyright (c) Moshe Zadka
# See LICENSE for details.

if __name__ != '__main__':
    raise ImportError('module cannot be imported')

import sys
import mainland

mainland.main(
    root='tillage',
    marker='TILLAGE_MAIN_OK',
    argv=sys.argv,
)
