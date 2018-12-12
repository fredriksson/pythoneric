# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy()


class USER_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    user_password = db.Column(db.String(150), unique=False, nullable=False)
    group_id = db.Column(db.String(20),unique=False, nullable=False)

class USER_GROUP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=False, nullable=False)


class IMAGE_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_uuid = db.Column(db.String(150), unique=False, nullable=False)
    img_description = db.Column(db.String(50), unique=False, nullable=False)
    img_album = db.Column(db.String(150), unique=False, nullable=False)


class IMAGE_ALBUM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(100), unique=False, nullable=False)
    album_description = db.Column(db.String(100), unique=False, nullable=False)



