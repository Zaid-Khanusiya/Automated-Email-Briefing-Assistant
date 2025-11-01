from app import api,app
from views import *

api.add_resource(Home,'/')
api.add_resource(MainAPI,'/main')