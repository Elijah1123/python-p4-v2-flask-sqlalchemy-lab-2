from app import app
from models import db, Customer, Item, Review

with app.app_context():
   
    print("Clearing existing data...")
    db.drop_all()
    db.create_all()

    
    print("Creating customers...")
    c1 = Customer(name="Tal Yuri")
    c2 = Customer(name="Sandra Mwai")
    c3 = Customer(name="James Kimani")

    
    print("Creating items...")
    i1 = Item(name="Laptop Backpack", price=49.99)
    i2 = Item(name="Insulated Coffee Mug", price=9.99)
    i3 = Item(name="Wireless Mouse", price=14.99)

   
    print("Creating reviews...")
    r1 = Review(comment="Great backpack for travel", customer=c1, item=i1)
    r2 = Review(comment="Keeps coffee hot all day", customer=c1, item=i2)
    r3 = Review(comment="Works perfectly with my laptop", customer=c2, item=i3)
    r4 = Review(comment="Very durable and spacious", customer=c3, item=i1)

    
    print("Committing to database...")
    db.session.add_all([c1, c2, c3, i1, i2, i3, r1, r2, r3, r4])
    db.session.commit()

    print("Seeding completed successfully.")
