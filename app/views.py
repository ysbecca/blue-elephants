from app import app
from flask import render_template, flash
from .forms import IdeaForm


@app.route('/', methods=['GET', 'POST'])
def index():

	form = IdeaForm()

	if form.validate_on_submit():
		flash("Succesfully received bright new idea: " + str(form.idea.data))
		
	return render_template('index.html', form=form)
