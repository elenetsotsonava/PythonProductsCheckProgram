def add_product_to_warehouse(product_name, price, warehouse=None):
    if warehouse is None:
        warehouse = {}
    warehouse[product_name] = price
    return warehouse


def get_warehouse_items(warehouse):
    for product, price in warehouse.items():
        print(f"Product: {product}, price: {price}₾")


warehouse = {}

while True:
    try:
        action = int(input("What do you want to do? Choose Number\n1) Add Product\n2) See Product\n3) Choose\n4) Exit\nType option: "))
        if action == 1:
            num_products = int(input("How many products do you want to add? "))
            for i in range(num_products):
                product_name = input("Enter product name: ")
                price = float(input("Enter price: "))
                warehouse = add_product_to_warehouse(product_name, price, warehouse)
        elif action == 2:
            print("---------------------")
            get_warehouse_items(warehouse)
            print("---------------------")
        elif action == 3:
            total_price = 0
            while True:
                product_name = input("Enter product name (or END to stop choosing): ")
                if product_name == "END":
                    break
                if product_name in warehouse:
                    total_price += warehouse[product_name]
                else:
                    print("Product not found.")

            print("==================")
            print(f"ჯამში გადახდილია {total_price}₾")
            print("==================")
        elif action == 4:
            break
        else:
            print("Invalid action")
    except ValueError:
        print("Invalid Input. Please type only a number!\n- - - - - - - - - - - -\n")