#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid
import orm, asyncio
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    #identity = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    # id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    id = StringField(primary_key=True, ddl='int(11)')
    user_identity = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)



# def test():
#     yield from orm.create_pool(loop='loop', user='root', password='355itu11', db='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()
# if __name__== '__main__':
#     for x in test():
# #         pass
# def test(loop):
#     yield from orm.create_pool(loop=loop,user='root',password='355itu11',db='awesome')
#     u=User(name='test3',email='test4@test.com',password='test',image='about:blank')
#     yield from u.save()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()