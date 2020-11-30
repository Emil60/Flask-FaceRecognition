import os
from flskfaceapp import app, db
from flask import render_template, flash, redirect, url_for, abort, request
from flskfaceapp.models import Images, User
from flskfaceapp.forms import imageForm


#APP_IMAGES = os.path.join( 'images/')



@app.route('/', methods=['GET','POST'])
def index():
    form=imageForm()
    if form.validate_on_submit():
        
        if form.photo.data:
            pht = form.photo.data
            temp_data = pht.read()
            os.walk('./flskfaceapp/temp')
            temp_file = open('./flskfaceapp/temp/temp.jpg','wb+')
            temp_file.write(temp_data)
            temp_file.close()
        
            from flskfaceapp import face_rec
            name = face_rec.classify_face('./flskfaceapp/temp/temp.jpg')
        else:
            from flskfaceapp import face_rec
            name = face_rec.classify_face_with_cam()
        print("done")
        checker = name
        if name != "Unknown":
            uname = User.query.filter_by(user_id = checker).first()
            flash(f'salam {uname.name}')
        else:
            flash('dayan goreh')



    return render_template('index.html',form=form)
