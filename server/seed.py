from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()
    

   
    restaurants = []
    restaurants.append(Restaurant(name='ALLOY', address='25 ALLOY Nairobi'))
    restaurants.append(Restaurant(name='CJ', address='25 Limuru Road'))
    restaurants.append(Restaurant(name='Big Knife', address='840 Hurlingham')),
    restaurants.append(Restaurant(name='seventy seven', address='250 Nairobi')),
    restaurants.append(Restaurant(name='Taco Bell', address='234 Taco Rd, Nairobi')),
    restaurants.append(Restaurant(name='BBQ Heaven', address='567 BBQ Blvd')), 
    restaurants.append(Restaurant(name='Pasta Fiesta', address='111 Pasta Ave, Nakuru')),
    restaurants.append(Restaurant(name='Dominos', address='123 Moi Avenue')),
    restaurants.append(Restaurant(name='Salad Oasis', address='222 Salad Blvd')),
    restaurants.append(Restaurant(name='Dessert Dream', address='333 Dessert St'))
    db.session.add_all(restaurants)

   
    pizzas = []
    pizzas.append(
        Pizza(name='Cheese Lover', ingredients='Tomato, Mozzarella, Basil'))
    pizzas.append(
        Pizza(name='Spicy Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni'))
    pizzas.append(
        Pizza(name='Veggie Delight', ingredients='Tomato, Mozzarella, Mixed Vegetables'))
    pizzas.append(
        Pizza(name='Tropical Hawaiian', ingredients='Tomato, Mozzarella, Ham, Pineapple'))
    pizzas.append(
        Pizza(name='BBQ Beef', ingredients='BBQ Sauce, Mozzarella, Chicken, Red Onion'))
    pizzas.append(
        Pizza(name='Supreme Deluxe', ingredients='Tomato, Mozzarella, Pepperoni, Mushroom, Bell Pepper, Olive'))
    pizzas.append(
        Pizza(name='Seafood Extravaganza', ingredients='Tomato, Mozzarella, Shrimp, Calamari, Clam'))
    pizzas.append(
        Pizza(name='Mushroom madness', ingredients='Tomato, Mozzarella, Mushroom Variety'))
    pizzas.append(
        Pizza(name='Carnivore Feast', ingredients='Tomato, Mozzarella, Sausage, Bacon, Ham, Pepperoni'))
    pizzas.append(
        Pizza(name='Four Seasons', ingredients='Mozzarella, Cheddar, Gorgonzola, Parmesan'))

    db.session.add_all(pizzas)


    restaurant_pizzas = []
    restaurant_pizzas.append(RestaurantPizza(
        price=10, restaurant=restaurants[0], pizza=pizzas[0]))
    restaurant_pizzas.append(RestaurantPizza(
        price=12, restaurant=restaurants[1], pizza=pizzas[1]))
    restaurant_pizzas.append(RestaurantPizza(price=11,
                             restaurant=restaurants[2], pizza=pizzas[2]))
    restaurant_pizzas.append(RestaurantPizza(price=13,
                             restaurant=restaurants[3], pizza=pizzas[3]))
    restaurant_pizzas.append(RestaurantPizza(price=15,
                             restaurant=restaurants[4], pizza=pizzas[4]))
    restaurant_pizzas.append(RestaurantPizza(price=14,
                             restaurant=restaurants[5], pizza=pizzas[5]))
    restaurant_pizzas.append(RestaurantPizza(price=16,
                             restaurant=restaurants[6], pizza=pizzas[6]))
    restaurant_pizzas.append(RestaurantPizza(price=17,
                             restaurant=restaurants[7], pizza=pizzas[7]))
    restaurant_pizzas.append(RestaurantPizza(price=18,
                             restaurant=restaurants[8], pizza=pizzas[8]))
    restaurant_pizzas.append(RestaurantPizza(price=19,
                             restaurant=restaurants[9], pizza=pizzas[9]))
    db.session.add_all(restaurant_pizzas)

    db.session.commit()