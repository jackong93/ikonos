from ikonos import db
from ikonos.models import Enquiry


def insert_to_enquiry(email, first_name, last_name, message):
    enquiry = Enquiry(
        email=email,
        first_name=first_name,
        last_name=last_name,
        message=message
    )
    db.session.add(enquiry)
    db.session.commit()
