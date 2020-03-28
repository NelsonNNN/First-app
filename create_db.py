from app import db 
from SQLalch import BlogPost

#create database
db.create_all()


#insert
db.session.add(BlogPost("I am Nelson", "I am doing programming"))
db.session.add(BlogPost("Another thing", "I love guitars"))

#commit
db.session.commit()