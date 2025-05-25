from db import get_db
acceptingData = True

nurse_accepting = "Yes"

#Return patient id?
def registerDB(name, sex, symptoms,history,age, last_meal, last_drink, email):
    error = None

    db = get_db()
    try:
        cursor = db.execute("INSERT INTO users (name, gender, symptoms, age, email, history, lastMeal, lastDrink) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, sex, symptoms, age, email, history, last_meal, last_drink))
        db.commit()
    except db.IntegrityError:
        error = "User already exists"
    finally:
        db.close()
    if error:
        return error
    else:
        print(error)
        return cursor.lastrowid
    
#recieves the code from the html "landingpage" and submits to sql database 


    
