from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
model = pickle.load(open('l.pkl', 'rb'))
app = Flask(__name__)
@app.route('/',methods=["GET"])
def main():
    return render_template('index.html')
@app.route('/s',methods=["GET","POST"])
def s(): 
    if request.method=="POST" :
        g=(request.form['gender'])
        if(g=="Male"):
            gender_M=1
        else:
            gender_M=0
        ten=(request.form['10'])
        twelve=(request.form['12'])
        degree=(request.form['degree'])
        stream=(request.form['stream'])
        if stream=='Commerce':
            hsc_s_Commerce=1
            hsc_s_Science=0
        if stream=='Science':
            hsc_s_Science=1
            hsc_s_Commerce=0
        if stream=='Arts':
            hsc_s_Science=0
            hsc_s_Commerce=0

        ug=(request.form['undergrad'])
        if ug=='Comm&Mgmt':
            degree_t_Others=0
            degree_t_Sci=0
        if ug=='Sci&Tech':
            degree_t_Others=0
            degree_t_Sci=1
        if ug=='Other':
            degree_t_Others=1
            degree_t_Sci=0
        wex=(request.form['workex'])
        if wex=='Yes':
            w=1
        else:
            w=0
        emptest=(request.form['emptest'])
        s=(request.form["special"])
        if s=='Mkt&HR':
            special=1
        else:
            special=0
        status=(request.form['status'])
        if status=="Placed":
            p=1
        else:
            p=0
        output=model.predict([[ten,twelve,degree,emptest,gender_M,hsc_s_Commerce,hsc_s_Science,
        degree_t_Others,degree_t_Sci,w,special,p]])
        output=output.round(2)
        if output<0:
            return render_template('index.html',text="Salary could not be displayed")
        else:
            return render_template('index.html',text="Your predicted salary is {}".format(output))
    return render_template("index.html")   
if __name__ == '__main__':
    app.run(debug=True)

