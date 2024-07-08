from flask import *
from src.dbconnection import *
app=Flask(__name__)
app.secret_key='123'
import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('login_index.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



@app.route("/")
def log():
    return render_template("login_index.html")

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
        session['lid']=res['lid']
        return redirect("/adminhome")
    elif res['type']=='hospital':
        session['lid']=res['lid']

        return redirect("/hospitalhome")
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''

@app.route('/addandmanagepumb_and_workshop',methods=['get','post'])
@login_required
def addandmanagepumb_and_workshop():
    q = "SELECT * FROM `workshop/pump`"
    r = selectall(q)
    return render_template("Add&manage Pump.html",val=r)

# @app.route('/addandmanageworkshop',methods=['get','post'])
# def addandmanageworkshop():
#     q="SELECT * FROM `workshop/pump`where type='workshop'"
#     r=selectall(q)
#     return render_template("Add&Manage Workshop.html",val=r)

@app.route('/addpumporworkshop',methods=['get','post'])
@login_required
def addpumporworkshop():
    return render_template("Add Pump or Workshop.html")

@app.route('/addpumporworkshop1',methods=['get','post'])
@login_required
def addpumporworkshop1():
    name=request.form["textfield"]
    place=request.form["textfield2"]
    phone=request.form["textfield3"]
    lattitude=request.form["textfield4"]
    longitude=request.form["textfield5"]
    status=request.form["textfield6"]
    type=request.form["select"]
    qry="insert into `workshop/pump` values(null,%s,%s,%s,%s,%s,%s,%s)"
    val=(name,place,phone,lattitude,longitude,status,type)
    iud(qry,val)
    return '''<script>alert("Workshop or Pump Added"); window.location="/addandmanagepumb_and_workshop"</script>'''


@app.route('/editpumporworkshop1',methods=['get','post'])
@login_required
def editpumporworkshop1():
    id=request.args.get('id')
    session['id']=id
    qry="SELECT * FROM `workshop/pump` where id=%s"
    res=selectone(qry,id)
    return render_template("editpump.html",val=res)

@app.route('/editpumporworkshop',methods=['get','post'])
@login_required
def editpumporworkshop():
    name=request.form["textfield"]
    place=request.form["textfield2"]
    phone=request.form["textfield3"]
    lattitude=request.form["textfield4"]
    longitude=request.form["textfield5"]
    status=request.form["textfield6"]
    type=request.form["select"]
    qry="UPDATE `workshop/pump` SET `name`=%s,`place`=%s,`phone`=%s,`latitude`=%s,`longitude`=%s,`status`=%s,`type`=%s WHERE `id`=%s"
    val=(name,place,phone,lattitude,longitude,status,type,str(session['id']))
    iud(qry,val)
    return '''<script>alert("Workshop or Pump Added"); window.location="/addandmanagepumb_and_workshop"</script>'''








@app.route('/deletepumporworkshop1',methods=['get','post'])
@login_required
def deletepumporworkshop1():
    id=request.args.get('id')
    q="DELETE FROM `workshop/pump` WHERE id=%s"
    iud(q,id)
    return '''<script>alert("Successfully Deleted"); window.location="/addandmanagepumb_and_workshop"</script>'''
@app.route('/blockuser',methods=['get','post'])
@login_required
def blockuser():
    qry = "SELECT `user`.*,`login`.* FROM `user` JOIN `login` ON `user`.`lid`=`login`.`lid`"
    res = selectall(qry)
    return render_template("blockuser.html",val=res)
@app.route('/blockusers',methods=['post','get'])
@login_required
def blockusers():
    id=request.args.get('id')
    qry="update login set type='block' where lid=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("Successfully blocked"); window.location="/blockuser"</script>'''


@app.route('/unblockusers', methods=['post', 'get'])
@login_required
def unblockusers():
    id = request.args.get('id')
    qry = "update login set type='user' where lid=%s"
    val = (str(id))
    iud(qry, val)
    return '''<script>alert("Successfully unblocked"); window.location="/blockuser"</script>'''





@app.route('/hospitalregister',methods=['get','post'])

def hospitalregister():
    return render_template("regindex.html")
@app.route('/hospital_register',methods=['post'])

def hospital_register():
    hname = request.form["textfield"]
    pname = request.form["textarea"]
    post = request.form["textfield2"]
    pin = request.form["textfield3"]
    phone = request.form["textfield24"]
    email = request.form["textfield5"]
   # phone1=987654321
    lt = request.form["textfield10"]
    lnt = request.form["textfield11"]

    username = request.form["textfield6"]
    password = request.form["textfield7"]
    qry = "insert into login values(null,%s,%s,'pending')"
    val = (username,password)
    id = iud(qry,val)
    qry1 = "insert into hospital values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id),hname,pname,pin,post,phone,email,lt,lnt)
    iud(qry1,val1)
    return '''<script>alert('hospital registered ');window.location="/"</script>'''



@app.route('/managepumporworkshop',methods=['get','post'])
@login_required
def managepumporworkshop():
    return render_template("Manage Pump or Workshop.html")
@app.route('/userregister',methods=['get','post'])

def userregister():
    return render_template("User Register.html")


@app.route('/verifyambulance',methods=['get','post'])
@login_required
def verifyambulance():
    qry="SELECT `ambulance`.*,`login`.*FROM`ambulance` JOIN `login`ON`ambulance`.lid=`login`.lid"
    res=selectall(qry)
    return render_template("Verify Ambulance.html",val=res)



@app.route('/verifyhospital',methods=['get','post'])
@login_required
def verifyhospital():
    qry = "SELECT `hospital`.*,`login`.* FROM `hospital` JOIN `login`ON `hospital`.`lid`=`login`.`lid`"
    res = selectall(qry)

    return render_template("Verify hospital.html",val=res)




@app.route('/viewdetails',methods=['get','post'])
@login_required
def viewdetails():
    qry="SELECT * FROM `notification`"
    res=selectall(qry)
    return render_template("View Details.html",val=res)




@app.route('/viewreport',methods=['get','post'])
@login_required
def viewreport():
    qry = "SELECT * FROM `report`JOIN `ambulance`ON `ambulance`.`lid`=`report`.`amb_id` JOIN `user`ON `user`.`lid`=`report`.`uid`"
    res=selectall(qry)
    return render_template("view report.html",val=res)


@app.route('/viewdetails1',methods=['get','post'])
@login_required
def viewdetails1():
    date=request.form['textfield']
    qry="SELECT * FROM `request` JOIN `user`ON `request`.`uid`=`user`.`lid` WHERE request.`date`=%s"
    res=selectall2(qry,date)
    return render_template("View Details.html",date=res)
@app.route('/adminhome',methods=['get','post'])
@login_required
def adminhome():
    return render_template("admin_index.html")

@app.route('/hospitalhome',methods=['get','post'])
@login_required
def hospitalhome():
    return render_template("Hospital Home.html")

#@app.route('/viewdetails',methods=['get','post'])
#def viewdetails():
 #   return render_template("View Details.html")

@app.route('/hospitalviewnotification',methods=['get','post'])
@login_required
def hospitalviewnotification():
    # qry = "SELECT `ambulance`.dname,`ambulance`.Anumber,`ambulance`.phone,`notification`.notification,`location`.latitude,`location`.longitude FROM `ambulance` JOIN `notification` ON `ambulance`.lid=`notification`.aid JOIN `location` ON `ambulance`.lid=`location`.aid"
    # res = selectall(qry)
    qry="SELECT * FROM `hospital_notification` JOIN `ambulance` ON `hospital_notification`.`aid`=`ambulance`.`lid` JOIN `location`ON `location`.`aid`=`ambulance`.`lid` WHERE `hospital_notification`.date = CURDATE() "
    res=selectall(qry)
    return render_template("Hospital View Notification.html",val=res)












@app.route('/AD_verify',methods=['get','post'])
@login_required
def AD_verify():
    id=request.args.get('id')
    qry="update login set type='Ambulance' where lid=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("verified");window.location="verifyambulance"</script>'''

@app.route('/AD_Rej',methods=['get','post'])
@login_required
def AD_Rej():
    id=request.args.get('id')
    qry="update login set type='Rejected' where lid=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Rejected");window.location="verifyambulance"</script>'''


@app.route('/hs_verify',methods=['get','post'])
@login_required
def hs_verify():
    id=request.args.get('id')
    qry="update login set type='hospital' where lid=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("verified");window.location="verifyhospital"</script>'''

@app.route('/hs_rej',methods=['get','post'])
@login_required
def hs_rej():
    id=request.args.get('id')
    qry="update login set type='Rejected' where lid=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Rejected");window.location="verifyhospital"</script>'''






app.run(debug=True)