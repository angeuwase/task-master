from project.auth import auth_blueprint

@auth_blueprint.route('/register')
def register():
    return 'This will be a registration page'

@auth_blueprint.route('/login')
def login():
    return 'This will be a login page'