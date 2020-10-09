from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from CC_Flask import db
from CC_Flask.models import Engineerprofile
from CC_Flask.engineerprofile.forms import EngineerprofileForm

engineerprofiles = Blueprint('engineerprofiles', __name__)


@engineerprofiles.route("/engineerprofile/new", methods=['GET', 'POST'])
@login_required
def new_engineerprofile():
    form = EngineerprofileForm()
    if form.validate_on_submit():
        engineerprofile = Engineerprofile(firstname=form.firstname.data, lastname=form.lastname.data, uscitizen=form.uscitizen.data, github=form.github.data, linkedin=form.linkedin.data, personalsite=form.personalsite.data,
                                          reason=form.reason.data, experienceyrs=form.experienceyrs.data, languages=form.languages.data, interest=form.interest.data, blurb=form.blurb.data,
                                            author=current_user)
        db.session.add(engineerprofile)
        db.session.commit()
        flash('Your profile has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('engineersignup.html', title='Engineer Profile',
                           form=form, legend='Engineer Profile')


@engineerprofiles.route("/engineerprofile/<int:engineerprofile_id>")
def engineerprofile(engineerprofile_id):
    engineerprofile = Engineerprofile.query.get_or_404(engineerprofile_id)
    return render_template('engineerprofile.html',  firstname=engineerprofile.firstname, engineerprofile=engineerprofile, lastname=engineerprofile.lastname)


@engineerprofiles.route("/engineerprofile/<int:engineerprofile_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(engineerprofile_id):
    engineerprofile = Engineerprofile.query.get_or_404(engineerprofile_id)
    if engineerprofile.author != current_user:
        abort(403)
    form = EngineerprofileForm()
    if form.validate_on_submit():
        engineerprofile.firstname = form.firstname.data
        engineerprofile.lastname = form.lastname.data
        db.session.commit()
        flash('Your engineerprofile has been updated!', 'success')
        return redirect(url_for('engineerprofiles.engineerprofile', engineerprofile_id=engineerprofile.id))
    elif request.method == 'GET':
        form.firstname.data = engineerprofile.title
        form.lastname.data = engineerprofile.content
    return render_template('create_concept.html', title='Update Concept',
                           form=form, legend='Update Concept')


@engineerprofiles.route("/engineerprofile/<int:engineerprofile_id>/delete", methods=['POST'])
@login_required
def delete_engineerprofile(engineerprofile_id):
    engineerprofile = Engineerprofile.query.get_or_404(engineerprofile_id)
    if engineerprofile.author != current_user:
        abort(403)
    db.session.delete(engineerprofile)
    db.session.commit()
    flash('Your engineerprofile has been deleted!', 'success')
    return redirect(url_for('main.home'))