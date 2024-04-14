from wtfpeewee.orm import model_form
import wtforms
from database import Url

UrlForm = model_form(Url , exclude=['created_at' , 'shorted_url'])