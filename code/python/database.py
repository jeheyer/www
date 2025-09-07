from os import path
from pathlib import Path
from system_tools import read_file


async def db_config(db_name) -> dict:

    _db_config = {}

    pwd = path.dirname(__file__)

    cfg_dirs = []
    for cfg_dir in ["../..", "../../..", "../../../.."]:
        _ = path.join(pwd, cfg_dir, "./private/cfg/db_config.toml")
        cfg_dirs.append(_)
        #print("looking for file:", _)
        if p := Path(_):
            if p.exists() and p.is_file():
                if _db_config := read_file(_):
                    #print("Found it!")
                    break
    assert _db_config, FileNotFoundError(f"Database config file could not be opened.  Looked here: {cfg_dirs}")
    if not (db_info := _db_config.get(db_name)):
        raise Exception(f"Database config not found for '{db_name}'")

    return db_info

async def db_engine(db_name):

    from sqlalchemy.ext.asyncio import create_async_engine

    # Connect to DB
    db_info = await db_config(db_name)
    db_hostname = db_info.get('hostname', "127.0.0.1")
    db_username = db_info.get('username', "root")
    db_password = db_info.get('password', "")
    db_type = db_info.get('driver', "mysql").lower()
    db_driver = None
    if db_type == "mysql":
        db_driver = "mysql+asyncmy"
    try:
        _ = f"{db_driver}://{db_username}:{db_password}@{db_hostname}/{db_name}"
        engine = create_async_engine(_)
        return engine
    except Exception as e:
        raise e


async def db_engine_dispose(engine=None, session=None):

    # Disconnect from DB
    if engine:
        await engine.dispose()
    if session:
        await session.close()


async def db_insert(engine, table_name, **values):

    from sqlalchemy import Table, MetaData

    try:
        async with engine.begin() as _conn:
            table = await _conn.run_sync(lambda conn: Table(table_name, MetaData(), autoload_with=conn))
            statement = table.insert().values(values)
            result = await _conn.execute(statement)
            return result

    except Exception as e:
        raise e


async def db_update(engine, table_name, column_name, value, **values):

    from sqlalchemy import Table, MetaData

    try:
        async with engine.begin() as _conn:
            table = await _conn.run_sync(lambda _conn: Table(table_name, MetaData(), autoload_with=_conn))
            #column_names = [c.name for c in table.columns]
            #val = update(table).values(values).where(table.c.column_name == value)

            #statement = update(table).where(table.id.in_(values(values).where(table.c.choice_id == value))
            #result = await conn.execute(statement)
            #return result

    except Exception as e:
        raise e


async def db_get_table(engine, table_name, join_table_name=None, **options):

    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy import Table, MetaData, select

    try:

        async with engine.begin() as _conn:
            table = await _conn.run_sync(lambda _conn: Table(table_name, MetaData(), autoload_with=_conn))
            column_names = [c.name for c in table.columns]
            if join_table_name:
                join_table = await _conn.run_sync(lambda conn: Table(join_table_name, MetaData(), autoload_with=conn))
                column_names.extend([c.name for c in join_table.columns])

        if join_table_name:
            async with AsyncSession(engine) as session:
                statement = select(table, join_table)\
                    .filter(table.columns.poll_name == join_table_name)\
                    .filter(join_table.columns.id == table.columns.choice_id)\
                    .order_by(table.columns.num_votes.desc())
                result = await session.execute(statement)
        else:
            async with engine.connect() as _conn:
                #print("limit to colum wall matching:", options)
                if wall := options.get('wall'):
                    statement = table.select().where(table.columns.Wall == wall)
                    #    .order_by(table.columns.timestamp.desc())
                    result = await _conn.execute(statement)
                else:
                    result = await _conn.execute(select(table))

        # Convert to dictionary with the column name as key
        rows = []
        for row in result:
            rows.append(dict(zip(column_names, row)))

        return rows

    except Exception as e:
        raise e

