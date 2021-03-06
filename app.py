from project import create_app
#from project.models import User
#from project import db

app = create_app()


#@app.shell_context_processor
#def make_shell_context():
    #return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run()