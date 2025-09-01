import re
import pathlib
import tomli
import yaml
import json
import configparser


def get_dns_servers_from_token(token="testing1234") -> dict:

    try:
        # Override if this is test token
        if token == "testing1234":
            dns_resolvers = ["192.0.2.53", "198.51.100.53", "203.0.113.53"]
        else:
            # Open the BIND log file for A record queries
            dns_resolvers = []
            dns_resolvers_hash = dict()
            bind_log_file = LogFile("/var/log/named/query.log", " IN A ")
            for line in bind_log_file.contents:
                if token in line[7]:
                    source_ip, source_port = line[6].split("#")
                    if not re.match("10.|192.168.", source_ip) and source_ip not in dns_resolvers_hash:
                        dns_resolvers_hash[source_ip] = True
                        dns_resolvers.append(source_ip)

        return dict(dns_resolvers=dns_resolvers)

    except Exception as e:
        raise Exception(e)


def read_file(file_name: str) -> dict:

    if path := pathlib.Path(file_name):
        if not path.is_file():
            open(path, 'a').close()  # Create an empty file
        if path.stat().st_size == 0:
            return {}  # File exists, but is empty
    else:
        raise f"Error occurred while reading '{path}'"

    file_format = file_name.split('.')[-1].lower()  # Auto-determine file type by examining extension

    try:
        if not path.is_file() or path.stat().st_size == 0:
            return {}
        contents = path.read_text(encoding='utf-8')
        if file_format == 'yaml':
            return yaml.load(contents, Loader=yaml.FullLoader)
        if file_format == 'json':
            return json.loads(contents)
        if file_format == 'toml':
            return tomli.loads(contents)
        if file_format == 'cfg':
            config = configparser.ConfigParser()
            return {i: v for i, v in enumerate(config.read(path))}
        raise f"unhandled file format '{file_format}'"
    except Exception as e:
        raise e

    return {}


def ConvertToDict(contents: list, file_type: str) -> list:

    data = []
    if file_type == "csv":
        for line in contents:
            line = line.rstrip()
            print(line)
            parts = line.split(",")
            obj = {}
            for i in range(0,len(parts)):
                obj[i] = parts[i]
            data.append(obj)

    return data

class LogFile():

    def __init__(self, filename, filter = None):

        self.filename = filename
        self.contents = []
        self.num_lines = 0
        self.ReadFile(filter)

    def ReadFile(self, filter = None):

        try:
            fh = open(self.filename,"r")
        except:
            raise Exception("ERROR: could not read log file '" + self.filename + "'")

        for line in fh:
            if filter:    
                if filter in line:
                    parts = line.split(" ")
                    self.contents.append(parts)
            else:
                parts = line.split(" ")
                self.contents.append(parts)
            self.num_lines += 1

        fh.close()

