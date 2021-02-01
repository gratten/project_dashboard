from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobnum = db.Column(db.String(12))
    # customer = db.Column(db.String(64))exit()
    ec_date = db.Column(db.String(12))
    engineer = db.Column(db.String(24))
    machines = db.relationship('Machine', backref='job', lazy='dynamic')
    kits = db.relationship('Kit', backref='job', lazy='dynamic')


    def __repr__(self):
        return f'<Project {self.jobnum}>'

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # jobnum = db.Column(db.String(8), index=True)
    # prodline = db.Column(db.String(64))
    serialnum = db.Column(db.String(64), index=True, unique=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    # kits = db.relationship('Kit', backref='parent', lazy='dynamic')

    def __repr__(self):
        return f'<Machine {self.serialnum}>'

class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # project = db.Column(db.String(8), index=True)
    # serialnum = db.Column(db.Integer, db.ForeignKey('machine.serialnum'))
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    speed = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return f'<Kit {self.length}x{self.width}x{self.depth}>'