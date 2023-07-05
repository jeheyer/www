

async def db_insert(engine, table_name: str, values={}):

    from sqlalchemy import Table, MetaData

    try:
        async with engine.begin() as conn:
            table = await conn.run_sync(lambda conn: Table(table_name, MetaData(), autoload_with=conn))
            statement = table.insert().values(values)
            result = await conn.execute(statement)
            return result

    except Exception as e:
        raise e


async def main():

    from sqlalchemy.ext.asyncio import create_async_engine

    db_hostname = "100.77.77.77"
    db_username = "primus"
    db_password = "frizfry"
    db_name = "primus"
    db_driver = "mysql+asyncmy"

    engine = create_async_engine("{}://{}:{}@{}/{}".format(db_driver, db_username, db_password, db_hostname, db_name))
    values = {'poll_name': "albums", 'choice_id': 71,  'num_votes': 69}
    result = await db_insert(engine, "polls", values)


if __name__ == "__main__":

    from asyncio import run

    run(main())