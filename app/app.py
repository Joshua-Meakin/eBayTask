from flask import Flask, render_template, request, flash
from forms import SubmitForm
from service import dis_calculate
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def calculate():
    form = SubmitForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('index.html', form=form, output="")
        else:
            pickup_postcode = form.p_postcode.data
            delivery_postcode = form.d_postcode.data
            vehicle = form.vehicle.data
            res_dict = dis_calculate(pickup_postcode=pickup_postcode, delivery_postcode=delivery_postcode, vehicle=vehicle)
            if 'error' in res_dict:
               return render_template('index.html', form=form, output="An error occurred, please input a valid postcode.")
            else:
               return render_template('index.html', form=form, output="A delivery from {} to {} using a {} will cost you £{}".format(res_dict["Pickup Postcode"], res_dict["Delivery Postcode"], res_dict["Vehicle"], res_dict["Price"]))       
    elif request.method == 'GET':
        return render_template('index.html', form=form, output="")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
