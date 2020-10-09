from flask import render_template, request, Blueprint
from CC_Flask.models import Concept

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    concepts = Concept.query.order_by(Concept.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', concepts=concepts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')



