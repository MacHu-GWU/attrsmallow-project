#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__short_description__ = "Integration of attrs and marshmallow."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"


try:
    from .model_schema import BaseModel, BaseSchema
except: # pragma: no cover
    pass