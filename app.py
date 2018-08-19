from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://km@localhost/esc'
db = SQLAlchemy(app)


# class Finalist(db.Model):
#   __tablename__ = 'finalists'
#   __table_args__ = {
#     'autoload': True,
#     'autoload_with': db.engine
#   }
#   id = db.Column(db.String, primary_key=True)


class Contest(db.Model):
  __tablename__ = 'contests'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  id = db.Column(db.String, primary_key=True)


@app.route("/")
def hello():
  contests = Contest.query.all()
  return render_template('list.html', contests=contests)


@app.route('/contests/')
def schools():
  contests = Contest.query.all()
  return render_template('list.html', contests=contests)


# @app.route('/search')
# def search():
#   schools = School.query.filter(School.school_name.contains('henry')).all()
#   return render_template('list.html', schools=schools)
# 

# @app.route('/school/<dbn>/')
# def school(dbn):
#   school = School.query.filter_by(dbn=dbn).first()
#   return render_template('show.html', school=school)


if __name__ == '__main__':
  app.run(debug=True)
