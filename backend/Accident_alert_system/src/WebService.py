import cmd

from flask import *
from src.dbconnection import *
app=Flask(__name__)
import functools
@app.route('/login',methods=['POST'])
def login():

    username=request.form['uname']
    password=request.form['password']

    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)

    if res is None:
        return jsonify({'task':'invalid'})

    else:
        id= res['lid']
        return jsonify({'task':'success','lid':id,'type':res['type']})
@app.route('/userregister',methods=['post'])
def userregister():
    fname=request.form['fname']
    lname=request.form['lname']
    place=request.form['place']
    phone=request.form['phone']
    email=request.form['email']
    username = request.form['username']
    password = request.form['password']
    qry = "insert into login values(null,%s,%s,'user')"
    val = (username, password)
    id = iud(qry, val)
    qry1 = "insert into user values(null,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id),fname,lname,place,phone,email)
    iud(qry1, val1)
    return jsonify({'task': 'valid'})


@app.route('/cancelnotification',methods=['POST'])
def cancelnotification():
    id=request.form['id']

    qry="DELETE FROM `notification` WHERE `id`=%s"
    iud(qry,id)
    return jsonify({'task': 'valid'})

@app.route('/send_notification',methods=['POST'])
def send_notification():
    print(request.form)

    aid=request.form['lid']
    notification=request.form['notification']
    qry="INSERT INTO `hos_notification` VALUES(NULL,%s,'0',CURDATE(),CURTIME(),%s)"

    val1 = (aid,notification)
    iud(qry,val1)
    return jsonify({'task': 'valid'})


@app.route('/setemergencynumber',methods=['POST'])
def setemergencynumber():

    uid=request.form['lid']
    number=request.form['number']
    qry = "INSERT INTO `emergency_no` VALUES(NULL,%s,%s)"
    val=(uid,number)
    iud(qry,val)
    return jsonify({'task': 'valid'})

@app.route('/viewemergencynumber',methods=['POST'])
def viewemergencynumber():
    uid = request.form['lid']
    qry = "SELECT * FROM emergency_no where uid=%s"
    res = selectall2(qry,uid)
    print(res)
    return jsonify(res)


@app.route('/deleteem',methods=['POST'])
def deleteem():
    uid = request.form['eid']
    qry = "DELETE  FROM emergency_no where id=%s"
    iud(qry,uid)
    return jsonify({'task': 'valid'})


@app.route('/reportaccident',methods=['POST'])
def reportaccident():
    uid = request.form['uid']
    aid = request.form['aid']####nearest ambulance
    q="insert  into `request` values(null,%s,%s,'null','lati','longi','pending',curdate(),curtime())"
    v=(uid,aid)
    iud(q,v)
    return jsonify({"task":"valid"})

@app.route('/reportstatus', methods=['POST'])
def reportstatus():
    print(request.form)
    uid = request.form['lid']
    q="select  `request`.*,`ambulance`.`Anumber`,`ambulance`.`dname`,`ambulance`.`phone` from `ambulance` join `request` on `request`.`aid`=`ambulance`.`lid`  where request.uid=%s"
    res=selectall2(q,uid)
    print(res)
    return  jsonify(res)





@app.route('/report',methods=['POST'])
def report():
    message=request.form['message']
    uid=request.form['uid']
    amb_id=request.form['amb_id']
    qry = "INSERT INTO `report` VALUES(NULL,%s,%s,%s,CURDATE(),'pending')"
    val=(message,amb_id,uid)
    iud(qry,val)
    return jsonify({'task': 'valid'})


# @app.route('/reportstatus',method=['POST'])
# def report():
#     qry = "SELECT`request`. *,`user`.`fname`,`lname`FROM request JOIN `user` ON request.uid=`user`.uid"
#     res = selectall(qry)
#     return jsonify(res)



@app.route('/ambulanceregister',methods=['POST'])
def ambulanceregister():
    Anumber=request.form['Anumber']
    dname=request.form['dname']
    phone=request.form['phone']
    email=request.form['email']
    place=request.form['place']
    username = request.form['username']
    password = request.form['password']
    qry = "insert into login values(null,%s,%s,'pending')"
    val = (username, password)
    id = iud(qry, val)
    qry1 = "insert into ambulance values(null,%s,%s,%s,%s,%s,%s,'pending')"
    val1 = (str(id),Anumber,dname,phone,email,place)
    iud(qry1, val1)
    return jsonify({'task': 'valid'})


@app.route('/updatestatus',methods=['POST'])
def updatestatus():
    lid=request.form['lid']
    status=request.form['status']
    qry = "UPDATE ambulance SET status=%s WHERE lid=%s"
    val = (status,lid)
    iud(qry, val)
    return jsonify({'task': 'valid'})

