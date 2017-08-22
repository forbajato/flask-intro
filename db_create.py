from project import db
from project.models import BlogPost
# from project.models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 1))
db.session.add(BlogPost("Postgresql", "We set up Postgresql database", 3))

# commit the changes
db.session.commit()
