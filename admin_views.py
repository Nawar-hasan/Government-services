from flask import render_template, request
from models import User, Order
from app import app  # تأكد من استيراد كائن التطبيق الصحيح

@app.route('/admin/customers', methods=['GET', 'POST'])
def admin_customers():
    if request.method == 'POST':
        national_id = request.form.get('national_id')
        if national_id:
            customer = User.query.filter_by(id=national_id).first()
            if customer:
                orders = Order.query.filter_by(user_id=national_id).all()
                return render_template('admin_customer_details.html', customer=customer, orders=orders)
            else:
                return render_template('admin_customers.html', error='Customer not found')

    return render_template('admin_customers.html')
