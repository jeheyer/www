#!/usr/bin/env python3

import platform
import socket
import sys
import traceback


def get_client_ip(headers: dict = None) -> str:

    try:
        # Convert all keys to lower case for consistency
        headers = {k.lower(): v for k, v in headers.items()}

        if x_appengine_user_ip := headers.get('http_x_appengine_user_ip'):
            return x_appengine_user_ip.split(',')[0].strip()

        behind_cdn = False
        if via := headers.get('http_via'):
            behind_cdn = True
        else:
            if "cloudfront" in headers.get('user_agent', "Unknown").lower():
                behind_cdn = True
        if not behind_cdn:
            if x_real_ip := headers.get('http_x_real_ip'):
                return x_real_ip
        if x_forwarded_for := headers.get('http_x_forwarded_for'):
            if "," in x_forwarded_for:
                if ", " in x_forwarded_for:
                    x_fwd_index = -3 if behind_cdn else -2
                else:
                    x_fwd_index = -2  # Stupid CloudRun
                x_forwarded_for = x_forwarded_for.split(",")[x_fwd_index]
            return x_forwarded_for.strip()
        return _.get('remote_addr', "127.0.0.1")

    except Exception as e:
        raise Exception(traceback.format_exc())


def ping(headers: dict = None, request: any = None) -> dict:

    info = {}

    header_names = ('HTTP_HOST', 'SERVER_NAME', 'SERVER_ADDR', 'SERVER_SOFTWARE', 'SERVER_PROTOCOL', 'SERVER_PORT',
        'REMOTE_ADDR', 'HTTP_X_REAL_IP', 
        'HTTP_X_FORWARDED_FOR', 'HTTP_X_FORWARDED_PROTO', 'HTTP_X_FORWARDED_PORT', 'HTTP_X_FORWARDED_HOST',
        'HTTP_CONNECTION', 'HTTP_VIA', 'PATH_INFO', 'REQUEST_URI', 'RAW_URI', 'SCRIPT_NAME', 'QUERY_STRING',
        'HTTP_USER_AGENT', 'REQUEST_METHOD',
    )

    try:

        # Standard environment variables in dictionary
        if isinstance(headers, dict):
            info['headers'] = str(headers)
            for header_name in header_names:
                header_name = header_name.lower()
                info[header_name] = headers.get(header_name.upper())
            if 'request_uri' not in info:
                info['request_uri'] = headers.get('RAW_URI')
            if 'raw_uri' not in info:
                info['raw_uri'] = headers.get('REQUEST_URI')

        # Request object
        if request:
            for header_name in header_names:
                try:
                    header_name = header_name.lower()
                    info[header_name] = str(getattr(request, header_name))
                except AttributeError:
                    info[header_name] = None
                else:
                    continue

            info['server_name'] = platform.node()
            info['server_addr'] = socket.gethostbyname(info['server_name'])
            info['http_user_agent'] = request.headers.get("User-Agent")
            info['http_connection'] = request.headers.get('Connection')

            if 'quart' in str(request.__class__):
                info['http_host'] = request.host.split(':')[0]
                info['path_info'] = request.path
                info['server_port'] = int(request.server[1])
                info['server_protocol'] = "HTTP/" + request.http_version
                info['remote_addr'] = request.remote_addr
                info['headers'] = str(request.headers)
                info['server_protocol'] = "HTTP/" + request.http_version
                info['via'] = request.headers.get('via')
                info['http_x_real_ip'] = request.headers.get('X-Real-IP')
                info['http_x_forwarded_for'] = request.headers.get('X-Forwarded-For')
                info['http_x_forwarded_proto'] = request.headers.get('X-Forwarded-Proto')
                info['http_x_forwarded_host'] = request.headers.get('X-Forwarded-Host')
                info['http_x_forwarded_port'] = request.headers.get('X-Forwarded-Port')
                #info['headers'] = str(request.headers)

            if 'starlette' in str(request.__class__):
                info['http_host'] = request.headers['host'].split(':')[0]
                info['path_info'] = request.url.path
                info['server_port'] = int(request.get('server', [])[1])
                #info['remote_addr'] = request['client'][0]
                info['remote_addr'] = request.client.host
                info['headers'] = str(request.headers)
                info['server_protocol'] = "HTTP/" + request.get('http_version')
                info['request_method'] = request.method
                info['via'] = request.headers.get('via')
                info['http_x_real_ip'] = request.headers.get('x-real-ip')
                info['http_x_forwarded_for'] = request.headers.get('x-forwarded-for')
                info['http_x_forwarded_proto'] = request.headers.get('x-forwarded-proto')
                info['http_x_forwarded_host'] = request.headers.get('x-forwarded-host')
                info['http_x_forwarded_port'] = request.headers.get('x-forwarded-port')
                info['client_ip'] = request.client.host
                #info['headers'] = request.headers

            info['script_name'] = info['path_info']

        info['client_ip'] = get_client_ip(info)
        info['platform_node'] = platform.node()
        info['platform_os'] = "{} {}".format(platform.system(), platform.release())
        info['platform_cpu'] = str(platform.machine())
        info['python_info'] = str(sys.version).split()[0]
        #info['environ'] = str(environ)

        return info

    except Exception as e:
        raise Exception(traceback.format_exc())


def mortgage(options: dict = None) -> dict:

    from financial import GetPaymentData

    try:
        return GetPaymentData(options)
    except Exception as e:
        raise Exception(traceback.format_exc())


async def graffiti(db_name, wall):

    from database import db_engine, db_engine_dispose, db_get_table

    try:
        engine = await db_engine(db_name)
        posts = await db_get_table(engine, "graffiti", where={'wall': wall})
        await db_engine_dispose(engine)
        return posts
    except Exception as e:
        raise Exception(traceback.format_exc())


