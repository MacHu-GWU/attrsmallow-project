.. image:: https://travis-ci.org/MacHu-GWU/attrsmallow-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/attrsmallow-project?branch=master

.. image:: https://codecov.io/gh/MacHu-GWU/attrsmallow-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/attrsmallow-project

.. image:: https://img.shields.io/pypi/v/attrsmallow.svg
    :target: https://pypi.python.org/pypi/attrsmallow

.. image:: https://img.shields.io/pypi/l/attrsmallow.svg
    :target: https://pypi.python.org/pypi/attrsmallow

.. image:: https://img.shields.io/pypi/pyversions/attrsmallow.svg
    :target: https://pypi.python.org/pypi/attrsmallow

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/attrsmallow-project


Welcome to ``attrsmallow`` Documentation
==============================================================================

`attrs <http://www.attrs.org/>`_ is a powerful library helps you to write concise and correct classes. And `marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_ is a powerful framework to write serializer/deserializer and data validator for complex object.

``attrsmallow`` is a glue layer to taking advantage from them.


Quick Links
------------------------------------------------------------------------------
- .. image:: https://img.shields.io/badge/Link-Document-red.svg
      :target: https://attrsmallow.readthedocs.io/index.html

- .. image:: https://img.shields.io/badge/Link-API_Reference_and_Source_Code-red.svg
      :target: https://attrsmallow.readthedocs.io/py-modindex.html

- .. image:: https://img.shields.io/badge/Link-Install-red.svg
      :target: `install`_

- .. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/attrsmallow-project

- .. image:: https://img.shields.io/badge/Link-Submit_Issue_and_Feature_Request-blue.svg
      :target: https://github.com/MacHu-GWU/attrsmallow-project/issues

- .. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.python.org/pypi/attrsmallow#downloads


Usage
------------------------------------------------------------------------------
A blog example:

.. code-block:: python

    import attr
    import marshmallow
    from attrsmallow import BaseModel, BaseSchema

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

    post_data = dict(id=1, title="Hello World!", user=dict(id=1, name="Alice"))
    post = Post.load(post_data)


.. _install:

Install
------------------------------------------------------------------------------

``attrsmallow`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install attrsmallow

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade attrsmallow
