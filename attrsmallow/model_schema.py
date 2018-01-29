#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import collections

import attr
import marshmallow


class BaseModel(object):
    """
    Base data model.

    Example::

        >>> import attr

        >>> @attr.s
        ... class User(BaseModel):
        ...     id = attr.ib()
        ...     name = attr.ib()
        ...
        ... @attr.s
        ... class Member(User):
        ...     level = attr.ib()
    """
    Schema = None

    def keys(self):
        """
        Return list of attributes name, in definition order.
        """
        return [a.name for a in self.__attrs_attrs__]

    def values(self):
        """
        Return values as list, in definition order.
        """
        return [getattr(self, a.name) for a in self.__attrs_attrs__]

    def items(self):
        """
        Return attr, value pairs. Similar to ``dict.items()``.
        """
        return list(zip(self.keys(), self.values()))

    def to_dict(self):
        """
        Convert to dict, attributes definition order is NOT preserved.
        """
        return attr.asdict(self)

    def to_OrderedDict(self):
        """
        Convert to OrderedDict, attributes definition order is preserved.
        """
        return collections.OrderedDict(self.items())

    def to_json(self, **kwargs):
        """
        Convert to json.

        :param kwargs: arguments in json.dumps(s, **kwargs)
        :return: json string.
        """
        return json.dumps(self.to_dict(), **kwargs)

    @classmethod
    def load(cls, data):
        """
        Load object from dict like data.
        """
        if cls.Schema is None: # pragma: no cover
            msg = ("Schema of this Model are not specified! For example: "
                   "class User(BaseModel): ...; class UserSchema(Schema): ...; "
                   "User.Schema = UserSchema")
            raise NotImplementedError(msg)

        res = cls.Schema().load(data)
        if len(res.errors) == 0:
            return res.data
        else:
            raise Exception("Errors: {}".format(res.errors))


class BaseSchema(marshmallow.Schema):
    """
    Base data schema.

    Example::

        >>> from marshmallow import fields

        >>> class UserSchema(BaseSchema):
        ...     id = fields.Integer()
        ...     name = fields.String()
        ...
        ...     Model = User
        ...
        ... User.Schema = UserSchema
    """
    Model = None

    @marshmallow.post_load
    def _make(self, data):
        try:
            return self.Model(**data)
        except TypeError: # pragma: no cover
            if self.Model is None:
                msg = ("Model of this Schema are not specified! For example: "
                       "class User(BaseModel): ...; class UserSchema(Schema): ...; "
                       "UserSchema.Model = User")
                raise NotImplementedError(msg)
            else:
                raise
        except: # pragma: no cover
            raise
