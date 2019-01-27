from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catalog, Base, Item, User
 
engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Admin
user = User(name = "Admin",email = "admin@admin.c")

session.add(user)
session.commit()

#Items for Sports
catalog1 = Catalog(name = "Sports", user = user)

session.add(catalog1)
session.commit()


item1 = Item(name = "Nike TShirt", description = "Description of the Nike TShirt ...", price = "200", catalog = catalog1, user = user)

session.add(item1)
session.commit()

item2 = Item(name = "Adidas TShirt", description = "Description of the Adidas TShirt ...", price = "100", catalog = catalog1, user = user)

session.add(item2)
session.commit()

item3 = Item(name = "Anta shose", description = "Description of the Anta shose ...", price = "150", catalog = catalog1, user = user)

session.add(item3)
session.commit()

#Items for Accessories

catalog2 = Catalog(name = "Accessories", user = user)

session.add(catalog2)
session.commit()


item1 = Item(name = "Accessory 1", description = "Description of the Accessory 1 ...", price = "25", catalog = catalog2, user = user)

session.add(item1)
session.commit()

item2 = Item(name = "Accessory 2", description = "Description of the Accessory 2 ...", price = "50", catalog = catalog2, user = user)

session.add(item2)
session.commit()

item3 = Item(name = "Accessory 3", description = "Description of the Accessory 3 ...", price = "15", catalog = catalog2, user = user)


session.add(item3)
session.commit()


#Items for Clothing

catalog3 = Catalog(name = "Clothing", user = user)

session.add(catalog3)
session.commit()


item1 = Item(name = "Shirt", description = "Description of the Shirt ...", price = "250", catalog = catalog3, user = user)

session.add(item1)
session.commit()

item2 = Item(name = "Pant", description = "Description of the Pant 2 ...", price = "500", catalog = catalog3, user = user)

session.add(item2)
session.commit()

item3 = Item(name = "Shose", description = "Description of the Shos 3 ...", price = "15", catalog = catalog3, user = user)


session.add(item3)
session.commit()



print "DONE... Database Created !!!"
