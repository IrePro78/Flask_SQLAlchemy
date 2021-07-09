from flask import render_template






def login():
    return render_template('header.html')


def register():
    return render_template('index.html')