@app.route('/viewrequest',methods=['POST'])
def viewrequest():
    print(request.form)
    lattitude = request.form['lati']
    longitude = request.form['longi']
    qry="SELECT `user`.`fname`,`lname`,phone,`request`.* , (3959 * ACOS ( COS ( RADIANS('"+lattitude+"') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('"+longitude+"') ) + SIN ( RADIANS('"+lattitude+"') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `request` JOIN `user` ON `request`.`uid`=`user`.`lid` HAVING user_distance  < 31.068"
    res = selectall(qry)
    print("===",res)
    return jsonify(res)





@app.route('/acceptrequest',methods=['POST'])
def acceptrequest():
    lid=request.form['rid']
    rid=request.form['lid']

    qry = "UPDATE request SET aid=%s,status='accepted' WHERE rid=%s"
    iud(qry,(rid,lid))
    return jsonify({'task': 'valid'})



@app.route('/rejectrequest',methods=['POST'])
def rejectrequest():
    lid=request.form['rid']
    rid=request.form['lid']

    qry = "UPDATE request SET aid=%s,status='rejected' WHERE rid=%s"
    iud(qry,(rid,lid))
    return jsonify({'task': 'valid'})


@app.route('/viewnearestworkshop',methods=['POST'])
def viewnearestworkshop():
    print(request.form,"==================================")
    latitude = request.form['lattitude']
    longitude = request.form['longitude']
    print(latitude,longitude,"==============================")
    qry="SELECT `workshop/pump`.*, (3959 * ACOS ( COS ( RADIANS(%s) ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS(%s) ) + SIN ( RADIANS(%s) ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `workshop/pump` HAVING user_distance  < 31.068 and type='workshop'"
    val=(latitude,longitude,latitude)
    res=selectall2(qry,val)
    print(res,"********************************")
    return jsonify(res)

@app.route('/viewnearestpump',methods=['POST'])
def viewnearestpump():
    latitude = request.form['lattitude']
    longitude = request.form['longitude']
    print(latitude,longitude)
    qry="SELECT `workshop/pump`.*, (3959 * ACOS ( COS ( RADIANS(%s) ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS(%s) ) + SIN ( RADIANS(%s) ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `workshop/pump` HAVING user_distance  < 31.068 and type='pump'"
    val=(latitude,longitude,latitude)
    s=selectall2(qry,val)
    return jsonify(s)

@app.route('/selectnearesthospital', methods=['POST'])
def selectnearesthospital():
    print(request.form)
    latitude = request.form['lati']
    longitude = request.form['logi']
    print(latitude)
    res = selectall("SELECT hospital.*, (3959 * ACOS ( COS ( RADIANS('" + latitude + "') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('" + longitude + "') ) + SIN ( RADIANS('" + latitude + "') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `hospital` HAVING user_distance  < 31.068")
    print(res)
    return jsonify(res)

@app.route('/trackreq',methods=['POST'])
def trackreq():
    lid = request.form['lid']
    qry="SELECT * FROM `request`  JOIN `user`ON `user`.`lid`=`request`.`uid`  WHERE  `request`.`status`='accepted'  and request.aid=%s"
    res=selectall2(qry,lid)
    return jsonify(res)


@app.route('/LOCATION',methods=['post'])
def LOCATION():
    print(request.form)
    lid=request.form['lid']
    tid=request.form['latitude']
    com=request.form['longitude']

    qry = "SELECT * FROM `location` WHERE `aid`=%s"
    res = selectone(qry,lid)

    if res is None:

        qry="INSERT INTO  `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,com,tid)
        iud(qry,val)
        return jsonify({'task': 'success'})
    else:
        qry = "UPDATE `location` SET `longitude`=%s,`latitude`=%s WHERE `aid`=%s"
        val = (com, tid, lid)
        iud(qry, val)
        return jsonify({'task': 'success'})


