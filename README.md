**ABSTRACT:**

  The goal of Smart Dormitory X (SDX) is to make dormitory management simpler, easier, and more contemporary. One of its main objectives is to reduce the inefficiency of traditional techniques, such as manual paper lists and data collection, which hinder effective management and waste time, money, and human resources. SDX provides a user-friendly interface accessible across all devices to ensure ease of use for all students. With the “Contact Us” service, SDX aims to help users resolve any issues they may encounter. Access to the platform is login-based, allowing users to access a range of services including checking payment lists, creating new lists, accessing user information, and creating reports or requests for any service or problem. That is the usual user but if the administrative is trying to log into SDX, it should have a role in the database is 0, which allows the platform to redirect the user to the Administrative Interface, this menu allows the administration to manage all the platform for example check payment made by users, check information for every user, contact any user, answer all questions and other services. Additionally, users with administrative privileges can access an administration interface to efficiently manage all aspects of the platform. By encrypting all passwords and utilizing strong database systems, our platform places a high priority on user data security. This ensures that you will receive your request and service more quickly, as well as attend to inquiries and afford your request (fixed, repaired, and renewed). To put it briefly, Smart Dormitory X (SDX) upgrades dorm administration by streamlining procedures, guaranteeing user accessibility, and putting security first. With its intuitive UI and extensive offerings, SDX helps students be more productive and live better. SDX ensures user data security by utilizing strong database systems and encryption. Furthermore, SDX is an essential tool for improving the entire dorm experience because of its administrative skills, which allow for the effective supervision of all operations.

Keywords: Management System, Python Flask, Dormitory, MySQL, Database.

