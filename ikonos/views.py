from flask import render_template, request
from ikonos import app, db
# from ikonos.worker import conn
from ikonos.models import Enquiry
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

        enquiry = Enquiry(
            email=email,
            first_name=first_name,
            last_name=last_name,
            message=message
        )
        db.session.add(enquiry)
        db.session.commit()

    return render_template('index.html', results=results)
