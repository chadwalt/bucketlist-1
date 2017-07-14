# BucketList

[![Build Status](https://travis-ci.org/jokamjohn/bucketlist.svg?branch=master)](https://travis-ci.org/jokamjohn/bucketlist)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/11fc4593f01d42d9af9fd30b8670ebcc)](https://www.codacy.com/app/jokamjohn/bucketlist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jokamjohn/bucketlist&amp;utm_campaign=Badge_Grade)

 This is an application that enables users to record and
 share things they want to achieve or experience before reaching
 a certain age and keeping track of their dreams and
 goals.
 
 ## Features
 The application has a couple of features as listed below:-
 * A user is able to `Register` and get an account in the app
 * A user is able to `Login` into the app using their credentials already supplied
 * A user is able to create, edit, update and delete `Buckets`
 * A user is also able to create, edit, update and delete `Bucket Items`
 
 
 ## Setup
 To start using this application, first clone it to your local machine by running
 
 ```
 git clone https://github.com/jokamjohn/bucketlist.git
 cd bucketlist
 ```
 
 Create the virtual environment and activate it
 
 ```
 virtualenv env
 source env/bin/activate
```

Then install all the required dependencies

```
pip install -r requirements.txt
```

Then run the application

```
python run.py
```

To now view the application head over to
```
http://localhost:5000
```
 
### Testing
You can then run the application tests using
```
cd bucketlist
nosetests tests
```
 
 