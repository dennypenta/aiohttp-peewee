import peewee

import datetime


class Post(peewee.Model):
    title = peewee.CharField(max_length=40)
    text = peewee.CharField(max_length=280, null=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        # with our pattern we don't care what database is there
        # we gonna set it via model manager that will be manage all operation in database
        # and out model is just most simple entity
        database = None
