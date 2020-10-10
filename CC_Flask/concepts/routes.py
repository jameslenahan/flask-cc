from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from CC_Flask import db
from CC_Flask.models import Concept
from CC_Flask.concepts.forms import ConceptForm

concepts = Blueprint('concepts', __name__)


@concepts.route("/concept/new", methods=['GET', 'POST'])
@login_required
def new_concept():
    form = ConceptForm()
    if form.validate_on_submit():
        concept = Concept(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(concept)
        db.session.commit()
        flash('Your concept has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_concept.html', title='New concept',
                           form=form, legend='New concept')


@concepts.route("/concept/<int:concept_id>")
def concept(concept_id):
    concept = Concept.query.get_or_404(concept_id)
    return render_template('concept.html', title=concept.title, concept=concept)


@concepts.route("/concept/<int:concept_id>/update", methods=['GET', 'POST'])
@login_required
def update_concept(concept_id):
    concept = Concept.query.get_or_404(concept_id)
    if concept.author != current_user:
        abort(403)
    form = ConceptForm()
    if form.validate_on_submit():
        concept.title = form.title.data
        concept.content = form.content.data
        db.session.commit()
        flash('Your concept has been updated!', 'success')
        return redirect(url_for('concepts.concept', concept_id=concept.id))
    elif request.method == 'GET':
        form.title.data = concept.title
        form.content.data = concept.content
    return render_template('create_concept.html', title='Update Concept',
                           form=form, legend='Update Concept')


@concepts.route("/concept/<int:concept_id>/delete", methods=['POST'])
@login_required
def delete_concept(concept_id):
    concept = Concept.query.get_or_404(concept_id)
    if concept.author != current_user:
        abort(403)
    db.session.delete(concept)
    db.session.commit()
    flash('Your concept has been deleted!', 'success')
    return redirect(url_for('main.home'))