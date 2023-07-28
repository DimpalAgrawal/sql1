
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import csv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///page.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/customer'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# this is the program of 404 video
class FilledFiller(db.Model):
   dcid = db.Column(db.Integer, primary_key=True)
   Student_Number = db.Column(db.Integer)
   StudentEmail = db.Column(db.String(50))
   Username = db.Column(db.String(50))
   Password = db.Column(db.String(30))
   # Student_Email= db.relationship('purchase', backref='customer')

# Step 2: This function is used to read the data from the csv file.
def read_csv_file(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Step 3: Insert data into the SQLite table
def insert_data_into_table(data):
    for row in data:
        dcid = row['dcid']
        existing_entry = FilledFiller.query.get(dcid)
        if existing_entry:
            # If the entry already exists, you may update it with new data if needed
            existing_entry.Student_Number = row['Student_Number']
            existing_entry.StudentEmail = row['StudentEmail']
            existing_entry.Username = row['Username']
            existing_entry.Password = row['Password']
        else:
            # If the entry does not exist, insert a new one
            new_entry = FilledFiller(dcid=dcid, Student_Number=row['Student_Number'], StudentEmail=row['StudentEmail'], Username=row['Username'], Password=row['Password'])
            db.session.add(new_entry)
    db.session.commit()

def fetch_data_from_table():
    try:
        data = FilledFiller.query.all()
        return data
    except:
        print("Some Error is there")
        return []


        






# @app.route('/getname/<int:customer_id>' ,methods=['GET'])
# def getname(customer_id):
#    Customer = customer.query.get(customer_id)
#    return 'Name : {}'.format(Customer.name)





# class purchase(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
#    price = db.Column(db.Integer)

# @app.route('/thread/<int:page_num>')
# def thread(page_num):
    
#     threads = Thread.query.paginate(per_page=5, page = page_num, error_out = True )
    
#     return render_template('index.html', threads = threads)

if __name__ == '__main__':
    app.run(port=5005,debug = True)
    # csv_file = "fieldfiller3.csv"
    # csv_data = read_csv_file(csv_file)
    # insert_data_into_table(csv_data)
    # print(csv_data)
    fetch_data = fetch_data_from_table()
    for row in fetch_data:
        print(f"dcid:{row.dcid}, Student_Number: {row.Student_Number}, StudentEmail: {row.StudentEmail}, Username: {row.Username}, Password: {row.Password}")

        

   
    
   




