from configparser import ConfigParser

try:
    config = ConfigParser()
    config.read("conf/application.conf")
    # server
    server_path = config.get("server", "server_path")
    port_no = config.get("server", "port")
    # mongo
    uri = config.get("mongo_connect", "uri")
    mongo_port = config.get("mongo_connect", "port")
except Exception as e:
    print(e)
