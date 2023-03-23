from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint

MONGO_HOST = #IP ADDRESS
MONGO_DB = #DATABASE NAME
MONGO_USER = #USERNAME
MONGO_PASS = #PASSWORD

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username = MONGO_USER,
    ssh_password = MONGO_PASS,
    remote_bind_address = ('127.0.0.1', 22)
    )
    
server.start()

client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
df = client[MONGO_DB]
pprint.pprint(df.collection_names())

server.stop()
