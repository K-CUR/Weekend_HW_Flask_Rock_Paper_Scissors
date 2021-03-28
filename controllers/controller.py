from app import app

from flask import render_template

from models.game import Game

from models.game_objs import who_wins

from models.player import Player

# COMMENT: proves html can be rendered to page and player choices can be seen in terminal...
# @app.route('/<player1_choice>/<player2_choice>')
# def game(player1_choice, player2_choice):
#     print(player1_choice)
#     print(player2_choice)
#     return render_template('base.html')

# COMMENT: returns player choices but not result...
# @app.route('/<player1_choice>/<player2_choice>')
# def game(player1_choice, player2_choice):
#     return render_template('base.html', player1_choice = player1_choice, player2_choice = player2_choice)

# COMMENT: returns player choices AND result...
@app.route('/<player1_choice>/<player2_choice>')
def game(player1_choice, player2_choice):
    result = who_wins(player1_choice, player2_choice)
    return render_template('base.html', title = "Game", player1_choice = player1_choice, player2_choice = player2_choice, result = result)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title = "How to")



