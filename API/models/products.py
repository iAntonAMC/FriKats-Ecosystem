import sqlite3
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse


# CREATE ONE
def create(product):
    try:
        with sqlite3.connect("DB/frikats.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("INSERT INTO products (product_sku, product_name, product_description, product_price, product_image, product_stock, id_category) VALUES (?,?,?,?,?,?,?);", (product.product_sku, product.product_name, product.product_description, product.product_price, product.product_image, product.product_stock, product.id_category))
            cnxn.commit()
            return JSONResponse(status_code = 201, content = {"message":"Product inserted successfully"})
    except Exception as error:
        print(f"Error in products.create: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.create method dropped an error: {error}"
        )
    finally:
        cursor.close()
        cnxn.close()

# GET ALL
def getAll():
    try:
        with sqlite3.connect("DB/frikats.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM products;")
            results = cursor.fetchall()
            if results == []:
                return JSONResponse(status_code = 404, content = {"message":"There are no products in database"})
            else:
                products = []
                print(results)
                for product in results:
                    products.append({
                        "id_product":product[0],
                        "product_sku":product[1],
                        "product_name":product[2],
                        "product_description":product[3],
                        "product_price":product[4],
                        "product_image":product[5],
                        "product_stock":product[6],
                        "id_category":product[7]
                    })
            return products
    except Exception as error:
        print(f"Error in products.getAll: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.getAll method dropped an error: {error}"
        )
    finally:
        cursor.close()
        cnxn.close()

# GET ONE
def getOne(id_product):
    try:
        with sqlite3.connect("DB/frikats.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM products WHERE id_product = ?;", (id_product))
            results = cursor.fetchone()
            if results == None:
                return JSONResponse(status_code = 404, content = {"message":"Can´t find 'id_product' in DB"})
            else:
                product = {
                        "id_product":results[0],
                        "product_sku":results[1],
                        "product_name":results[2],
                        "product_description":results[3],
                        "product_price":results[4],
                        "product_image":results[5],
                        "product_stock":results[6],
                        "id_category":results[7]
                }
            return product
    except Exception as error:
        print(f"Error in products.getOne: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.getOne method dropped an error: {error}"
        )
    finally:
        cursor.close()
        cnxn.close()

# UPDATE ONE
def update(id_product, product):
    try:
        with sqlite3.connect("DB/frikats.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM products WHERE id_product = ?;", (id_product))
            results = cursor.fetchone()
            if results == None:
                return JSONResponse(status_code = 404, content = {"message":"Can´t find 'id_product' in DB"})
            else:
                cursor.execute("UPDATE products SET product_sku = ?, product_name = ?, product_description = ?, product_price = ?, product_image = ?, product_stock = ?, id_category = ? WHERE id_product = ?;", (product.product_sku, product.product_name, product.product_description, product.product_price, product.product_image, product.product_stock, product.id_category, id_product))
                cnxn.commit()
                return JSONResponse(status_code = 200, content = {"message":"Product updated successfully"})
    except Exception as error:
        print(f"Error in products.update: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.update method dropped an error: {error}"
        )
    finally:
        cursor.close()
        cnxn.close()


# SEARCH BY NAME
def searchName(product_name):
    try:
        with sqlite3.connect("DB/frikats.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM products WHERE product_name LIKE ?;", (f"%{product_name}%",))
            results = cursor.fetchall()
            if results == []:
                return JSONResponse(status_code = 404, content = {"message":"Can´t find 'product_name' in DB"})
            else:
                products = []
                for product in results:
                    products.append({
                        "id_product":product[0],
                        "product_sku":product[1],
                        "product_name":product[2],
                        "product_description":product[3],
                        "product_price":product[4],
                        "product_image":product[5],
                        "product_stock":product[6],
                        "id_category":product[7]
                    })
            return products
    except Exception as error:
        print(f"Error in products.searchByName: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.searchByName method dropped an error: {error}"
        )
    finally:
        cursor.close()
        cnxn.close()
