from project import db
from project.models import Kickoff, PapResults

# from project.models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(PapResults('Janet',52,3968,"13919112077","Hydroelectric","unk",1,">5000",1,0,"<50%",0,0,0,0,0,"not bad","3 years","Janet","unk",1))
db.session.add(PapResults("史有梅",62,3969,"15809308992","生产路","unk",1,">5000",1,0,"<50%",0,0,0,0,0,"细胞炎性改变，轻度炎症","三年","林大夫",'unk',1))
db.session.add(PapResults("王英菊",42,3970,"18393005742","临夏市拆桥镇后古村一组","unk",1,">5000",1,0,">75%",0,0,0,1,0,"细胞炎性改变，中度炎症","一年","林大夫","unk",1))

# commit the changes
db.session.commit()
