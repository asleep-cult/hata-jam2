import functools
import sqlite3
from sqlite3 import Connection, Cursor
from hata.backend.executor import ExecutorThread


class SQLiteConn:
    def __init__(self, executor: ExecutorThread, conn: Connection):
        self._executor = executor
        self._conn = conn

    async def backup(
        self,
        target,
        *,
        pages=0,
        progress=None,
        name='main',
        sleep=0.250
    ):
        future = self._executor.execute(
            functools.partial(
                self._conn.backup,
                target, pages=pages,
                progress=progress,
                name=name, sleep=sleep
            )
        )
        return await future

    async def close(self):
        future = self._executor.execute(
            self._conn.close
        )
        return await future

    async def commit(self):
        future = self._executor.execute(
            self._conn.commit
        )
        return await future

    async def create_aggregate(self, name, narg, aggregate_class):
        future = self._executor.execute(
            functools.partial(
                self._conn.create_aggregate,
                name, narg, aggregate_class
            )
        )
        return await future

    async def create_collation(self, name, callback):
        future = self._executor.execute(
            functools.partial(
                self._conn.create_collation,
                name, callback
            )
        )
        return await future

    async def create_function(self, name, narg, func, *, deterministic):
        future = self._executor.execute(
            functools.partial(
                self._conn.create_function,
                name, narg, func,
                deterministic=deterministic
            )
        )
        return await future

    async def cursor(self):
        cursor = await self._executor.execute(
            self._conn.cursor
        )
        return SQLiteCursor(self, cursor)

    async def enable_load_extension(self, onoff):
        future = self._executor.execute(
            functools.partial(
                self._conn.enable_load_extension,
                onoff
            )
        )
        return await future

    async def execute(self, sql, parameters=None):
        parameters = parameters or []
        cursor = await self._executor.execute(
            functools.partial(
                self._conn.execute,
                sql, parameters
            )
        )
        return SQLiteCursor(self, cursor)

    async def executemany(self, sql, parameters):
        cursor = await self._executor.execute(
            functools.partial(
                self._conn.executemany,
                sql, parameters
            )
        )
        return SQLiteCursor(self, cursor)

    async def executescript(self, sql):
        cursor = await self._executor.execute(
            functools.partial(
                self._conn.executescript,
                sql
            )
        )
        return SQLiteCursor(self, cursor)

    async def iterdump(self):
        future = self._executor.execute(
            self._conn.iterdump
        )
        return await future

    async def load_extension(self, extension_name):
        future = self._executor.execute(
            functools.partial(
                self._conn.load_extension,
                extension_name
            )
        )
        return await future

    async def rollback(self):
        future = self._executor.execute(
            self._conn.rollback
        )
        return await future

    async def set_authorizer(self, authorizer_cb):
        future = self._executor.execute(
            functools.partial(
                self._conn.set_authorizer,
                authorizer_cb
            )
        )
        return await future

    async def set_progress_handler(self, progress_handler, n):
        future = self._executor.execute(
            functools.partial(
                self._conn.set_progress_handler,
                progress_handler,
                n
            )
        )
        return await future

    async def set_trace_callback(self, trace_callback):
        future = self._executor.execute(
            functools.partial(
                self._conn.set_trace_callback,
                trace_callback
            )
        )
        return await future


class SQLiteCursor:
    def __init__(self, conn: SQLiteConn, cursor: Cursor):
        self._conn = conn
        self._cursor = cursor

    async def executemany(self, sql, parameters):
        future = self._conn._executor.execute(
            functools.partial(
                self._cursor.executemany,
                sql, parameters
            )
        )
        return await future

    async def executescript(self, sql):
        future = self._conn._executor.execute(
            functools.partial(
                self._cursor.executescript,
                sql
            )
        )
        return await future

    async def fetchone(self):
        future = self._conn._executor.execute(
            self._cursor.fetchone
        )
        return await future

    async def fetchmany(self, size=None):
        args = (size,) if size is not None else ()
        future = self._conn._executor.execute(
            functools.partial(
                self._cursor.fetchmany,
                *args
            )
        )
        return await future

    async def fetchall(self):
        future = self._conn._executor.execute(
            self._cursor.fetchall
        )
        return await future

    async def close(self):
        future = self._conn._executor.execute(
            self._cursor.close
        )
        return await future

    @property
    def rowcount(self):
        return self._cursor.rowcount

    @property
    def lastrowid(self):
        return self._cursor.lastrowid

    @property
    def arraysize(self):
        return self._cursor.arraysize

    @arraysize.setter
    def arraysize(self, value):
        self._cursor.arraysize = value

    @property
    def description(self):
        return self._cursor.description

    @property
    def connection(self):
        return self._cursor.connection


async def connect(*args, **kwargs): # noqa
    executor = ExecutorThread()
    conn = await executor.execute(
        functools.partial(sqlite3.connect, *args, **kwargs)
    )
    return SQLiteConn(executor, conn)
