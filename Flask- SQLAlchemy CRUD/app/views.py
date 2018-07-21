from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import Note

# 노트 생성
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        note = Note(request.form['title'], request.form['content'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/')
def index():
    note = Note.query.all()
    return render_template('index.html', note=note)

# 노트 수정
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    note = Note.query.get(id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)

# 노트 삭제
@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('index'))