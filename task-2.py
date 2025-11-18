# Store product info in a Python list of dicts → write functions to add product, update product, delete product.

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 700},
    {"id": 3, "name": "Keyboard", "price": 1200}
]

#Fuction to add 
def add_products(pid,name,price):
    products.append({'id':pid,'name':name,'price':price})
    return f"Product {name} added"

#fuction to update products
def update_products(pid,name=None,price=None):
    for p in products:
        if p["id"] == id:
            if name is not None:
                p["name"] = name
            if price is not None:
                p["price"] = price
            return f"Product {pid} updated"
    return "Product not found"

#Function to delete a product
def delete_products(pid):
    for p in products:
        if p["id"] == pid:
            products.remove(p)
            return f"Product {pid} deleted"
    return "Product not found"


print(add_products(4,'Condom',450))
# print(delete_products(3))
print(update_products(3,price=1000))


print(products)