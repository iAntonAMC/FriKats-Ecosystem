import sqlite3
from fastapi import HTTPException
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