async def polls(db_name: str, db_join_table: str) -> list:

    from database import db_engine, db_engine_dispose, db_get_table

    try:
        engine = await db_engine(db_name)
        results = await db_get_table(engine, "polls", join_table_name=db_join_table)
        await db_engine_dispose(engine)
        return results
    except Exception as e:
        raise Exception(traceback.format_exc())


async def get_table(db_name: str, db_table: str = None, db_join_table: str = None, wall: str = None) -> list:

    from database import db_engine, db_engine_dispose, db_get_table

    try:
        engine = await db_engine(db_name)
        results = await db_get_table(engine, db_table)
        await db_engine_dispose(engine)
        return results
    except Exception as e:
        raise Exception(traceback.format_exc())


    """
        if db_table == "polls":
            result = await get_table(engine, db_table, db_join_table, {'wall': wall, 'name': name, 'text': text})
        if db_table == "graffiti":
            result = await get_table(engine, db_table, where={'wall': wall})
        await db_engine_dispose(engine)

        async with engine.begin() as conn:
            table = await conn.run_sync(lambda conn: Table(db_table, MetaData(), autoload_with=conn))
            column_names = [c.name for c in table.columns]
            if db_join_table:
                join_table = await conn.run_sync(lambda conn: Table(db_join_table, MetaData(), autoload_with=conn))
                column_names.extend([c.name for c in join_table.columns])

        if db_table == "polls":
            async with AsyncSession(engine) as session:
                statement = select(table, join_table)\
                    .filter(table.columns.poll_name == db_join_table)\
                    .filter(join_table.columns.id == table.columns.choice_id)\
                    .order_by(table.columns.num_votes.desc())
                result = await session.execute(statement)
            await db_engine_dispose(engine, session)
        else:
            async with engine.connect() as conn:
                if db_table == "graffiti":
                    statement = table.select().where(table.columns.wall == wall).order_by(table.columns.timestamp.desc())
                    result = await conn.execute(statement)
                else:
                    result = await conn.execute(select(table))
            await db_engine_dispose(engine)

        # Convert to dictionary with the column name as key
        rows = []
        for row in result:
            rows.append(dict(zip(column_names, row)))

        return rows

    except:
        raise Exception(traceback.format_exc())
"""


async def graffiti_post(db_name: str, wall: str, graffiti_url: str = None, name: str = None, text: str = None):

    from database import db_engine, db_engine_dispose, db_insert

    if not graffiti_url:
        graffiti_url = "http://localhost"
    if not name:
        name = "Anonymous Coward"
    if not text:
        text = "I have nothing to say"

    try:
        engine = await db_engine(db_name)
        row = {'wall': wall, 'name': name, 'text': text}
        result = await db_insert(engine, "graffiti", row)
        await db_engine_dispose(engine)
        return f"{graffiti_url}?wall={wall}"
    except Exception as e:
        raise Exception(traceback.format_exc())


async def poll_vote(db_name: str, poll_name: str, poll_url: str, poll_desc: str, choice_id: int) -> str:

    from database import db_engine, db_engine_dispose, db_get_table, db_insert, db_update

    if not poll_url:
        poll_url = "http://localhost"

    poll_url = f"{poll_url}?poll_name={poll_name}&poll_desc={poll_desc}"

    choice_id = int(choice_id)
    if choice_id < 1:
        return poll_url

    db_row = {'poll_name': poll_name, 'choice_id': choice_id, 'num_votes': 0}
    try:

        # Connect to database
        engine = await db_engine(db_name)

        # Check if there's existing votes for this choice
        num_votes = 0
        results = await db_get_table(engine, "polls", join_table_name=poll_name)
        for _ in results:
            if int(_['choice_id']) == choice_id:
                num_votes = _.get('num_votes', 0)
                break

        # Update the database
        db_row['num_votes'] = num_votes + 1
        if num_votes > 0:
            result = await db_update(engine, "polls", "choice_id", choice_id, db_row)
        else:
            result = await db_insert(engine, "polls", db_row)
        """
        session = orm.sessionmaker(bind=engine)()

        table = Table("polls", MetaData(), autoload_with=engine)

        # See if this choice has existing votes
        result = session.query(table.columns.num_votes)\
            .filter(table.columns.poll_name == poll_name)\
            .filter(table.columns.choice_id == choice_id)\
            .all()
        if len(result) > 0:
            num_votes = result[0][0] + 1
            statement = table.update()\
                .filter(table.columns.poll_name == poll_name)\
                .filter(table.columns.choice_id == choice_id)\
                .values(num_votes=num_votes)
        else:
            statement = table.insert().values(poll_name=poll_name, choice_id=choice_id, num_votes=1)

        result = session.execute(statement)
        """

        await db_engine_dispose(engine)

        return poll_url

    except Exception as e:
        raise Exception(traceback.format_exc())


def get_geoip_info(geoiplist: list = ["127.0.0.1"]) -> list:

    from geoip import GeoIPList

    try:
        return GeoIPList(geoiplist).geoips
    except Exception as e:
        raise Exception(traceback.format_exc())


def get_dns_servers(token: str = "testing1234") -> list:

    from system_tools import get_dns_servers_from_token

    try:
        _ = get_dns_servers_from_token(token)
        return _.get('dns_resolvers', [])
    except Exception as e:
        raise Exception(traceback.format_exc())


if __name__ == '__main__':

    from pprint import pprint
    from os import environ

    _ = dict(environ)
    pprint(ping(_))

