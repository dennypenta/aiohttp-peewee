import peewee_async

from models.post import Post


class PostManager(object):
    model = Post
    db = None
    _manager = None

    def __init__(self, db):
        self.db = db
        self.model._meta.database = db
        self._manager = peewee_async.Manager(db)

    @property
    def manager(self):
        return self._manager

    async def get_by_id(self, id):
        return await self.manager.get(self.model, id=id)

    async def create(self, **kwargs):
        return await self.manager.create(self.model, **kwargs)
