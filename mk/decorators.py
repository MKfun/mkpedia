from flask import *

def admin_only(func):
    def wrapper(*args, **kwargs):
        if not g.user or not g.user.admin:
            return render_template("not_admin.html")

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper

def user_only(func):
    def wrapper(*args, **kwargs):
        if not 'user' in g:
            return render_template("not_admin.html")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper

def root_only(func):
    def wrapper(*args, **kwargs):
        if not 'user' in g or not g.user.username == "root":
            return render_template("not_admin.html")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper

def unauthorized_only(func):
    def wrapper(*args, **kwargs):
        if 'user' in g:
            return render_template("error.html", error="Доступно только неавторизированным пользователям.")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper
