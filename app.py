from project import create_app
from project.models import User, Task
from project import db

app = create_app()
app.logger.info('Flask application instance instantiated')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Task=Task)


if __name__ == '__main__':
    app.run()