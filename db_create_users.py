from app import db
from models import User

# insert data
db.session.add(User('tom', 'tom@example.com', 'i no tell'))
db.session.add(User('janet', 'janet@hotmama.com', 'baby'))
db.session.add(User('admin', 'ad@min.com', 'admin'))

# commit changes
db.session.commit()
