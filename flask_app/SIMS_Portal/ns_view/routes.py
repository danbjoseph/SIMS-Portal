from flask import (
	Blueprint, render_template
)
from SIMS_Portal import db
from flask_sqlalchemy import SQLAlchemy
from SIMS_Portal.models import NationalSociety

ns_view = Blueprint('ns_view', __name__)

@ns_view.route('/ns_view/<int:ns_go_id>')
def ns_page(ns_go_id):
	ns_selected = db.session.query(NationalSociety).filter(NationalSociety.ns_go_id == ns_go_id).first()
	# associated_members or something, declare 2 tables referenced, do a join, reference an additional dot notation on the html
	return render_template('ns_view.html', ns_selected = ns_selected )
	
