from aiohttp.test_utils import setup_test_loop, teardown_test_loop, unittest_run_loop
import peewee_async

from models.post import Post
from managers.post import PostManager

import unittest


class PostManagerTestCase(unittest.TestCase):
    database = peewee_async.PostgresqlDatabase('test')
    manager = PostManager(database)
    model = Post

    loop = None

    @classmethod
    def setUpClass(cls):
        Post.create_table()

    @classmethod
    def tearDownClass(cls):
        Post.drop_table()

    def setUp(self):
        self.loop = setup_test_loop()

    def tearDown(self):
        Post.delete().execute()

        self.loop.run_until_complete(self.manager.manager.close())
        teardown_test_loop(self.loop)

    @unittest_run_loop
    async def test_get_by_id(self):
        data = dict(title='title')
        instance = await self.manager.create(**data)

        retrieved = await self.manager.get_by_id(instance.id)

        self.assertEqual(instance, retrieved)

    @unittest_run_loop
    async def test_create(self):
        data = dict(title='title', text='text')

        instance = await self.manager.create(**data)

        self.assertEqual(data, dict(title=instance.title, text=instance.text))
