from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app.models.subcomment import Subcomment

@app.route("/create/comment", methods=['POST'])
def create_comment():
    if 'user_id' not in session:
        return redirect('/')

    #el "panas" vendria a ser reemplazado por %(category)s
    red = "/post/panas/" + str(request.form["post_id"])

    if not Comment.valida_comentario(request.form):
        return redirect(red)

    Comment.save(request.form)
    
    return redirect(red)

@app.route("/delete/comment/<int:post_id>/<int:comment_id>")
def delete_comment(post_id, comment_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": comment_id,
        "comment_id": comment_id
    }

    red = "/post/panas/" + str(post_id)

    Comment.delete_comment_by_comment_id(data)
    Subcomment.delete_subcomments_by_comment_id(data)
    
    return redirect(red)