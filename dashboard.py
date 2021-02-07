from app import create_app, db
from app.models import Project, Machine, Kit, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Project': Project, 'Machine': Machine, 'Kit': Kit, 'Task':Task}