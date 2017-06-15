# -*- coding: utf-8 -*-
from project.models.model import *
from flask import render_template, request, jsonify, json, send_from_directory
from sqlalchemy import desc
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = app.root_path + '/upload_file'

@app.route('/')
def helloWorld():
    db.drop_all()
    db.create_all()
    return 'Hello world'

@app.route('/main')
def testTemplate():
    files = File.query.all()
    return render_template('mainpage/index.html', files=files )

@app.route('/api/songs', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_songs():
    added_status_flag = 'Nothing'
    if(request.method == 'GET'):
        songs = {}
        songs_in_database = Song.query.all()

        for song in songs_in_database:
            songs[song.id] = song.as_dictionary()

        return jsonify(songs)

    elif(request.method == 'POST'):
        new_file = json.loads(request.data)
        check_file = File.query.filter_by(id=new_file['file']['id']).first()

        if (check_file == None):
            write_new_file = File(new_file['file']['id'], new_file['file']['name'])
            createData(write_new_file)
            added_status_flag = 'Added song'
        else: added_status_flag = 'File exists in database'

        return added_status_flag

    elif(request.method == 'PUT'):
        edit_file = json.loads(request.data)
        check_file = File.query.filter_by(id=edit_file['file']['id']).first()

        if (check_file != None):
            check_file.filename = edit_file['file']['name']
            db.session.add(check_file)
            db.session.commit()
            added_status_flag = 'Edited song'
        else:
            added_status_flag = 'File does not exists in database'

        return added_status_flag

    elif (request.method == 'DELETE'):
        delete_file = json.loads(request.data)
        check_file = File.query.filter_by(id=delete_file['file']['id']).first()

        if (check_file != None):
            check_song = Song.query.filter_by(file_id=check_file.id).first()
            db.session.delete(check_file)
            db.session.delete(check_song)
            db.session.commit()
            added_status_flag = 'Deleted song'
        else:
            added_status_flag = 'File does not exists in database'
        return added_status_flag

@app.route('/api/songs/add', methods=['GET', 'POST'])
def add_songs():
    added_status_flag = 'Nothing happened'
    if(request.method == 'POST'):
        id = request.form['id_song']
        name = request.form['name_song']
        check_file = File.query.filter_by(id=id).first()

        if (check_file == None):
            write_new_file = File(id, name)
            createData(write_new_file)
            added_status_flag = 'Added song'
        else:
            added_status_flag = 'File exists in database'

        return added_status_flag

    return render_template('api/addsong.html')

def createData(file):
    song = Song()
    song.file = file
    db.session.add(file)
    db.session.add(song)
    db.session.commit()
    return 'Created song'

# @app.route('/api/songs/edit', methods=['GET', 'POST'])
# def edit_songs():
#     added_status_flag = 'Nothing happened'
#     if(request.method == 'POST'):
#         id = request.form['id_song']
#         name = request.form['name_song']
#         check_file = File.query.filter_by(id=id).first()
#
#         if (check_file == None):
#             write_new_file = File(id, name)
#             createData(write_new_file)
#             added_status_flag = 'Added song'
#         else:
#             added_status_flag = 'File exists in database'
#
#         return added_status_flag
#
#     return render_template('api/addsong.html')

@app.route('/api/files', methods=['GET', 'POST'])
# @decorators.require('multipart/form-data')
# @decorators.accept('application/json')
def file_post():
    if(request.method == 'POST'):
        file = request.files['fileToUpload']

        if(file!= None):
            file_name = secure_filename(file.filename)
            # file.save('E:/upload/' + file_name )
            file.save(UPLOAD_FOLDER + '/' + file_name)
            file_id = File.query.order_by(desc(File.id)).first()

            if(file_id == None):
                new_id = 1
            else:
                new_id = file_id.id + 1

            createData(File(new_id, file_name))
        else:
            return 'Cannot find file'

    return render_template('mainpage/upload.html')

@app.route('/uploads/<filename>', methods=['GET'])
def get_file(filename):
    # return send_from_directory('E:/upload', filename)
    return send_from_directory(UPLOAD_FOLDER + '/', filename)