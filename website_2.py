#heyyy bbg

#Priority site for different symptoms
from flask import Flask, request, render_template,url_for, redirect, send_file 
from db import view, get_db
from user_input2 import registerDB
from api import diagnose


app = Flask(__name__)


#data structure
#each person has id - int
#each person has a list of symptoms - list[string] -> string points to the currently available dictionairy
#dicionairy of symptoms - dict[string, int] -> int points to the priority of the symptom


#PRIMARY SCREENING
#FULL NAME INPUTS
#GENDER INPUT
#SYMPTOMS INPUT


#SECONDARY SCREENING
#HISTORY INPUT
#FEELINGS INPUT
#LAST MEAL
#LAST DRINK

#REGISTERED NURSE INPUT
#LEVEL OF CONCIOUSNOUS INPUT
#VITALS INPUT

@app.route('/')
def hello():
    # print(view())
    # return send_file ('static\main.html')
    #redirect(url_for('Site/main.html'))
    return render_template('main.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
#     # print(view())
#     # return send_file ('static\main.html')
#     #redirect(url_for('Site/main.html'))

    if request.method == 'POST':
        # print("TEST", request.form)
        name = request.form['Name']
        sex = request.form['sex']
        age = request.form['age']
        symptoms = request.form['symptoms']
        history = request.form['history']
        last_meal = request.form['lastMeal']    
        last_drink = request.form['lastDrink']
    # if "submit" in request.form:
        print(name)
    #     print("TEST", request.form)
    return render_template('landingpage.html')



@app.route('/submit', methods=['POST'])
def submit(): 
    print("HELLLLO - Check if the data is recieved ")
    name = request.form['Name']
    sex = request.form['sex']
    age = request.form['age']
    symptoms = request.form['symptoms']
    history = request.form['history']
    last_meal = request.form['lastMeal']
    last_drink = request.form['lastDrink']
    email = "email@gmia.com"

    patient = {
        "name": name,
        "sex": sex,
        "age": age,
        "symptoms": symptoms,
        "history": history,
        "last_meal": last_meal,
        "last_drink": last_drink,
        "email": email
    }

                    
    registerDB(name, sex, symptoms, history, age, last_meal, last_drink, email)

    return render_template('waiting_page.html', patient=patient, predict=diagnose) 

@app.route('/nurse', methods=['GET', 'POST'])
def nurse():
    db=get_db()
    patients = db.execute(
        'SELECT * FROM users'
    ).fetchall()
    patients = [dict(patient) for patient in patients]
    db.close()

    return render_template('nurse.html',patients=patients)


# @app.route('/waiting_page', methods=['GET', 'POST'])
# def waiting_page():
#     return render_template('waiting_page.html', )

@app.route('/view/<int:id>', methods=('GET', 'POST'))
def view_user(id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
    if user is None:
        return "User not found", 404
    
    return dict(user)

@app.route('/doctor/<int:id>')
def doctor(id):
    print(id)
    db = get_db()
    doctors = db.execute('SELECT * FROM doctors').fetchall()
    
    doctors = [dict(doctor) for doctor in doctors]
    print(doctors)
    # user = dict(db.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone())
    return render_template('doctor_page.html',doctors=doctors)#, user=user)

@app.route('/send_doctor/<int:id>', methods=('GET', 'POST'))
def send_doctor(id):
    db = get_db()
    doctors = db.execute('SELECT * FROM doctors').fetchall()
    if doctor is None:
        return "Doctor not found", 404
    
    return [dict(doctor) for doctor in doctors]
# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #debug=True for development, False for production
#     # app.run(debug=True, host='
if __name__=='__main__':
    # create_tables()
    # add_col()
    app.debug=True #set to false for prod
    app.run(port=5000)