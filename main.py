from fastapi import FastAPI
from db.mongodb_utils import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', close_mongo_connection)
