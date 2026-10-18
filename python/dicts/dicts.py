"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    inventory_dictionary = {}
    for item in items:
        if inventory_dictionary.get(item, "not found") == "not found":
            inventory_dictionary[item] = 1
        else:
            inventory_dictionary[item] += 1
    return inventory_dictionary


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    for item in items:
        if inventory.get(item, "not found") == "not found":
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


# Alternate solutions
# for i in items:
#        inventory[i] = inventory.get(i, 0) + 1
#    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    for item in items:
        if inventory.get(item, "none") != "none" and inventory.get(item) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, "none")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    return_lst = []

    for key, value in inventory.items():
        if value != 0:
            return_lst.append((key, value))
    return return_lst


# Alternate Solution:
# output_inventory = [(k, v) for k, v in inventory.items() if inventory[k] > 0]
#     return output_inventory
