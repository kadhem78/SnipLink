from peewee import * 
from fields import UrlField
from datetime import datetime
from playhouse.migrate import *
from flask import abort
from dotenv import load_dotenv
import os 

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('db_name'),  
    user=os.getenv('db_user'),  
    password=os.getenv('db_password'),  
    host=os.getenv('db_host'))  

class BaseModel(Model):
    class Meta:
        database = db

class Url(BaseModel) : 
    main_url = UrlField()
    shorted_url = UrlField()
    suffix = CharField(null=True)
    created_at = DateTimeField(default = datetime.now)


def get_or_404(query, *expr):
    try:
        return query.where(*expr).get()
    except DoesNotExist:
        abort(404)


