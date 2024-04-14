from flask import Flask , render_template , request , redirect , url_for
from forms import UrlForm
from database import Url 
from flask_htmx import HTMX 
import zlib



app = Flask(__name__)
htmx = HTMX(app)

@app.route('/' , methods=['GET', 'POST'])
def home() :
   
    url = Url()

    if request.method == 'POST':
        form = UrlForm(request.form, shorted_url = 'https://flask-admin.readthedocs.io/' ,  obj=url)
        
        if form.validate():           
            form.populate_obj(url)

            try : 
                if htmx : 
                    suffix = str(zlib.crc32(bytes( url.main_url ,'utf-8')))
                    shorted_url = request.root_url + suffix
                    url.shorted_url = shorted_url
                    url.suffix = suffix
                    url.save()
                    message = 'succesfully shorted your url' 
                    succed = True
                    
                    context = {
                        'message': message , 
                        'succed' : succed , 
                        'shorted_url' : shorted_url
                    }
                    
                    return render_template('message.html' , context=context)
            except TypeError : 
                message = 'enter valid url' 
                succed = False
                context = {
                    'message' : message , 
                    'succed' : succed
                }
                return render_template('message.html' , context= context)
        else : 
            message = 'enter valid url' 
            succed = False
            context = {
                'message' : message , 
                'succed' : succed
            }
            return render_template('message.html' , context= context)

                
            
           
    else:
        form = UrlForm(obj=url)
    return render_template('home.html', form = form)

@app.route('/<suffix>') 
def redirect_shorted_urls(suffix):
    try :  
        url = Url.get(Url.suffix == suffix)
        main_url = url.main_url 
        return redirect(main_url , code=302)
    except Url.DoesNotExist: 
        return redirect(url_for('notFound'))
    
@app.route('/404')
def notFound():
    return render_template('404.html')



if __name__ == '__main__': 
    app.run()