from flask import Flask,request,render_template


obj=Flask(__name__)



@obj.route('/')
def welcome():
    return "Welcome the Flask"

@obj.route('/cal',methods = ["GET"])
def math_operator():
    number

print(__name__)

if __name__== '__main__':
    obj.run()