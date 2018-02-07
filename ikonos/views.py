from flask import render_template, request
from ikonos import app
# from ikonos.worker import conn
from ikonos.utils.enquiry import insert_to_enquiry
# from rq import Queue
# from rq.job import Job

# q = Queue(connection=conn)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == "POST":
        # get url that the person has entered
        email = request.form['email']
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        message = request.form['msg']

        results = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "message": message
        }
        insert_to_enquiry(
            email=email,
            first_name=first_name,
            last_name=last_name,
            message=message
        )

    return render_template('index.html', results=results)
