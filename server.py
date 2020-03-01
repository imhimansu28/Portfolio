from flask import Flask , render_template , request, url_for, redirect 
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html') 


@app.route('/<string:page_name>')

def my_page(page_name):
    return render_template(page_name)

# create a database 

def write_to_file(data):
    with open('database.txt', mode= 'a') as database :
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject} , {message}")



@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return render_template('./thanku.html')
    else:
        return 'something went worng. Try again !'



