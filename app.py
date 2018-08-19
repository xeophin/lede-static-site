from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://km@localhost/esc'
db = SQLAlchemy(app)


class Contests(db.Model):
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  id = db.Column(db.String, primary_key=True)
  
class Finalists(db.Model):
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  id = db.Column(db.String, primary_key=True)
  contest_id = db.Column(db.String, db.ForeignKey('contests.id'))





@app.route("/")
def index():
  contests = Contests.query.all()
  return render_template('list.html', contests=contests)


# @app.route('/search')
# def search():
#   schools = School.query.filter(School.school_name.contains('henry')).all()
#   return render_template('list.html', schools=schools)
# 

@app.route('/contest/<id>/')
def contest(id):
  contest = Contests.query.filter_by(id=id).first()
  finalists = Finalists.query.filter_by(contest_id=id).order_by(
    Finalists.ranking).all()
  return render_template('show.html', contest=contest, finalists=finalists)


if __name__ == '__main__':
  app.run(debug=True)
