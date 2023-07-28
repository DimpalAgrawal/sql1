
# @app.route('/getname/<int:customer_id>' ,methods=['GET'])
# def getname(customer_id):
#    Customer = customer.query.get(customer_id)
#    return 'Name : {}'.format(Customer.name)





# class purchase(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
#    price = db.Column(db.Integer)
