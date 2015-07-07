# Copyright (c) Moshe Zadka
# See LICENSE for details.

import attr

@attr.s
class Description(object):
    name = attr.ib(validator=attr.validators.instance_of(str))
    description = attr.ib(validator=attr.validators.instance_of(str))
    year = attr.ib(validator=attr.validators.instance_of(int))
    author = attr.ib(validator=attr.validators.instance_of(str))
    authorEmail = attr.ib(validator=attr.validators.instance_of(str))
    githubID = attr.ib(validator=attr.validators.instance_of(str))
