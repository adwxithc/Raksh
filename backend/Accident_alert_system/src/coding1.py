from flask import *
from src.dbconnection import *
app=Flask(__name__)



@app.route("/")
def log():
    return render_template("login.html")
@app.route('/login',methods=['get','post'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif res['type']=="admin":
        return redirect("/adminhome")
    elif res['type']=='hospital':
        return redirect("/hospitalhome")
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''

@app.route('/addandmanagepumb',methods=['get','post'])
def addandmanagepumb():
    return render_template("Add&manage Pump.html")
@app.route('/addandmanageworkshop',methods=['get','post'])
def addandmanageworkshop():
    return render_template("Add&Manage Workshop.html")
@app.route('/addpumporworkshop',methods=['get','post'])
def addpumporworkshop():
    return render_template("Add Pump or Workshop.html")








@app.route('/hospitalregister',methods=['get','post'])
def hospitalregister():
    return render_template("Hospital Register.html")
@app.route('/hospital_register',methods=['post'])
def hospital_register():
    hname = request.form["textfield"]
    pname = request.form["textarea"]
    post = request.form["textfield2"]
    pin = request.form["textfield3"]
    phone = request.form["textfield4"]
    email = request.form["textfield5"]
    lt = request.form["textfield10"]

    lnt = request.form["textfield11"]

    username = request.form["textfield6"]
    password = request.form["textfield7"]
    qry = "insert into login values(null,%s,%s,'pending')"
    val = (username,password)
    id = iud(qry,val)
    qry1 = "insert into hospital values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id),hname,post,pname,pin,phone,email,lt,lnt)
    iud(qry1,val1)
    return '''<script>alert("hospital registered");window.location="/"</script>'''


@app.route('/managepumporworkshop',methods=['get','post'])
def managepumporworkshop():
    return render_template("Manage Pump or Workshop.html")
@app.route('/userregister',methods=['get','post'])
def userregister():
    return render_template("User Register.html")


@app.route('/verifyambulance',methods=['get','post'])
def verifyambulance():
    qry="SELECT * FROM `ambulance`"
    res=selectall(qry)
    return render_template("Verify Ambulance.html",val=res)



@app.route('/verifyhospital',methods=['get','post'])
def verifyhospital():
    qry = "SELECT * FROM `ambulance`"
    res = selectall(qry)

    return render_template("Verify hospital.html",val=res)


@app.route('/adminviewnotification',methods=['get','post'])
def adminviewnotification():
    return render_template("Admin View Notification.html")
@app.route('/adminhome',methods=['get','post'])
def adminhome():
    return render_template("Admin Home.html")
@app.route('/hospitalhome',methods=['get','post'])
def hospitalhome():
    return render_template("Hospital Home.html")
@app.route('/viewdetails',methods=['get','post'])
def viewdetails():
    return render_template("View Details.html")
@app.route('/hospitalviewnotification',methods=['get','post'])
def hospitalviewnotification():
    return render_template("Hospital View Notification.html")





app.run(debug=True)