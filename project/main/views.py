from project.main import main_blueprint
from flask import render_template
from project.models import Task

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')

@main_blueprint.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('main/tasks.html')