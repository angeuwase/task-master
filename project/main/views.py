from project.main import main_blueprint
from flask import render_template, url_for, redirect
from project.models import Task
from project.forms import TaskForm, UpdateForm
from flask_login import current_user, login_required
from project import db




@main_blueprint.route('/')
def index():
    return render_template('main/index.html')

@main_blueprint.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = TaskForm()
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    completed_tasks = Task.query.filter_by(completed=True).all()
    if form.validate_on_submit():
        content = form.content.data
        new_task = Task(content=content, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.tasks'))

    return render_template('main/tasks.html', form=form, tasks=tasks, completed_tasks=completed_tasks)


@main_blueprint.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('main.tasks'))

@main_blueprint.route('/mark_complete/<int:task_id>')
@login_required
def mark_complete(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('main.tasks'))

@main_blueprint.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    form = UpdateForm(content=task.content)

    if form.validate_on_submit():
        task.content = form.content.data
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.tasks'))

    return render_template('main/update_task.html', form=form, task=task)

@main_blueprint.route('/clear_list')
@login_required
def clear_list():
    completed_tasks = Task.query.filter_by(completed=True).all()
    for task in completed_tasks:
        db.session.delete(task)
    db.session.commit()
    return  redirect(url_for('main.tasks'))