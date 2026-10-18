"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


# Alternate Solution:
# for item in items_to_add:
#         current_cart[item]=current_cart.setdefault(item,0)+1
#     return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    return {item: 1 for item in notes}


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for keys, values in recipe_updates:
        ideas[keys] = values
    return ideas


# Alternate Solution
# ideas.update(update_recipes)
# return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_list = {}
    for item, aisle in aisle_mapping.items():
        if item in cart:
            fulfillment_list[item] = [
                cart[item],
                *aisle,
            ]  # * unpacks the aisle list so the value is not a nested list.
    return dict(sorted(fulfillment_list.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for ingredient, information in fulfillment_cart.items():
        if information[0] >= store_inventory[ingredient][0]:
            store_inventory[ingredient][0] = "Out of Stock"
        else:
            store_inventory[ingredient][0] -= information[0]

    return store_inventory
