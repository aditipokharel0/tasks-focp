def calculate_price(num_pizzas, delivery, is_tuesday, used_app):
    pizza_price = 12.0
    delivery_cost = 2.5
    app_discount = 0.25

   
    if is_tuesday:
        pizza_price *= 0.5

    total_pizza_cost = num_pizzas * pizza_price

    if delivery == 'y':
        if num_pizzas >= 5:
            delivery_cost = 0.0
        total_pizza_cost += delivery_cost

    if used_app == 'y':
        total_pizza_cost *= (1.0 - app_discount)

    return round(total_pizza_cost, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    while True:
        delivery = input("Is delivery required? (y/n) ").lower()
        if delivery in ['y', 'n']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        is_tuesday = input("Is it Tuesday? (y/n) ").lower()
        if is_tuesday in ['y', 'n']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        used_app = input("Did the customer use the app? (y/n) ").lower()
        if used_app in ['y', 'n']:
            break
        else:
            print('Please answer "Y" or "N".')

    total_price = calculate_price(num_pizzas, delivery, is_tuesday == 'y', used_app == 'y')
    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
