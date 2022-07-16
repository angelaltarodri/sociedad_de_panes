from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app.models.subcomment import Subcomment

@app.route("/create/subcomment", methods=['POST'])
def create_subcomment():
    if 'user_id' not in session:
        return redirect('/')

    red = "/post/panas/" + str(request.form["post_id"])

    if not Subcomment.valida_subcomentario(request.form):
        return redirect(red)

    Subcomment.save(request.form) 
    
    return redirect(red)

@app.route("/delete/subcomment/<int:post_id>/<int:subcomment_id>")
def delete_subcomment(post_id, subcomment_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": subcomment_id
    }

    red = "/post/panas/" + str(post_id)

    Subcomment.delete_subcomment_by_subcomment_id(data)
    
    return redirect(red)