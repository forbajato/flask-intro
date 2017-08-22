from project import db
from project.models import Kickoff, PapResults

# from project.models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(Kickoff("Linxia","2017-07-09"))

# commit the changes
db.session.commit()
