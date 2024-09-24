def update_inventory(inventory, restock=[]):
    # product[0] is product name. product[1] is product descriptions and weight.
    # product[2][0] is the product quantity. product[2][1] is the product aisle.
    for product in restock:
        if product[0] in inventory.keys():
            for description in product[1]:
                if description != '':
                    inventory[product[0]][0].insert(-1, description)
            inventory[product[0]][1][0] += product[2][0]
            if product[2][1] != '':
                inventory[product[0]][1][1] += ' ' + product[2][1]
        else:
            inventory[product[0]] = []
            for i in range(1, len(product)):
                inventory[product[0]].append(product[i])
    return inventory

def merge_inventory(inventory, new_inventory={}):
    # product[0] is product name. product[1] is product descriptions and weight.
    # product[2] contains the quantity of the product, and aisle of the product.
    inventory_dict = {}
    new_inventory_list = []
    for product in inventory:
        if len(product) != 0:
            inventory_dict[product[0]] = []
            for i in range(1, len(product)):
                inventory_dict[product[0]].append(product[i])
    for key, value in new_inventory.items():
        new_inventory_list.append([key, value[0], value[1]])
    return update_inventory(inventory_dict, new_inventory_list)

def products_info(products, products_detail, new_products_detail=[]):
    # i represents the index products, products_detail, and new_products_detail.
    products_dict = {}
    for i in range(len(products)):
        products_detail[i].insert(0, products[i])
        if len(new_products_detail) != 0:
            if len(new_products_detail[i]) != 0:
                products_dict[products[i]] = new_products_detail[i]
    return merge_inventory(products_detail, products_dict)

def digits_summation(n):
    # the function keeps calling itself and floor dividing n until it reaches 0.
    # after that, it adds all the remainders in the previous functions together.
    # floor dividing n by 10 causes each digit to eventually become first digit.
    if n != 0:
        return digits_summation(n // 10) + (n % 10)
    return 0

def vowel_counts(some_str, results={}):
    # the vowels list represents all of the vowels that are possible in results.
    # the function keeps calling itself and slicing the last letter of some_str.
    # slicing causes the last letter to change each time vowel_counts is called.
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if results == {}:
        results = {}
    if some_str != '':
        if some_str[-1] in vowel_list:
            if some_str[-1] in results.keys():
                results[some_str[-1]] += 1
            else:
                results[some_str[-1]] = 1
        return vowel_counts(some_str[:len(some_str)-1], results)
    return results
