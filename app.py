import pytz
import os
from flask import render_template, url_for, request, redirect, flash
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_login import UserMixin
from sqlalchemy import or_, and_
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:amnay.mou2002@localhost/Dorm'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'amnaytrk@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpti cqjl wrgw llno'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'amnaytrk@gmail.com'

mail = Mail(app)


# ---------------------user-DB---------------------------------------------------
class User(db.Model, UserMixin):
    iduser = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.Column(db.String(350), nullable=False, unique=True)
    email = db.Column(db.String(150), default='null@null')
    role = db.Column(db.Integer, default=1)
    password = db.Column(db.String(450), nullable=False)
    nationality = db.Column(db.String(155), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(45), default='not define')
    birthday = db.Column(db.Date)
    major = db.Column(db.String(90), default='not define')
    date_created = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Shanghai')))
    roomnum = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.iduser

    def get_id(self):
        return str(self.iduser)
# ---------------------------------------------------------------------------


# ---------------------payment-DB---------------------------------------------------
class Payment(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    service = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Shanghai')), nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    cardnum = db.Column(db.BigInteger, nullable=False)
    cardtype = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Payment %r>' % self.id

    def get_id(self):
        return str(self.id)  # userid
# ---------------------------------------------------------------------------


# ---------------------room-DB---------------------------------------------------
class Rooms(db.Model, UserMixin):
    romnum = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    type = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    status2 = db.Column(db.String(45), nullable=False)
    username = db.Column(db.String(100), nullable=True, unique=True)

    def __repr__(self):
        return '<Room %r>' % self.romnum

    def get_id(self):
        return str(self.romnum)
# ---------------------------------------------------------------------------


# ---------------------Message-DB---------------------------------------------------
class Messages(db.Model, UserMixin):
    idmssg = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userid = db.Column(db.Integer, nullable=False)
    problem = db.Column(db.String(150), nullable=False)
    message = db.Column(db.String(800), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Shanghai')), nullable=False)
    emergency = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Messages %r>' % self.idmssg

    def get_id(self):
        return str(self.idmssg)
# ---------------------------------------------------------------------------


# ---------------------Message-DB---------------------------------------------------
class Usermessage(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(80), nullable=False)
    problem = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(700), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Shanghai')), nullable=False)

    def __repr__(self):
        return '<Usermessage %r>' % self.id

    def get_id(self):
        return str(self.id)
# ---------------------------------------------------------------------------


# ---------------------Contact_User---------------------------------------------------
class Contactuser(db.Model, UserMixin):
    idcnt = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    message = db.Column(db.String(500), nullable=False)
    idusr = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Shanghai')), nullable=False)
    userid = db.Column(db.Integer)
    userreply = db.Column(db.String(500))

    def __repr__(self):
        return '<contactuser %r>' % self.idcnt

    def get_id(self):
        return str(self.idcnt)
# ---------------------------------------------------------------------------


# ---------------------Event--------------------------------------------------- # 00000087
class Event(db.Model, UserMixin):
    idevent = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(200))
    eventdetails = db.Column(db.String(800))
    picture = db.Column(db.String(150))

    def __repr__(self):
        return '<Event %r>' % self.idevent

    def get_id(self):
        return str(self.idevent)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
# ---------------------------------------------------------------------------


# ---------------------Pass Forget----------------------------------------USER---
@app.route('/forgetpassword', methods=['GET'])
def pass_forget():
    query = request.args.get('query')
    search_attempted = False
    if query:
        search_attempted = True
        user = User.query.filter_by(email=query).first()
        if user:
            send_reset_email(user.email)
            return render_template('forget.html', tasks=[user], search_attempted=search_attempted)
    return render_template('forget.html', tasks=[], search_attempted=search_attempted)


def send_reset_email(user_email):
    query = request.args.get('query')
    user = User.query.filter_by(email=query).first()
    msg = Message('Password Reset Request', sender=app.config['MAIL_DEFAULT_SENDER'])
    msg.recipients = [user_email]

    msg.html = f"""
        <p><img src="cid:logo" alt="Reset Password Image"></p>
        <p></p>
        <p>Hello,</p>
        <p>Do you want to reset your password for your account in SDX?</p>
        <p>http://127.0.0.1:5000/resetpassword/{user.iduser}</p>
        
    """

    with app.open_resource("static/img/logo1.png") as img_file:
        img_data = img_file.read()
        msg.attach("logo3.png", "image/png", img_data, "inline", headers=[('Content-ID', '<logo>')])

    try:
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
# -----------------------------------------------------------------------------


# --------------------------------- Update Password --------------------------------------
@app.route('/resetpassword/<int:idusr>', methods=['POST', 'GET'])
def password(idusr):
    passw = User.query.get_or_404(idusr)
    if request.method == 'POST':
        if request.method == 'POST':
            hashed_password = bcrypt.generate_password_hash(request.form['password'])
            passw.password = hashed_password
        try:
            db.session.commit()
            return redirect('/login')
        except:
            return 'Dear User, There was an issue updating Password'
    else:
        return render_template('updatepassword.html', tst=passw)
# ----------------------------------------------------------------------------------------


# ---------------------------------Payment--------------------------------------
@app.route('/payment', methods=['POST', 'GET'])
@login_required
def pay():
    existing_payment = Payment.query.filter_by(userid=current_user.iduser).first()
    if existing_payment:
        old = Payment.query.order_by(Payment.date).all()
        username = current_user.username
        id = current_user.iduser
        return render_template('payinfo.html', old=old, username=username, id=id)
    else:
        return redirect(url_for('InfoPay'))
# ----------------------------------------------------------------------------------------


# --------------------------------------Add payment-------------------------------USER--
@app.route('/addpayment', methods=['POST', 'GET'])
@login_required
def AddPay():
    if request.method == 'POST':
        task_service = request.form['service']
        task_amount = request.form['amount']
        task_userid = request.form['userid']
        task_cardtype = request.form['cardtype']
        task_cardnum = request.form['cardnum']
        new_task = Payment(service=task_service, amount=task_amount, userid=task_userid, cardtype=task_cardtype,
                           cardnum=task_cardnum)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/payment')
        except Exception as e:
            db.session.rollback()
            print(f'Error adding payment: {str(e)}')
            return 'There was an issue adding your payment'
    else:
        pays = Payment.query.order_by(Payment.date).all()
        username = current_user.username
        id = current_user.iduser
        return render_template('pay.html', pays=pays, username=username, id=id)
# ----------------------------------------------------------------------------------------


# --------------------------------------Info payment-------------------------------USER--
@app.route('/infopay')
@login_required
def InfoPay():
    pays = Payment.query.order_by(Payment.date).all()
    username = current_user.username
    id = current_user.iduser
    return render_template('pay.html', pays=pays, username=username, id=id)
# ----------------------------------------------------------------------------------------


# --------------------------------------Delete payment-------------------------------USER--
@app.route('/deletepy/<int:id>')
def DeletePay(id):
    task_to_delete = Payment.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/payment')
    except:
        return 'There was a problem deleting that payment'
# ----------------------------------------------------------------------------------------


# ---------------------contact users----------------------------------------ADMIN---
@app.route('/contactuser/<int:idusr>', methods=['GET', 'POST'])
@login_required
def Contact_User(idusr):
    if request.method == 'POST':
        task_message = request.form['message']
        task_idusr = idusr
        new_message = Contactuser(message=task_message, idusr=task_idusr)
        try:
            db.session.add(new_message)
            db.session.commit()
            return redirect(f'/info/{idusr}')
        except Exception as e:
            print(e)
            return 'There was an issue replaying the user ( ' + str(e) + ')'
    else:
        mssg = User.query.filter_by(iduser=idusr).first()
        return render_template('contactuser.html', mssg=mssg)
# -----------------------------------------------------------------------------


# --------------------------- Delete admin message Reply ----------------------
@app.route('/dltmssgAD_USR/<int:idcnt>')
def deleteContactuserMessageAd(idcnt):
    DltMessage = Contactuser.query.get_or_404(idcnt)
    try:
        db.session.delete(DltMessage)
        db.session.commit()
        return redirect('/messageuser')
    except:
        return 'There was an issue deleting the user message'


# ---------------------Reply Admin----------------------------------------USER---
@app.route('/contactAd/<int:idmssg>', methods=['GET', 'POST'])
@login_required
def Contact_Admin(idmssg):
    mssg = Contactuser.query.filter_by(idcnt=idmssg).first()
    if request.method == 'POST':
        task_reply = request.form['userreply']

        mssg.userreply = task_reply
        mssg.userid = 9
        try:
            db.session.commit()
            return redirect('/messageuser')
        except Exception as e:
            print(e)
            return 'There was an issue replaying the admin (' + str(e) + ')'
    else:
        return render_template('contactad.html', mssg=mssg)
# -----------------------------------------------------------------------------


# ---------------------Search users----------------------------------------ADMIN---
@app.route('/searchuser', methods=['GET'])
def search_username_in_users():
    query = request.args.get('query')
    if query:
        tasks = User.query.filter_by(username=query).all()
    else:
        tasks = User.query.order_by(User.date_created).all()
    return render_template('users.html', tasks=tasks)
# -----------------------------------------------------------------------------


# ---------------------Search payment----------------------------------------ADMIN---
@app.route('/searchpay', methods=['GET'])
def search_username_in_pay():
    query = request.args.get('query')
    if query:
        Pay = Payment.query.filter_by(service=query).all()
    else:
        Pay = Payment.query.order_by(Payment.date).all()
    return render_template('adpayment.html', Pay=Pay)
# -----------------------------------------------------------------------------


# ---------------------Search message----------------------------------------ADMIN---
@app.route('/searchmssg', methods=['GET'])
def search_username_in_mssg():
    query = request.args.get('query')
    if query:
        show2 = Messages.query.filter_by(problem=query).all()
    else:
        show2 = Messages.query.order_by(Messages.date).all()

    if query:
        show1 = Usermessage.query.filter_by(problem=query).all()
    else:
        show1 = Usermessage.query.order_by(Usermessage.date).all()
    return render_template('showmssgs.html', show2=show2, show1=show1)
# -----------------------------------------------------------------------------


# ---------------------Show All User------------------------------------ADMIN---
@app.route('/alluser', methods=['POST', 'GET'])
def index():
    tasks = User.query.order_by(User.date_created).all()
    return render_template('users.html', tasks=tasks)
# -----------------------------------------------------------------------------


# --------------------- Event list ------------------------------------ADMIN---

@app.route('/eventcontrol', methods=['POST', 'GET'])
def eventcontrol():
    event = Event.query.order_by(Event.idevent).all()
    return render_template('eventlist.html', evnt=event)
# -----------------------------------------------------------------------------


# --------------------- Event Configue ------------------------------------ADMIN---
app.config['UPLOAD_FOLDER'] = r'C:\Users\amnay\PycharmProjects\Project\static\img\event'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
# -----------------------------------------------------------------------------


@app.route('/addevent', methods=['POST', 'GET'])
@login_required
def addevent():
    if request.method == 'POST':
        t_title = request.form['title']
        t_eventdetails = request.form['eventdetails']
        t_file = request.files['picture']

        if t_file and allowed_file(t_file.filename):
            filename = secure_filename(t_file.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            db_path = os.path.join('img/event/', filename)

            try:
                t_file.save(full_path)
                new_event = Event(title=t_title, eventdetails=t_eventdetails, picture=db_path)
                db.session.add(new_event)
                db.session.commit()
                return redirect('/eventcontrol')
            except Exception as e:
                return f'There was an issue adding the new event: {str(e)}'
        else:
            return 'Invalid file type or no file uploaded'

    events = Event.query.order_by(Event.idevent).all()
    return render_template('addevent.html', events=events)
# -----------------------------------------------------------------------------


# --------------------- Delete Event ------------------------------------ADMIN---
@app.route('/deletevent/<int:id>', methods=['POST', 'GET'])
def eventupdate(id):
    Dltevent = Event.query.get_or_404(id)
    try:
        db.session.delete(Dltevent)
        db.session.commit()
        return redirect('/eventcontrol')
    except:
        return 'There was an issue deleting the Event'
# -----------------------------------------------------------------------------


# --------------------- Update Event ------------------------------------ADMIN---
@app.route('/eventupdate/<int:id>', methods=['POST', 'GET'])
def deletevent(id):
    evt = Event.query.get_or_404(id)
    if request.method == 'POST':
        evt.title = request.form['title']
        evt.eventdetails = request.form['eventdetails']
        t_file = request.files['picture']

        if t_file and allowed_file(t_file.filename):
            filename = secure_filename(t_file.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            db_path = os.path.join('img/event/', filename)
        evt.picture = db_path
        try:
            t_file.save(full_path)
            db.session.commit()
            return redirect('/eventcontrol')
        except:
            return 'Dear User, There was an issue updating details of the selected Event'
    else:
        return render_template('updateevent.html', evt=evt)
# -----------------------------------------------------------------------------


# ---------------------Search event----------------------------------------ADMIN---
@app.route('/searchevent', methods=['GET'])
def search_Event():
    query = request.args.get('query')
    if query:
        evt = Event.query.filter_by(title=query).all()
    else:
        evt = Event.query.order_by(Event.idevent).all()
    return render_template('eventlist.html', evnt=evt)
# -----------------------------------------------------------------------------


# ----------------------REGISTER--------------------------------
@app.route('/register', methods=['POST', 'GET'])
def register():
    error_message = None
    if request.method == 'POST':
        task_email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        task_gender = request.form['gender']
        task_username = request.form['username']
        task_birthday = request.form['birthday']
        task_age = request.form['age']
        task_nationality = request.form['nationality']
        task_major = request.form['major']
        task_rmtype = request.form['room_type']
        if task_rmtype == 'single':
            task_roomnum = request.form['roomnum_single']
        elif task_rmtype == 'double':
            task_roomnum = request.form['roomnum_double']
        else:
            return 'Please select a room'
        existing_user = User.query.filter_by(username=task_username).first()
        if existing_user:
            error_message = "Username is already in use."
            return render_template('register.html', error_message=error_message)

        new_user = User(username=task_username, password=hashed_password, nationality=task_nationality,
                        gender=task_gender, age=task_age, birthday=task_birthday, email=task_email, major=task_major,
                        roomnum=task_roomnum)
        room_to_update = Rooms.query.filter_by(romnum=task_roomnum).first()

        if room_to_update:
            print(f"done{task_roomnum}")
            room_to_update.username = task_username
            if task_rmtype == 'single':
                room_to_update.status = 'dval' if room_to_update.status == 'val' else 'val'
            elif task_rmtype == 'double':
                if room_to_update.status == 'val':
                    room_to_update.status = 'dval'
                elif room_to_update.status == 'dval' and room_to_update.status2 == 'val':
                    room_to_update.status2 = 'dval'
        else:
            print(f"error{task_roomnum}")
            return 'Room not found'
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return 'There was an issue adding your task'
    else:
        def get_available_rooms():
            Single_Rooms = Rooms.query.filter_by(type='single', status='val').all()
            Double_Rooms = Rooms.query.filter(
                or_(
                    and_(Rooms.type == 'double', Rooms.status == 'val', Rooms.status2 == 'val'),
                    and_(Rooms.type == 'double', Rooms.status == 'val', Rooms.status2 == 'dval'),
                    and_(Rooms.type == 'double', Rooms.status == 'dval', Rooms.status2 == 'val'),
                    and_(Rooms.type == 'double', Rooms.status == 'dval', Rooms.status2 == 'val')
                )
            ).all()
            return Single_Rooms, Double_Rooms
        single_rooms, double_rooms = get_available_rooms()
        single_room_numbers = [room_instance.romnum for room_instance in single_rooms]
        double_room_numbers = [room_instance.romnum for room_instance in double_rooms]
        return render_template('register.html', srn=single_room_numbers, drn=double_room_numbers)
# --------------------------------------------------------------


# --------------------------LOGIN-------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    info = None
    error = None
    events = Event.query.all()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            if user.role == 0:  # Check if the user is an admin
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('After intro.html', error=error)
    return render_template('After intro.html', events=events)
# -----------------------------------------------------------------------------------------


#  --------------------------- Dashboard / Logout ----------------------------------------------USER--
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    info = None
    error = None
    username = current_user.username
    gender = current_user.gender
    DateCreate = current_user.date_created
    return render_template('studx.html', username=username, date_created=DateCreate, gender=gender)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    info = None
    error = None
    info = "successful Logout"
    events = Event.query.all()
    logout_user()
    return render_template('After intro.html', info=info, events=events)
# ---------------------------------------------------------------------------------------------------


#  --------------------------- ADMIN -------------------------------------------------------
@app.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    id = current_user.iduser
    username = current_user.username
    DateCreate = current_user.date_created
    infomssg = Contactuser.query.filter_by(userid=current_user.iduser).all()
    numssg = len(infomssg)
    return render_template('adminmenu.html', username=username, date_created=DateCreate, id=id, numssg=numssg)
#  -----------------------------------------------------------------------------------------


#  --------------------------- ADMIN 'Show all payment'---------------------------------------
@app.route('/adpayments', methods=['GET', 'POST'])
@login_required
def AllPayment():
    Pay = Payment.query.order_by(Payment.date).all()

    return render_template('adpayment.html', Pay=Pay)
#  -------------------------------------------------------------------------------------------


#  --------------------------- ADMIN 'Show all payment'---------------------------------------
@app.route('/UserPayments', methods=['GET', 'POST'])
@login_required
def AllPaymentuser():
    Pay = Payment.query.order_by(Payment.date).all()

    return render_template('userpayment.html', Pay=Pay)
#  -------------------------------------------------------------------------------------------


#  --------------------------- ADMIN 'Delete payment'------------------------------------------
@app.route('/deletead/<int:id>')
@login_required
def DeletePayAd(id):
    task_to_delete = Payment.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/adpayments')
    except:
        return 'Dear Admin, There was a problem deleting that payment'
#  -----------------------------------------------------------------------------------------


#  --------------------------- 'Update payment' ---------------------USER---------------
@app.route('/updatpayUser/<int:id>', methods=['GET', 'POST'])
@login_required
def UpdatePayUsr(id):
    task = Payment.query.get_or_404(id)

    if request.method == 'POST':
        task.service = request.form['service']
        task.amount = request.form['amount']
        task.cardtype = request.form['cardtype']
        task.cardnum = request.form['cardnum']
        try:
            db.session.commit()
            return redirect('/payment')
        except:
            return 'Dear User, There was an issue updating details of the selected payment'
    else:
        return render_template('updatepay.html', task=task)
#  ------------------------------------------------------------------------------------------


#  --------------------------- 'Update payment' ---------------------Admin---------------
@app.route('/updatpayAdmin/<int:id>', methods=['GET', 'POST'])
@login_required
def UpdatePayAd(id):
    task = Payment.query.get_or_404(id)

    if request.method == 'POST':
        task.id = request.form['id']
        task.service = request.form['service']
        task.amount = request.form['amount']
        task.userid = request.form['userid']
        task.cardtype = request.form['cardtype']
        task.cardnum = request.form['cardnum']  # here
        try:
            db.session.commit()
            if current_user.iduser == 9:
                return redirect('/adpayments')
            else:
                return redirect('/payment')
        except:
            return 'Dear Admin, There was an issue updating details of the selected payment'
    else:
        return render_template('adupdatepay.html', task=task)
#  ------------------------------------------------------------------------------------------


#  -------------- ERROR ------------------------------
@app.route('/baseinfo')
def error():
    return render_template('404.html')
#  ---------------------------------------------------


#  --------------------------------- DELETE  -------------------------------ADMIN--
@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/alluser')
    except:
        return 'There was a problem deleting that User selected'
#  -----------------------------------------------------------------------------------------


#  --------------------------------- UPDATE User -------------------------------ADMIN--
@app.route('/updateuserad/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = User.query.get_or_404(id)
    room = Rooms.query.order_by(Rooms.type)
    if request.method == 'POST':
        old_room_num = task.roomnum
        task.username = request.form['username']
        task.gender = request.form['gender']
        task.birthday = request.form['birthday']
        task.major = request.form['major']
        task.age = request.form['age']
        task.iduser = request.form['iduser']
        room_type = request.form['room_type']
        task.nationality = request.form['nationality']
        if room_type == 'single':
            task_roomnum = request.form['roomnum_single']
        elif room_type == 'double':
            task_roomnum = request.form['roomnum_double']
        else:
            return 'Please select a room'
        if old_room_num and old_room_num != task_roomnum:
            old_room = Rooms.query.filter_by(romnum=old_room_num).first()
            if old_room:
                if old_room.type == 'single':
                    old_room.status = 'val'
                    old_room.username = ''
                elif old_room.type == 'double':
                    if old_room.status == 'dval' and old_room.status2 == 'dval':
                        old_room.status = 'val'
                        old_room.username = ''
                    elif old_room.status == 'dval' and old_room.status2 == 'val':
                        old_room.status = 'val'
                        old_room.username = ''
                    elif old_room.status == 'val' and old_room.status2 == 'dval':
                        old_room.status2 = 'val'
                        old_room.username = ''
        room_to_updateUser = User.query.filter_by(username=task.username).first()
        room_to_update = Rooms.query.filter_by(romnum=task_roomnum).first()

        # room database
        if room_to_update:
            print(f"done{task_roomnum}")
            room_to_update.username = task.username
            room_to_updateUser.roomnum = task_roomnum
            room_to_updateUser.type = room_type

            if room_type == 'single':
                room_to_update.status = 'dval' if room_to_update.status == 'val' else 'val'

            elif room_type == 'double':
                if room_to_update.status == 'val':
                    room_to_update.status = 'dval'
                elif room_to_update.status == 'dval' and room_to_update.status2 == 'val':
                    room_to_update.status2 = 'dval'
        else:
            print(f"error{task_roomnum}")
        try:
            db.session.commit()
            if current_user.iduser == 9:
                return redirect('/alluser')
            else:
                return redirect('/persinfo')

        except Exception as e:
            print(f"There was an issue updating account details: {str(e)}")
            return 'There was an issue updating account details'

    else:
        def get_available_rooms():
            Single_Rooms = Rooms.query.filter_by(type='single', status='val').all()
            Double_Rooms = Rooms.query.filter(
                or_(
                    and_(Rooms.type == 'double', Rooms.status == 'val', Rooms.status2 == 'val'),
                    and_(Rooms.type == 'double', Rooms.status == 'val', Rooms.status2 == 'dval'),
                    and_(Rooms.type == 'double', Rooms.status == 'dval', Rooms.status2 == 'val'),
                    and_(Rooms.type == 'double', Rooms.status == 'dval', Rooms.status2 == 'val')
                )
            ).all()
            return Single_Rooms, Double_Rooms

        single_rooms, double_rooms = get_available_rooms()
        single_room_numbers = [room_instance.romnum for room_instance in single_rooms]
        double_room_numbers = [room_instance.romnum for room_instance in double_rooms]
        return render_template('update.html', task=task, srn=single_room_numbers, drn=double_room_numbers, rm=room)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- User Info -------------------------------USER--
@app.route('/persinfo', methods=['GET', 'POST'])
@login_required
def personalInfo():
    payment_count = 0
    numssg = 0
    pays = Payment.query.order_by(Payment.date).all()
    for payment in pays:
        if payment.userid == current_user.iduser:
            payment_count += 1
    info = User.query.filter_by(iduser=current_user.iduser).first()
    num = Rooms.query.filter_by(username=current_user.username).first()
    infomssg = Contactuser.query.filter_by(idusr=current_user.iduser).all()
    numssg = len(infomssg)
    return render_template('perinfo.html', info=info, pay=payment_count, num=num, numssg=numssg)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- Message To The User ---------------------------USER--
@app.route('/messageuser', methods=['GET', 'POST'])
@login_required
def MessageTouser():
    numssg = 0
    infomssg = Contactuser.query.filter_by(idusr=current_user.iduser).all()
    numssg = len(infomssg)  # Count the number of messages for the current user
    return render_template('messageuser.html', info=infomssg, numssg=numssg)
#  ----------------------------------------------------------------------------------------


#  --------------------------------- Message To The Admin --------------------------Admin--
@app.route('/messageadmin', methods=['GET', 'POST'])
@login_required
def MessageToAdmin():
    numssg = 0
    infomssg = Contactuser.query.filter_by(userid=current_user.iduser).all()
    numssg = len(infomssg)
    return render_template('replyuser.html', reply=infomssg, numssg=numssg)
#  ----------------------------------------------------------------------------------------


# --------------------------- Delete ----------------------
@app.route('/dllt/<int:idcnt>')
@login_required
def dllt(idcnt):
    DltMessage = Contactuser.query.get_or_404(idcnt)
    try:
        db.session.delete(DltMessage)
        db.session.commit()
        return redirect('/messageadmin')
    except:
        return 'There was an issue deleting the user message'
#  ------------------------------------------------------------


# -------------------------- Reply --------------------------
@app.route('/reply/<int:idmssg>', methods=['GET', 'POST'])
@login_required
def reply(idmssg):
    mssg = Contactuser.query.filter_by(idcnt=idmssg).first()
    if request.method == 'POST':
        task_reply = request.form['userreply']

        mssg.userreply = task_reply
        mssg.userid = 9
        try:
            db.session.commit()
            if current_user == 9:
                return redirect('/messageadmin')
            else:
                return redirect('/messageuser')
        except Exception as e:
            print(e)
            return 'There was an issue replaying the User (' + str(e) + ')'
    else:
        return render_template('contactad.html', mssg=mssg)

# -----------------------------------------------------------


# ---------------------------- Search reply -------------------------------
@app.route('/seachreply', methods=['GET'])
def dd():
    query = request.args.get('query')
    if query:
        reply = Contactuser.query.filter_by(message=query).all()
    else:
        reply = Contactuser.query.order_by(Contactuser.date).all()
    return render_template('replyuser.html', reply=reply)


#  --------------------------------- All Messages -----------------------------------ADMIN--
@app.route('/showmessages', methods=['POST', 'GET'])
def MssgAd():
    show1 = Usermessage.query.order_by(Usermessage.date).all()
    show2 = Messages.query.order_by(Messages.date).all()
    return render_template('showmssgs.html', show1=show1, show2=show2)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- User Info/Delete/update -------------------------------ADMIN--------
@app.route('/info/<int:iduser>')
@login_required
def InfoPersonal(iduser):
    task_to_info = User.query.get_or_404(iduser)
    payment_count = 0
    pays = Payment.query.order_by(Payment.date).all()
    for payment in pays:
        if payment.userid == Messages.userid:
            payment_count += 1
    info = User.query.filter_by(iduser=iduser).first()
    num = Rooms.query.filter_by(username=User.username).first()
    return render_template('perinfoad.html', info=info, pay=payment_count, num=num, task_to_info=task_to_info)


@app.route('/dlte/<int:idmssg>')
def deleteMessageAd(idmssg):
    task_to_Message = Messages.query.get_or_404(idmssg)
    try:
        db.session.delete(task_to_Message)
        db.session.commit()
        return redirect('/showmessages')
    except:
        return 'There was a problem deleting the message selected'


@app.route('/updateadmssg/<int:idmssg>', methods=['GET', 'POST'])
def UpdateMssgAd(idmssg):
    mssg = Messages.query.get_or_404(idmssg)
    if request.method == 'POST':
        mssg.idmssg = request.form['idmssg']
        mssg.userid = request.form['userid']
        mssg.problem = request.form['problem']
        mssg.message = request.form['message']
        mssg.date = request.form['date']
        mssg.emergency = bool(request.form.get('emergency', False))
        try:
            db.session.commit()
            return redirect('/showmessages')
        except:
            return 'Dear Admin, There was an issue updating The Message'
    else:
        return render_template('updatemssg.html', mssg=mssg)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- User Delete/update -------------------------------ADMIN--------
@app.route('/dltedfltmssg/<int:id>')
def AdDeleteMessage(id):
    task_to_Usermessage = Usermessage.query.get_or_404(id)
    try:
        db.session.delete(task_to_Usermessage)
        db.session.commit()
        return redirect('/showmessages')
    except:
        return 'There was a problem deleting the message selected'


@app.route('/dfltmssgupdatead/<int:id>', methods=['GET', 'POST'])
def MssgUpdateAd(id):
    dfltmssg = Usermessage.query.get_or_404(id)
    if request.method == 'POST':
        dfltmssg.email = request.form['email']
        dfltmssg.problem = request.form['problem']
        dfltmssg.message = request.form['message']
        dfltmssg.date = request.form['date']
        try:
            db.session.commit()
            return redirect('/showmessages')
        except:
            return 'Dear Admin, There was an issue updating The Message'
    else:
        return render_template('updatedfltmssg.html', dfltmssg=dfltmssg)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- Loby send message -------------------------------USER--
@app.route('/Message', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        task_email = request.form['email']
        task_problem = request.form['problem']
        task_message = request.form['message']
        new_message = Usermessage(problem=task_problem, message=task_message, email=task_email)
        try:
            db.session.add(new_message)
            db.session.commit()
            return redirect('/Message')
        except Exception as e:
            print(e)
            return 'There was an issue sending your message: ' + str(e)
    else:
        return render_template('contctus.html')

#  -----------------------------------------------------------------------------------------


#  --------------------------------- Loby send message -------------------------------USER--
@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    return render_template('wechat.html')
#  -----------------------------------------------------------------------------------------


#  --------------------------------- User send message -------------------------------USER--
@app.route('/ctctus', methods=['GET', 'POST'])
@login_required
def contactususer():
    if request.method == 'POST':
        problem = request.form['problem']
        message = request.form['message']
        emergency = bool(request.form.get('emergency', False))
        userid = current_user.iduser
        new_message = Messages(userid=userid, problem=problem, message=message, emergency=emergency)
        try:
            db.session.add(new_message)
            db.session.commit()
            return redirect('/ctctus')
        except Exception as e:
            print(e)
            return 'There was an issue sending your message: ' + str(e)
    else:
        user = current_user.username
        return render_template('contctuslogin.html', user=user)
#  -----------------------------------------------------------------------------------------


#  --------------------------------- Room ----------------------------------------TRAINING--
@app.route('/room', methods=['GET', 'POST'])
def ValRoom():
    def get_available_rooms():
        SingleRooms = Rooms.query.filter_by(type='single', status='val').all()
        DoubleRooms = Rooms.query.filter_by(type='double', status='val', status2='val').all()
        return SingleRooms, DoubleRooms
    single_rooms, double_rooms = get_available_rooms()
    single_room_numbers = [room_instance.romnum for room_instance in single_rooms]
    double_room_numbers = [room_instance.romnum for room_instance in double_rooms]
    return render_template('valromms.html', srn=single_room_numbers, drn=double_room_numbers)
#  -----------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)
