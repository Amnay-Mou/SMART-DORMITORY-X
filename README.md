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




