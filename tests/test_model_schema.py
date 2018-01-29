#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from attrsmallow.model_schema import (
    attr, marshmallow, BaseModel, BaseSchema, json, collections,
)

fields = marshmallow.fields


@attr.s
class User(BaseModel):
    id = attr.ib()
    name = attr.ib()


class UserSchema(BaseSchema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)

    Model = User


User.Schema = UserSchema


@attr.s
class Member(User):
    access_level = attr.ib()


class MemberSchema(UserSchema):
    access_level = fields.Integer(required=True)

    Model = Member


Member.Schema = MemberSchema


@attr.s
class Post(BaseModel):
    id = attr.ib()
    title = attr.ib()
    user = attr.ib()


class PostSchema(BaseSchema):
    id = fields.Integer()
    title = fields.String()
    user = fields.Nested(UserSchema)

    Model = Post


Post.Schema = PostSchema


def test_load():
    user_data = dict(id=1, name="Alice")
    user = User.load(user_data)
    assert user.id == 1
    assert user.name == "Alice"

    with raises(Exception):
        User.load(dict(id="a1"))

    member_data = dict(id=1, name="Alice", access_level=3)
    member = Member.load(member_data)
    assert member.id == 1
    assert member.name == "Alice"
    assert member.access_level == 3

    assert member.keys() == ["id", "name", "access_level"]
    assert member.values() == [1, "Alice", 3]
    assert member.items() == [("id", 1), ("name", "Alice"), ("access_level", 3)]
    assert member.to_dict() == {"id": 1, "name": "Alice", "access_level": 3}
    assert member.to_OrderedDict() == collections.OrderedDict(
        [("id", 1), ("name", "Alice"), ("access_level", 3)]
    )
    assert member.to_dict() == json.loads(member.to_json())

    post_data = dict(id=1, title="Hello World!", user=dict(id=1, name="Alice"))
    post = Post.load(post_data)

    assert isinstance(post.user, User)
    assert post.to_dict() == {
        'id': 1, 'title': 'Hello World!',
        'user': {'id': 1, 'name': 'Alice'},
    }


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
