from flask import Flask,request,render_template


obj=Flask(__name__)



@app.route('/')
def welcome():
    return "Welcome the Flask"

@obj

print(__name__)

if __name__== '__main__':
    app.run()