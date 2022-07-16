from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app.models.subcomment import Subcomment
from flask_app.models.reaction_has_post import Reaction_has_post
from flask_app.models.reaction_has_comment import Reaction_has_comment

@app.route("/new/post")
def new_recipe():

    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    return render_template('new_post.html', user= user)

@app.route("/create/post", methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/')

    if not Post.valida_publicacion(request.form):
        return redirect('/new/post')

    Post.save(request.form)

    data = {
        "id": session['user_id'],
        "category_id": request.form['category_id']
    }

    print(Post.assign_category_to_post(data))

    return redirect("/dashboard")

@app.route("/all/post/panas")
def all_post_panas():
    if 'user_id' not in session:
        return redirect('/')


    data = {
        "id": session['user_id']
    }

    data_admin = {
        "id": "4"
    }
    
    posts_panas = Post.get_posts_data_for_page(data_admin)

    return render_template('avisos_panas.html', posts_panas=posts_panas)

@app.route("/post/panas/<int:id>") 
def aviso_pana(id):

    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }
    user = User.get_by_id(data)

    data_post = {
        "post_id": id
    }
    post = Post.get_post_data_for_page(data_post)

    comments = Comment.get_comments_data_for_page(data_post)

    subcomments = Subcomment.get_subcomments_data_for_page(data_post)

    reactions_post = Reaction_has_post.get_reactions_by_post(data_post)

    reactions_comments_post = Reaction_has_comment.get_reactions_by_post(data_post)

    return render_template('aviso_pana.html', user= user, post=post,comments=comments, subcomments=subcomments, reactions_post=reactions_post, reactions_comments_post=reactions_comments_post)

@app.route("/delete/post/<int:id>") 
def delete_pana(id):

    if 'user_id' not in session:
        return redirect('/')
    

    data = {
        "post_id": id,
        "user_id": session['user_id']
    }

    subcomments = Subcomment.get_all_subcomments_by_post_id(data)

    for subcomment in subcomments:
        Subcomment.delete_subcomments_by_comment_id(subcomment)

    Comment.delete_comments_by_post_id(data)
    Post.delete_post_from_categories(data)
    Post.delete_post(data)

    return redirect("/all/post/panas")