@app.route('/viewnearestambulance',methods=['POST'])
def viewnearestambulance():
    print(request.form)
    lid=request.form['lid']
    lattitude=request.form['lattitude']
    longitude=request.form['longitude']
    print(lattitude,longitude,"===========================")
    qry="SELECT `ambulance`.*,location.* , (3959 * ACOS ( COS ( RADIANS('"+lattitude+"') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('"+longitude+"') ) + SIN ( RADIANS('"+lattitude+"') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `ambulance` JOIN location ON ambulance.lid=location.aid  HAVING user_distance  < 31.068 and ambulance.status='active' "
    res=selectall(qry)
    print(res)
    qry1 = "SELECT `ambulance`.*,location.* , (3959 * ACOS ( COS ( RADIANS('" + lattitude + "') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('" + longitude + "') ) + SIN ( RADIANS('" + lattitude + "') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `ambulance` JOIN location ON ambulance.lid=location.aid where ambulance.lid not in (select aid from request where status = 'accepted')  HAVING user_distance  < 31.068 and ambulance.status='active' LIMIT 1 "
    res1 = selectone1(qry1)
    print(res1,"eeeeeeeeeeeeeeeeeee")

    iud("INSERT INTO `request` (`uid`,`aid`,`latitude`,`longitude`,`status`,`date`,`time`) VALUES(%s,%s,%s,%s,'pending',CURDATE(),CURTIME())",(lid,'0',lattitude,longitude))
    return jsonify(res)






@app.route('/addlocation', methods=['post'])
def addlocation():
    lid=request.form['lid']
    lat=request.form['lat']
    lon=request.form['lon']
    qry="SELECT * FROM `location` WHERE `aid`=%s"
    res=selectone(qry,lid)
    print(res)
    if res is None:
        qry="INSERT INTO `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,lat,lon)
        iud(qry,val)
    else:
        qry="UPDATE `location` SET `latitude`=%s,`longitude`=%s WHERE `aid`=%s"
        val=(lat,lon,lid)
        iud(qry,val)
    return jsonify({'task': 'valid'})



@app.route('/Emergency_message', methods=['post'])
def Emergency_message():
    print(request.form)
    try:
        uid=request.form['uid']
        lati=request.form['latitude']
        longi=request.form['longitude']
        if lati=='':
            lati = "11.344556"
            longi = "75.3456"

        qry = "SELECT * FROM `notification` WHERE `uid`=%s"
        res = selectone(qry, uid)
        print(res)
        if res is None:
            qry = "INSERT INTO `notification` VALUES(NULL,%s,CURDATE(),curtime(),%s,%s,'pending')"
            val = (uid, lati, longi)
            iud(qry, val)
        else:
            qry = "UPDATE `notification` SET `latitude`=%s,`longitude`=%s WHERE `uid`=%s"
            val = (lati, longi, uid)
            iud(qry, val)

        res = selectall2("SELECT * FROM `emergency_no` WHERE `uid`=%s",uid)

        # qry = "SELECT `ambulance`.*,location.* , (3959 * ACOS ( COS ( RADIANS('" + lattitude + "') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('" + longitude + "') ) + SIN ( RADIANS('" + lattitude + "') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `ambulance` JOIN location ON ambulance.lid=location.aid  HAVING user_distance  < 31.068 and ambulance.status='active' "
        # res = selectall(qry)
        print(res)
        print("=========================+++++++++++++++++++")
        qry1 = "SELECT `ambulance`.*,location.* , (3959 * ACOS ( COS ( RADIANS('" + lati + "') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('" + longi + "') ) + SIN ( RADIANS('" + lati + "') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `ambulance` JOIN location ON ambulance.lid=location.aid where ambulance.lid not in (select aid from request where status = 'accepted') and ambulance.status='active' having user_distance<30 order by  user_distance LIMIT 1 "
        res1 = selectone1(qry1)
        print(res1, "eeeeeeeeeeeeeeeeeee")
        try:
            qry = "INSERT INTO `request` VALUES(NULL,%s,'0',%s,%s,'pending',CURDATE(),CURTIME())"
            iud(qry,(uid,lati,longi))
        except:
            pass
        num=""
        for i in res:
            num+=str(i['number'])+"pp"
            print (i['number'],"==========")
        return jsonify(task="success",pp=num)
            # return jsonify(task="success",pp=i['number'])
    except Exception as e:
        print(e,"pppppppppppppppppppppppppppppppppppppppppppppp")
        return jsonify(task="success", pp="7902248441")







@app.route('/Request_ambulance', methods=['post'])
def Request_ambulance():
    uid = request.form['uid']
    aid = request.form['aid']  ####nearest ambulance
    q = "insert  into `request` values(null,%s,%s,'null','lati','longi','pending',curdate(),curtime())"
    v = (uid, aid)
    iud(q, v)
    return jsonify({"task": "valid"})


@app.route('/sendhosptlreq', methods=['post'])
def sendhosptlreq():
    uid = request.form['hid']
    aid = request.form['aid']
    iud("INSERT INTO `hospital_notification` VALUES(null,%s,%s,'emergency',curdate())",(aid,uid))
    return jsonify({"task": "success"})


app.run(host='0.0.0.0',port=5000)