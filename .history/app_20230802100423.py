from flask import Flask, request,render_template






app=Flask(__name__)



@app.route('/')
def welcome():
    return "Welcome the Flask"

if __name__== ''
app.run()