![image](https://github.com/user-attachments/assets/f91e633d-4324-4b02-a786-134a17432654) / ![image](https://github.com/user-attachments/assets/bb7bbdec-535f-4488-a09e-65c0e2a2ccf1)

**The architectural diagram:**

![image](https://github.com/user-attachments/assets/29ebf796-4e7e-498c-84a5-9ff3f78cce2b)

**E-R diagram:**

![image](https://github.com/user-attachments/assets/c66b734b-48a7-447a-b536-fa89a78dab29)

**Python**

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically typed, and garbage collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented, and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library. Python consistently ranks as one of the most popular programming languages and has gained widespread use in the machine-learning community.

**Python Flask:**

  The Model-View-Controller (MVC) framework has become the standard in modern software development, with the model layer, display layer, and controller layer making it easier and faster. The Flask is a framework that uses Python language with easy-to-understand code writing. However the Flask framework still doesn't use the MVC method, so files and codes are not regular. The purpose of this study was to design an MVC for a framework that uses the Python programming language. This system has a generator that can make MVC folder structure easily and quickly, this system is also equipped with the Bootstrap framework, and this system is open source. The results showed that the presence of MVC on the Flask framework could enable users easier in create new projects and have a faster full load time.
To ensure that the environment has a better experience using Flask and gets all the library needs I chose PyCharm, its integrated development environment used for programming in Python.
Python Flask, these frameworks offer similar functionalities and capabilities for developing web applications, providing a standardized platform for building B/S architecture software. Additionally, Python Flask is well-suited for developing web applications in Python, offering simplicity, flexibility, and scalability. Both Python Flask encompasses various features and tools to streamline development processes and meet the specific functional requirements of your project.

**SQLAlchemy:**

  Mike B. (2015), SQLAlchemy Documentation states, “The SQLAlchemy SQL Toolkit and Object Relational Mapper is a comprehensive set of tools for working with databases and Python. It has several distinct areas of functionality which can be used individually or combined.” SQLAlchemy provides a flexible and powerful toolkit for interacting with databases in Python, allowing developers to work with databases using Pythonic syntax and patterns. With SQLAlchemy, developers can create, query, and manipulate database objects using an expressive and intuitive API.

**Flask-SQLAlchemy:**

  Flask SQLAlchemy is a dynamic database toolkit tailored for Flask. It offers an intuitive interface for database operations within Flask apps, capitalizing on the capabilities of SQLAlchemy, a renowned object-relational mapping (ORM) library in Python. Object-relational mapping, commonly known as ORM, is a programming technique that seamlessly connects the dots between databases and object-oriented programming languages. Imagine a scenario where you have a table in a database, and instead of writing lengthy SQL queries to interact with it, you could treat that table just like an object in your code. That’s precisely what ORM allows you to do.

**Bcrypt:**

  Bcrypt is a hash function created by Niels Provos and David Mazières. It is based on the Blowfish encryption algorithm and was presented at USENIX in 19991. In addition to the use of salt to protect against rainbow table attacks, bcrypt is an adaptive function, that is to say, we can increase the number of iterations to make it slower. Thus, it continues to be resistant to brute force attacks despite the increase in computing power.

**MySQL:**

  MySQL is a relational database system. Many fanatical MySQL enthusiasts think that MySQL is quicker, more reliable, and cheaper than any other database system (including commercial systems like Oracle and DB2). Many MySQL opponents continue to challenge this viewpoint, going even so far as to assert that MySQL is not even a relational database system. And to make it more clear MySQL is an Oracle-backed open-source relational database management system (RDBMS) based on Structured Query Language (SQL). MySQL runs on virtually all platforms, including Linux, UNIX, and Windows. Although it can be used in a wide range of applications, MySQL is most often associated with web applications and online publishing. MySQL is an important component of an open-source enterprise stack called LAMP. LAMP is a web development platform that uses Linux as the operating system, Apache as the web server, MySQL as the relational database management system, and PHP as the object-oriented scripting language. (Sometimes Perl or Python is used instead of PHP). MySQL is Characterized by bright features (Relational Database System, Client/Server Architecture, SQL compatibility …).


**Home page:**

![image](https://github.com/user-attachments/assets/da6e95ce-818e-4d4d-aab7-93ba38897290)
![image](https://github.com/user-attachments/assets/2a0b8bca-a54b-4581-9f3a-d828aec6e8b7)

**Login error message in home page:**

![image](https://github.com/user-attachments/assets/d5d03d46-2286-4de3-b6e3-fcb9b71264a1)

**Successful logout message on the home page:**

![image](https://github.com/user-attachments/assets/7e3872e4-3c7c-489a-b581-dfcb165ac7f3)

**Registration page:**

![image](https://github.com/user-attachments/assets/b665e299-5ac3-4798-8a9f-bd1933e46ce8)
![image](https://github.com/user-attachments/assets/b66c13db-9d59-4f31-a05b-5673c9de2522)

After full all information & check i read .... the button will be Enable:

![image](https://github.com/user-attachments/assets/773996ed-fd07-4846-93e8-dfb4631adf17)

**Student Dashboard page:**

The menu of services for the student is represented in the student dashboard, after the successful login, and the system checks that the role of the user is equal to 1, the SDX redirects to: http://127.0.0.1:5000/dashboard The first part of the interface shows the username of the user and the option to logout, the logo (redirects you to the home page), and the Contact Us service.
![image](https://github.com/user-attachments/assets/d59c8792-0063-413b-9f19-fd505c6e1cb0)

![image](https://github.com/user-attachments/assets/eadaa767-0c8f-4e8a-97f4-863ac7317907)


**Profile Page & Update Page & Reply Admin Page:**

The interface of the profile shows the information for the current user (birthday, username, age, major, room type, room number …). Also, it contains a counter (number 1 in Figure 2.11) for the payment made by the current user.

![image](https://github.com/user-attachments/assets/510594b3-b990-4f58-9d08-cd87c2684266)

After Click on 'Update' Button:

![image](https://github.com/user-attachments/assets/7c853335-5dba-49f7-ba62-53eb1aa3420e)

After Click on 'Message' Button:

![image](https://github.com/user-attachments/assets/dfecc4c8-3d8d-4ef9-8837-4da272ce4182)

After Click on 'Reply' Super link:

![image](https://github.com/user-attachments/assets/a6e95adc-92ae-4305-b2fc-b380b1545573)

Profile interfaces Schema:

![image](https://github.com/user-attachments/assets/4c345804-5770-4deb-911b-a469339ad198)

**Add payment page:**

http://127.0.0.1:5000/infopay. The new payment UI is user-friendly since the user is enabled to enter the amount, and the card number, and to choose the service, and card type by a drop-down. Completion of the transaction is simply a click on the ‘Pay’ button. The interface has been created with Flask and supports GET and POST requests for the smooth processing of form submissions, with error handling done through rollback mechanisms for data integrity. Enhanced with scripts and style sheets, the HTML layout creates a neat, responsive user interface with a welcome banner and good client-side validations to ensure security. That is why this design does not just ease the whole process of payment; it is in line with all the top data protection policies.

![image](https://github.com/user-attachments/assets/796c818b-ad72-447f-98f7-5543fa66d5af)

**Payments history page:**

The payment interface for the web page, http://127.0.0.1:5000/payment , is built using Python Flask; it's simple, easy and secure. It was constructed so that it could serve GET and POST requests for viewing and manipulation payment records with help of SQLAlchemy. It was additionally built to prevent unauthorized data access by any user through the Flask @login_required decorator. The data interface greets the user by his name and lists payment history, which can be edited or deleted. Furthermore, it has an easy possibility to add a new payment by clicking the "Add New Payment" link. This is designed to be responsive, attractive to view, and uses a number of local resources as well as animate.css resources for its CSS to use the highest standards of data safety. This further improves usability and also provides safety with regard to financial data management.

![image](https://github.com/user-attachments/assets/f9b06fb1-5c6f-4f24-85e8-e06cd64f8880)

**Update payment page**

Another obvious user-centered and simple design from the SDX system is the Update Payment Web Interface. This interface allows secure and convenient updating of payment information: card number, card type, payment amount, and service type in a well-structured layout, thus ensuring simplicity and accessibility. It features clean and clear fields, big enough to view the details of the last payment. The system guarantees updated data because the backend system is seamless, and the data is updated. It includes checks for validation to avoid wrong data entry, dynamical correction of errors before form submission, and uses POST methods to assure secure data transmission.
Security and user experience are the leading priorities in the design and functionality of the interface. The system secures sensitive payment information using strong measures such as HTTPS and strict data validation, thus eliminating SQL injection, XSS, and other security vulnerabilities. In this situation, if the changes are not going through, then the user is immediately aware of it and, in turn, has a sense of reliability and trust. The HTML of the interface is formatted for accessibility, thus making screen readers perform better. There is also responsive CSS that makes this interface usable on any device. Also, the Python Flask backend handles the request and database interactions very efficiently and safely, so updating the payment is a very safe and effective process.

![image](https://github.com/user-attachments/assets/dec7359b-0a5d-4123-a9f1-3c98bdf1a08a)

**Contact administration page**

The form “Contact administration” provides a simple way the users can address their grievances. They can fill out a long note that describes their issue and, if necessary, they can specify it as an emergency. This form is submitted the moment they feed in all the necessary details and press the "Submit" button. This UI leverages the simple animations in Bootstrap.min.css and, above all, the "Submit" button remains disabled until all fields are filled in. A floating button supports navigation, it provides the ability to scroll back to the top of the page without sudden snap. A hyperlink is added in the Banner section to the home page, which is further supported by an attractive image to make the page more beautiful.

![image](https://github.com/user-attachments/assets/ea3854ad-9e39-43e0-b0fd-af2c5f56a811)

**Admin Dashboard page**

The admin menu/dashboard is one the principal interface in SDX. It backs up admin features well and with clear routes to manage users, payments, messages, and events. Security is also assured as the information is visible only to authenticated users to shield informative information. The HTML structure used Bootsrap as well as Animate.css to offer an attractive, responsive interface that morphs efficiently across devices. 
The critical elements are brought to one click with straightforward navigation and icons clearly marked increasing user engagement and efficiency. The Owl Carousel and Magnific Popup scripts add more interactivity to the Dashboard while the media queries amp a part of the design to cater for the optimal performance of the Dashboard across various environments. It is the very reason that makes the dashboard a necessary tool, ensuring that administration is well achieved in an effective and efficient.

![image](https://github.com/user-attachments/assets/23689696-47d9-41c7-a2f8-bea24a51d234)
![image](https://github.com/user-attachments/assets/c1e983d4-e56e-4d41-a204-f507975371ec)
![image](https://github.com/user-attachments/assets/273d28ee-b0da-4bb1-aa07-aaae499dbc9e)
![image](https://github.com/user-attachments/assets/7ce54acd-d799-4735-9114-701175423db3)

**Admin all users list page:**

‘All Users’ interface for easy handling of users on SDX platform. The admin can update and delete users through the flask route, http://127.0.0.1:5000/alluser , which fetches data modularly to be displayed in a table in the users.html template. The aesthetics of the user interface have been improved with an HTML setup that includes a graphic design feature. It is composed of a background image, and corresponding graphic color schemes through formatting, which helps readability. The interface has been natively made responsive to allow the user, at a glance, to search for the user. All these come together, having a back-end that processes data correctly, user interaction that is intuitive, and an interface that is visually appealing and coherent.

![image](https://github.com/user-attachments/assets/f50ad2ac-a4af-4fd8-b3bf-cd75f2590341)

**Admin all payments list page:**

The payment details list under URL: http://127.0.0.1:5000/adpayments , securely shows all payment records, thereby giving the administrators the power and capability for financial management right in this educational platform. Authenticated through Python Flask, this interface uses the adpayment.html template to list payments as per date, with other added features for updating and deleting. It has been designed with a dynamic view—made animated and fully responsive—thereby uplifting usability to the users by incorporating searchable facilities, which simply make navigation as simple as possible with the least fuss. In this way, a marriage of firm, back-end functionality with a friendly, engaging, and intuitively designed front end will give a solution functionally designed but easy to use in practice, making management of payments easier.

![image](https://github.com/user-attachments/assets/6f78d268-3483-495d-9f13-54d77caefb08)

**Admin all messages page:**

In an SDX system, the admin panel's "All Messages" tab optimally deals with user communications, aggregating data from two sources by means of Python Flask and rendering the resultant page in the showmssgs.html template. The interface will be responsive, so it can be resized, and the table will support quick filtering to get more details on messages regarding ID, user info, problem, and date. Any communication with the authorities is made aware of immediately. Flask secures the backend processes and makes them efficient. An HTML and CSS template makes it remain usable and nice-looking on every device, with an easy and seamlessly smooth process of dealing with communications for the administrator.

![image](https://github.com/user-attachments/assets/c76fe663-073a-4b5e-8b57-6a97d6ccb017)
![image](https://github.com/user-attachments/assets/2c7cdeed-ca61-45dc-8090-438e10b42a56)

**Admin all reply message page:**

Communication can be better practiced with the 'Message to the Admin' feature of an admin dashboard: An admin can see and manage messages sent by any user. Developed with Python Flask in a very secure way, this section is built on user authentication and makes use of Flask's ORM for filtering messages addressed to the currently logged in admin. In the interface made, using the template replyuser.html, we made it of a simple but very user-friendly nature. There is a search feature, so navigation and managing communication become truly a breeze. Unified table format for messages, which emphasizes content of the reply, text, and date. The table also allows for some quick options: replying to a message or deleting one. Properly, the design fits the aesthetics of the entire platform. It uses a full-background image and the same consistency of styling. But yeah, the interface should, literally, be a feast for the eyes.

![image](https://github.com/user-attachments/assets/3cfe3f99-7a0e-4d66-9c8f-67d6e2a54352)

**Admin event control:**

The events controller, done through Python Flask, remains important in handling the content relevant to events in an educational platform. This is accessed through the /eventcontrol route, using the ORM capabilities of Flask, to fetch a list of events, ordered by the IDs, from the database. Additional information in a table for each of the listed events includes the ID of the event, its title, details, and, if an image is related to the event, an associated image is shown in detail for a more advanced and engagement-inducing setting to the administrators. The design also comes with searching functionality which enables filtering of events in a more effortless way. This is in regard to the fact that it becomes easier for the administrator to edit and delete an event's entry without the need to go to the update or delete page for such a purpose. The design comes in with a stylish CSS file and a dynamic background image that makes the design of the interface as good-looking as it is functional, with a perfect harmony in the general look and feel of the back-end interface.

![image](https://github.com/user-attachments/assets/c60ebf68-8a6f-46f2-91a7-b679b291e6fc)

**Admin update user:**

The "Update User" interface in the admin dashboard is an important part of the dynamical management of user profiles—in support from Python Flask, of course. Accessed under the route /updateuserad/<int:id>, again, this will require user authentication for secure access. The back end of the route fetches user details via User.query.get_or_404(id) and available room options from Rooms in a dynamic fashion, depending on input by the user. This thereby allows the admin to change user detail such as username, room assignments, gender, and other personal details in a form of POST request—since changes happen on room occupancy and the database is updated.
Next, there is a form included with a friendly interface that selects the available room options dynamically depending on the room type chosen in the form, courtesy of JavaScript. This aides user functionality by reducing work done when choosing. This HTML layout follows mostly the general look of a base template, so the general look of the page remains consistent throughout the platform. A background image has been put in place to make the page more attractive; throughout, the CSS file linked in the block of the head is very clean and follows the general aesthetics of the site. The form is complete, and it includes all information regarding the user, and a submit function applies to the completion of updates. With this setup, both the update process of the user and practical and available interface for administrative purposes have been facilitated.

![image](https://github.com/user-attachments/assets/73c96eae-4d04-4690-a7e2-5fd6214be19f)

**Admin update payment**

The most important core functionality developed for efficient management attributes of payment, hence the admin dashboard interface, is developed with Python Flask, specifically "Update Payment". This is a secured route /updatpayAdmin/<int:id> which requires logins and ensures that only authenticated admins can access and manipulate the payment data. The form, which is furnished to the user on the adupdatepay.html template, updates major payment attributes: ID, service, amount, card type, and card number. In that connection, POST requests when submitting changes are handled by the Flask backend, hosting effective error handling so to control the database commit operation and show the proper feedback in case of failures. First and foremost, this view maintains consistency of user interface, as it is pretty much basic from a base HTML template, adds attractiveness while styled with CSS, and linked with dropdowns and input fields for efficient updates, and most of all includes the footer link to navigate back to the admin dashboard easily. This ooze implements a strong Flask back-end with a simple front end in taking the details of the payment to be managed effectively, yet keeping it intuitive and secure for the users.

![image](https://github.com/user-attachments/assets/8d74bdbe-0541-4278-adae-a3ee69fd9dd5)

**Admin Reply user**

The admin dashboard's user interface, which is the "Reply Admin", spaces communication in a way that allows the administrators to reply with no hustle to inquiries made by the user. This is a secure Python Flask application that requires user authentication. At the back end, this interface fetches one message from the table Contactuser and displays it in the form in the contactad.html template for the administrator to write and send the reply. The workflow is smooth since, upon making a POST request, the response of the administrator will be updated in the database and a redirection to the confirmation page by the user.
A simple and clean form within a neat and organized layout, which flows out from a rudimentary template, makes the application more engagingly communicative in its HTML setup. A form is used to show the original message and lets the user type the response in a textarea element, and then a submit button follows, which forwards the response. Aesthetic styling is done with CSS to drive effective user appeal and interaction, followed by a footer for easy navigation back to the main admin or user dashboard, dependent on the user's role. The interface is built super clean with basic workflow, making it ridiculously easy for an admin to get back to a user with effective communication and having full backup of powerful data handling of Flask. 

![image](https://github.com/user-attachments/assets/10c89d08-8c85-4ae1-9134-121a1b03a6d9)

**Admin add event**

The most recently added events are added through the "Add Event" on the admin dashboard in creating a simple user interface. This can be supported with Python Flask, where administrators are allowed to key in the event's title, specifics, and upload any relevant images, through a Multipart form, when events are being created. The configuration of backend Flask ensures that the uploaded images are to be stored within a particular folder. It also validates the types of files uploaded for system integrity. For successful POST requests, the details of the event are saved on the database, and, in case of an error, error handling is implemented.
The HTML structure built on top of the base template is modern and increases the amount of visual and user interaction on the web page made. Navigation is made a breeze by the intuitively laid forms where derivations are made upon addition of JavaScript enhancements that lead to ensured correct form fields before submission. It comes with Bootstrap and other libraries for CSS in order to give adaptive looks and styles while including JavaScript plug-ins for functional builds that produce an increase in the level of improvement, including form validation and dynamic UI updates. The interface combines the strong server-side capabilities of Flask and advanced frontend technologies into an effective whole, providing a highly functional, secure, and engaging user experience when managing events.

![image](https://github.com/user-attachments/assets/4c7afe80-d213-4868-828a-b313edd46729)

**Admin update event**

The "Update Event" interface is robust in allowing details of events to be manipulated using the admin dashboard. Python Flask provides the muscle in the backend. Through this feature, a further layer of security and the ability for the administrator to update the details of events is upon the administrator, who can now safely update the details of the events using a form with features to upload files provided the upload directory, and file type validation to enable storing of valid image files, is guaranteed by the Flask setup and configuration. The HTML form with features to upload files is represented in a multipart data form. The contents of the multipart data form are styled with CSS to give it a professional outlook. Truly, in the mechanics, the system directly interfaces continuously with the backing Flask provides and saves the updates into a preset directory. Documentation is not only made easier on this configuration but enriches the ability of the administrator to have information about events updated and thus dynamically situates the site tops with usability and security features.

![image](https://github.com/user-attachments/assets/ff2c282a-515d-4d12-8e07-3f896a51f2d9)

**Forget Password:**

A good example is the robust mechanism in the SDX platform password management system that allows a user to reset and update his or her password, backed up by Python Flask. This process starts when a user sends a request to reset his or her password Fig 5.35 and enters his or her email address. If there is an email which belongs to a valid user account, then the system tries to send one email having a link to reset the password Fig 5.36 by calling the function send_reset_email. This function builds an HTML email embedding an inline image and sends it to the previously configured mail server. Users will be able to receive new passwords safely on /resetpassword/<int:idusr> passing a new password that will be stored in the database in hashed form from bcrypt. The password reset and change HTML form is of simple design and styled to be user-friendly with CSS, and embedded within the template extension from a base layout in order to keep the platform uniform. This will leave not only a robust approach to handling password changes but also be made very intuitive from a user experience viewpoint, with clear ways to navigate back to the login page, covered in minimal yet effective frontend design elements.

![image](https://github.com/user-attachments/assets/635be3eb-d39d-462a-8ca8-0e8836995632)


**DATABASE**:
MySQLWorkbench interface:

![MySQLWorkbench_1TVdpqMif9](https://github.com/user-attachments/assets/43925239-dff9-4bbf-93e1-263b1b3ee3a0)

To collect informaion enter by the use to the database (MySQL) simple process:

HTML Code:
-> <div class="home-user">
     <span class="home-text">Username:</span>
     <input id="username" name="username" type="text" required="true" placeholder="User" class="home-user1 input"/>
   </div>
   <div class="home-pass">
     <span class="home-text01">Password:</span>
     <input id="password" name="password" type="password" required="true" placeholder="Password" class="home-user2 input"/>
   </div>

Python Code:
-> @app.route('/login', methods=['GET', 'POST'])
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

  The process of collecting data from an HTML interface and storing it in a MySQL database using Python Flask involves several key steps. First, the HTML form captures user input through fields like username and password, which are assigned specific name attributes. When the form is submitted, this data is sent to the server via an HTTP POST request. In the Flask application, the login function handles this request, retrieving the entered data using request.form.get(). The username is then used to query the database for a matching user record, and the password is verified against the stored hash. If the credentials are valid, the user is logged in and redirected to the appropriate dashboard. This process ensures that user input is securely collected, processed, and authenticated against the database, adhering to best practices like password hashing.
(Same process with all data collected)
