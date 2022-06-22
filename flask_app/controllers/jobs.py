from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.job import Job
from flask_app.models.user import User


@app.route('/new/job')
def new_job():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_job.html', user=User.get_id(data))






@app.route('/update/job',methods=['POST'])
def update_job():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Job.validate_job(request.form):
        return redirect('/new/job')
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "location": request.form["location"],
        "created_at": request.form["created_at"],
        "updated_at": request.form["updated_at"],
        "id": request.form['id']
    }
    Job.update(data)
    return redirect('/dashboard')



@app.route('/create/job',methods=['POST'])
def create_job():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Job.validate_job(request.form):
        return redirect('/new/job')
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "location": request.form["location"],
        "created_at": request.form["created_at"],
        "user_id": session["user_id"]
    }
    Job.save(data)
    print("hmmmm")
    return redirect('/dashboard')


@app.route('/edit/account/<int:id>')
def edit_account(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    return render_template("user_account.html", job=Job.get_job_user(data),user=User.get_id(data))









@app.route('/destroy/job/<int:id>')
def destroy_job(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Job.destroy(data)
    return redirect('/dashboard')