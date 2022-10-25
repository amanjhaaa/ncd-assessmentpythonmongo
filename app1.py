
# from crypt import methods
from flask import Flask,render_template,request
app = Flask(__name__)#interface between webserver and web application


@app.route("/" , methods = ['GET','POST'])
def home():
    return render_template("registration.html")  

@app.route('/res',methods=['GET',"POST"])
def res():
    if request.method == "POST":
        firstname = request.form.get('firstname')
    return render_template('result1.html', fname=firstname)   




@app.route('/login/', methods=['GET',"POST"])
def ncd():
    return render_template('ncd1.html')

@app.route('/result',methods=['GET',"POST"])
def result():
    if request.method == "POST":
        count = 0

# getting the value for age

        while True :
        
            age = request.form.get('age')
            
            smoke = request.form.get('smoke')
            
            alcohol =request.form.get('alcohol')

            
            measurement = request.form.get('measurement')
            
            physical =  request.form.get('physical')



            disease_family_hist =  request.form.get('history')

            count = int(age)+int(smoke)+int(alcohol)+int(measurement)+int(physical)+int(disease_family_hist)
            add = int(count)
            print(add)
            res=""
            if count>4:
                res="you need screening" 
            else:
                res="No screening needed"

            return render_template('result1.html', add1=add,prescription=res)
    return render_template('result1.html', add1="result not found in session.")

@app.route('/back',methods=['GET',"POST"])  
def back():  
    if request.method == 'POST':
        return render_template("ncd1.html");  
if __name__ == '__main__':
    app.run(debug = True)  
    
