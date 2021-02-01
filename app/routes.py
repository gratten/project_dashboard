from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import AddProjectForm, AddMachineForm, AddKitForm
from app.models import Project, Machine, Kit

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
    return render_template('project.html', project=project, machines=machines, kits=kits)

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

@app.route('/add_machine/<jobnum>', methods=['GET', 'POST'])
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

@app.route('/add_kit/<jobnum>', methods=['GET', 'POST'])
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

