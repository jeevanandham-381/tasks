from flask import Flask,request
app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    fname=request.form['fname']
    lname=request.form['lname']

    if fname == fname:
        return "Welcome %s" % fname
@app.route('/details',methods=['POST'])
def details():
    fname = request.form['fname']
    lname = request.form['lname']
    if fname==fname:
        return "Welcome %s " %fname


if __name__ == '__main__':
    app.run(debug=True)
