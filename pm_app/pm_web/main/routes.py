# All flask Routes that controls the access and usage of each web
# Integration of the back end and front-end functionality is done 

import random
from .. import app
from ..users.forms import Register_form, login_form, Project_form, Task_form
from ..modules.models import user, project, task
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, current_user, logout_user, login_required



def generate_random_hex_color():
    """Generates a random hex color value in the format #RRGGBB."""
    letters = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += random.choice(letters)
    return color

@app.route("/", methods=['GET', 'POST'])
@login_required
def home():
    '''
    Home route for our project management page.
    
    You can add 'cascade=true' to the 'save()' function to save referencefields,
    but i didn't seem to need it guess i.e Project.save(cascade=True)
    '''

    form = Project_form()
    User = user.objects(name=current_user.name).first()
    # flash(User.id)
    color = generate_random_hex_color()
    if form.validate_on_submit():
        Project = project(project_name=form.project_name.data, description=form.description.data, color=color)
        Project.save()
        User.project_id.append(Project)
        User.save()
        return redirect(url_for('boards'))
    return render_template('index.html', form=form, user=User)


@app.route("/boards", methods=['GET', 'POST'])
@login_required
def boards():
    '''
    The Boards route: This routes is used to display available projects
    and also addition of new tasks.
    Users can check and monitor their progress on this page.
    '''
    form = Task_form()
    User= user.objects(name=current_user.name).first()
    projects = []
    for project_object in User.project_id:
        projects.append(project_object)
    color = generate_random_hex_color()
    # Tasks = task.objects()
    # flash(projects)
    return render_template('boards.html', projects=projects, color=color, form=form)


@app.route("/boards/<string:board>", methods=['GET','POST'])
@login_required
def boards_task(board):
    '''
    Boards_task Route: This is the route used to create tasks under a particular
    project.
    board: this is ppassed in into the url so that the specific project can be queried
    and the required task will be added under it.
    '''
    form = Task_form()
    User= user.objects(name=current_user.name).first()
    Project_object = project.objects(id=board).first()
    # flash(Project_object)
    projects = []
    for project_object in User.project_id:
        projects.append(project_object)
    if form.validate_on_submit():
        new_task = task(task=form.task.data, priority=form.priority.data)
        new_task.save()
        Project_object.task_id.append(new_task)
        Project_object.save()

    return redirect(url_for('boards'))


@app.route("/projects")
@login_required
def projects():
    '''
    projects route: This route displays all the available projects to the user 
    and how far they have gone in its completion.
    '''
    User = user.objects(name=current_user.name).first()
    projects = []
    for project_object in User.project_id:
        projects.append(project_object)
    return render_template('projects.html', projects=projects)

@app.route("/login", methods=['GET','POST'])
def login():
    '''
    login Route: This is the access point of users to the project management
    website.
    '''
    form = login_form()
    if form.validate_on_submit():
        User = user.objects(email=form.email.data).first()
        if User and User.email == form.email.data:
            login_user(User)
            next_page = request.args.get('next')
            flash(f'{User.name} {next_page}you have a succesful login')
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash('Login terminated')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    '''
    reegister route: Here new users can create an account with their data to
    be able to access our project management software.
    '''
    form = Register_form()
    if form.validate_on_submit():
        User = user(name=form.name.data, email=form.email.data, password=form.password.data)
        User.save()
        flash(f'{form.name.data}, Login sucessful. Please check email and password', 'danger')
        return redirect(url_for("home"))
    return render_template('register.html', form=form)

@app.route("/logout", methods=['GET','POST'])
def logout():
    '''
    logout route: Users can log out of their account in their browsers
    for safety or any other purposes.
    '''
    logout_user()
    return redirect(url_for('login'))