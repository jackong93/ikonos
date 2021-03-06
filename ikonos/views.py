from flask import render_template, request, jsonify
from rq import Queue
from rq.job import Job

from ikonos import app
from ikonos.models import Enquiry
from ikonos.worker import conn
from ikonos.utils.enquiry import insert_to_enquiry

q = Queue(connection=conn)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    # return render_template('demo.html')
    return "Coming soon..."


@app.route('/enquire', methods=['GET', 'POST'])
def enquire():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if request.method == 'POST':
            job = q.enqueue_call(
                func=insert_to_enquiry,
                kwargs=data,
                result_ttl=5000
            )
            return job.get_id()
    return render_template('enquire.html')


@app.route('/enquiry/<job_key>', methods=['GET'])
def enquiry(job_key):
    job = Job.fetch(job_key, connection=conn)
    if job.is_finished:
        result = Enquiry.query.filter_by(id=job.result).first()
        return jsonify(result._asdict())
    else:
        return "Running...", 202
