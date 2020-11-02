"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)

from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ Homepage route"""
    return render_template('homepage.html')

# Replace this with routes and view functions!


@app.route('/movies')
def all_movies():
    """View all movies"""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show movie details"""
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def all_users():
    """View all users"""
    users = crud.get_user_email()
    return render_template('all_users.html', users=users)


@app.route('/users/<user_id>')
def display_user_email(user_id):
    """Return user's email by id"""
    user = crud.get_user_id(user_id)
    return render_template('user_details.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form['email']
    password = request.form['password']
    user = crud.get_user_by_email(email)

    if user:
        flash('Email already exists.')
    else:
        crud.create_user(email, password)
        flash('Account created successfully')
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=5002)
