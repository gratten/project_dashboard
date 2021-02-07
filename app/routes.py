from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import AddProjectForm, AddMachineForm, AddKitForm, AddTaskForm
from app.models import Project, Machine, Kit, Task

@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    return render_template('index.html', title='Home', projects=projects)

@app.route('/<jobnum>')
def project(jobnum):
    project = Project.query.filter_by(jobnum=jobnum).first_or_404()
    machines = project.machines.all()
    kits = project.kits.all()
    tasks = project.tasks.all()
    return render_template('project.html', project=project, machines=machines, kits=kits, tasks=tasks)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm()
    if form.validate_on_submit():
        project = Project(jobnum=form.jobnum.data,
                          ec_date=form.ec_date.data,
                          engineer=form.engineer.data)
        db.session.add(project)
        db.session.commit()
        flash('Project added')
        return redirect(url_for('index'))
    return render_template('add_project.html', form=form)

@app.route('/<jobnum>/add_machine', methods=['GET', 'POST'])
def add_machine(jobnum):
    form = AddMachineForm()
    # test = test_var
    # jobnum = 'HS5279'
    p = Project.query.filter_by(jobnum=jobnum).first_or_404()
    if form.validate_on_submit():
        machine = Machine(serialnum=form.serialnum.data,
                          job=p)
        db.session.add(machine)
        db.session.commit()
        flash('Machine added')
        return redirect('/' + jobnum)
    return render_template('add_machine.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/edit_machine/<string:id>', methods=['GET', 'POST'])
def edit_machine(jobnum, id):
    form = AddMachineForm()
    m = Machine.query.filter_by(id=id).first_or_404()

    # populate form with existing data
    form.serialnum.data = m.serialnum

    if form.validate_on_submit():
        m.serialnum = request.form['serialnum']
        db.session.commit()
        flash('Machine updated')
        return redirect('/' + jobnum)
    return render_template('edit_machine.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/delete_machine/<string:id>', methods=['POST'])
def delete_machine(jobnum, id):
    m = Machine.query.filter_by(id=id).first_or_404()
    db.session.delete(m)
    db.session.commit()
    flash('Machine deleted')
    return redirect('/' + jobnum)

@app.route('/<jobnum>/add_kit', methods=['GET', 'POST'])
def add_kit(jobnum):
    form = AddKitForm()
    p = Project.query.filter_by(jobnum=jobnum).first_or_404()
    if form.validate_on_submit():
        kit = Kit(length=form.length.data,
                  width=form.width.data,
                  depth=form.depth.data,
                  speed=form.speed.data,
                  job=p)
        db.session.add(kit)
        db.session.commit()
        flash('Kit added')
        return redirect('/' + jobnum)
    return render_template('add_kit.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/edit_kit/<string:id>', methods=['GET', 'POST'])
def edit_kit(jobnum, id):
    form = AddKitForm()
    k = Kit.query.filter_by(id=id).first_or_404()

    # populate form with existing data
    form.length.data = k.length
    form.width.data = k.width
    form.depth.data = k.depth
    form.speed.data = k.speed

    if form.validate_on_submit():
        k.length = request.form['length']
        k.width = request.form['width']
        k.depth = request.form['depth']
        k.speed = request.form['speed']
        db.session.commit()
        flash('Kit updated')
        return redirect('/' + jobnum)
    return render_template('edit_kit.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/delete_kit/<string:id>', methods=['POST'])
def delete_kit(jobnum, id):
    k = Kit.query.filter_by(id=id).first_or_404()
    db.session.delete(k)
    db.session.commit()
    flash('Kit deleted')
    return redirect('/' + jobnum)

@app.route('/<jobnum>/add_task', methods=['GET', 'POST'])
def add_task(jobnum):
    form = AddTaskForm()
    p = Project.query.filter_by(jobnum=jobnum).first_or_404()
    if form.validate_on_submit():
        task = Task(task=form.task.data,
                    engineer=form.engineer.data,
                    job=p)
        db.session.add(task)
        db.session.commit()
        flash('Task added')
        return redirect('/' + jobnum)
    return render_template('add_task.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/edit_task/<string:id>', methods=['GET', 'POST'])
def edit_task(jobnum, id):
    form = AddTaskForm()
    t = Task.query.filter_by(id=id).first_or_404()

    # populate form with existing data
    form.task.data = t.task
    form.engineer.data = t.engineer

    if form.validate_on_submit():
        t.task = request.form['task']
        t.engineer = request.form['engineer']
        db.session.commit()
        flash('Task updated')
        return redirect('/' + jobnum)
    return render_template('edit_task.html', form=form, jobnum=jobnum)

@app.route('/<jobnum>/delete_task/<string:id>', methods=['POST'])
def delete_task(jobnum, id):
    t = Task.query.filter_by(id=id).first_or_404()
    db.session.delete(t)
    db.session.commit()
    flash('Task deleted')
    return redirect('/' + jobnum)

