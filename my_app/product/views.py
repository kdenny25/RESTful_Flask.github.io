# RESTful_Flask/my_app/product/views.py

from flask import Blueprint, abort, request, jsonify
from flask.views import MethodView
from my_app import db, app
from my_app.product.models import Contact_Us

comment_list = Blueprint('comment_list', __name__)

@comment_list.route('/')
@comment_list.route('/home')
def home():
    return "Welcome to the Contact List Home Page."

class ContactView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            contacts = Contact_Us.query.paginate(page, 10).items
            res = {}
            for contact in contacts:
                res[contact.id] = {
                    'name': contact.name,
                    'comment': contact.comment
                }
        else:
            contact = Contact_Us.query.filter_by(id=id).first()
            if not contact:
                abort(404)
            res = {
                'name': contact.name,
                'comment': contact.comment
            }
        return jsonify(res)

    def post(self):
        name = request.form.get('name')
        comment = request.form.get('comment')
        contact = Contact_Us(name,comment)
        db.session.add(contact)
        db.session.commit()
        return jsonify({contact.id: {
            'name': contact.name,
            'comment': contact.comment
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id
        return

contact_view = ContactView.as_view('contact_view')
app.add_url_rule(
    '/contact/', view_func=contact_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/contact/<int:id>', view_func=contact_view, methods=['GET']
)