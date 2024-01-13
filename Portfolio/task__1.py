def calculate_price(number_of_pizzas, delivery, tuesday, app_used):
    price_of_pizza = 12.0
    cost_of_delivery = 2.5
    app_discount = 0.25


    if tuesday:
        price_of_pizza *= 0.5

    total_pizza_price = number_of_pizzas * price_of_pizza

    if delivery == 'y':
        if number_of_pizzas >= 5:
            cost_of_delivery = 0.0
        total_pizza_price += cost_of_delivery


    if app_used == 'y':
        total_pizza_price *= (1.0 - app_discount)

    return round(total_pizza_price, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")


    while True:
        try:
            number_of_pizzas = int(input("How many pizzas ordered? "))
            if number_of_pizzas< 0:
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
        tuesday = input("Is it Tuesday? (y/n) ").lower()
        if tuesday in ['y', 'n']:
            break
        else:
            print('Please answer "Y" or "N".')


    while True:
        app_used = input("Did the customer use the app? (y/n) ").lower()
        if app_used in ['y', 'n']:
            break
        else:
            print('Please answer "Y" or "N".')


    total_price = calculate_price(number_of_pizzas, delivery, tuesday == 'y', app_used == 'y')
    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
