from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from scrap import scrape_site
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 3 is relative, 4 is abs path
db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.id)


@app.route('/', methods=['POST', 'GET'])
def home():
    # src, parser = scrape_site(URL)
    # return str(src)
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = ToDo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
        except:
            return 'ERROR: Failed Adding the Task'
        return redirect('/')
    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html', tasks = tasks )

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e :
        return 'ERROR: There was a problem deleting task with id:{}\n\t{}'.format(id,e)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task_to_update = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['content']
        try:
            db.session.commit()
            return  redirect('/')
        except Exception as e :
            return 'Failed to update {} \n\tERROR:{}'.format(task_to_update,e)
    else:
        return render_template('update.html', task = task_to_update)
    #
    # try:
    #     db.session.delete(task_to_update)
    #     db.session.commit()
    #     return redirect('/')
    # except Exception as e :
    #     return 'ERROR: There was a problem updating task with id:{}\n\t{}'.format(id,e)

if __name__ == '__main__':
    URL = 'https://ryan47liao.github.io/Ryan-Portfolio/'
    app.run(debug=True)
