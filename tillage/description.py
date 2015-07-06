# Copyright (c) Moshe Zadka
# See LICENSE for details.

import attr

@attr.s
class Description(object):
    name = attr.ib(validator=attr.validators.instance_of(str))
