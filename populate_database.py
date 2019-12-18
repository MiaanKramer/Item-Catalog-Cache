from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind engine to a session
Session = sessionmaker(bind=engine)

# Create session object.
session = Session()

user = User(
    name='Miaan Kramer',
    email='miaankatkramer@gmail.com',
)

session.add(user)
session.commit()

category = Category(
    name='Gaming',
    user=user
)

session.add(category)
session.commit()

item = Item(
    name='Headphones',
    description='The Razer Kraken Chroma is a top of the range headhone',
    category=category,
    user=user
)

session.add(item)
session.commit()

print('Database Populated')