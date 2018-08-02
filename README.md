App-example how to code and test with aiohttp/peewee-async.

The main idea is show how to manage event loop and peewee connections in tests.

I don't recomend use that stack because of many reasons:
- async python libs don't ready for real big project, just for fun or small services.
- python has awful version compability, for this example you likely remain need to change source of aiopg and psycopg.

Feel free to create issue and compleme code.
