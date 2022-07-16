from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.reaction_has_post import Reaction_has_post
from flask_app.models.reaction_has_comment import Reaction_has_comment

@app.route("/post/add/reaction/<int:post_id>/<int:reaction_id>")
def new_post_reaction(post_id, reaction_id):

    if 'user_id' not in session:
        return redirect('/')

    red = "/post/panas/" + str(post_id)
    
    data = {
        "user_id": session['user_id'],
        "post_id": post_id,
        "reaction_id": reaction_id,
    }
    
    Reaction_has_post.save(data)

    return redirect(red)

@app.route("/post/quit/reaction/<int:post_id>/<int:reaction_id>")
def quit_post_reaction(post_id, reaction_id):

    if 'user_id' not in session:
        return redirect('/')

    red = "/post/panas/" + str(post_id)
    
    data = {
        "user_id": session['user_id'],
        "post_id": post_id,
        "reaction_id": reaction_id,
    }
    
    Reaction_has_post.quit(data)

    return redirect(red)

@app.route("/comment/add/reaction/<int:post_id>/<int:comment_id>/<int:reaction_id>")
def new_comment_reaction(post_id, comment_id, reaction_id):

    if 'user_id' not in session:
        return redirect('/')

    red = "/post/panas/" + str(post_id)
    
    data = {
        "user_id": session['user_id'],
        "comment_id": comment_id,
        "reaction_id": reaction_id,
    }
    Reaction_has_comment.save(data)

    return redirect(red)

@app.route("/comment/quit/reaction/<int:post_id>/<int:comment_id>/<int:reaction_id>")
def quit_comment_reaction(post_id, comment_id, reaction_id):

    if 'user_id' not in session:
        return redirect('/')

    red = "/post/panas/" + str(post_id)
    
    data = {
        "user_id": session['user_id'],
        "comment_id": comment_id,
        "reaction_id": reaction_id,
    }
    
    Reaction_has_comment.quit(data)

    return redirect(red)
