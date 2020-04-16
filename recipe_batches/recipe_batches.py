#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    batches = 0
    while True:
        should_break = False
        for i in recipe:
            if i not in ingredients.keys() or recipe[i] > ingredients[i]:
                should_break = True
                break
            ingredients[i] -= recipe[i]
        if should_break:
            break
        batches += 1
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches = recipe_batches(recipe, ingredients), ingredients = ingredients))
