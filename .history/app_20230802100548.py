from flask import Flask, request,render_template


app=Flask(__name__)



@app.route('/')
def welcome():
    return "Welcome the Flask"

print(__name__)

if __name__== '__main__':
    
    app.run()