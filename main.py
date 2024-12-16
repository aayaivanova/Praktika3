if __name__ == '__main__':
    from product import Product

    product = Product('Книга', 150)

    print(product)

    product.set_discount(10)
    print(f"Цена со скидкой: {product.current_price} рублей")

    product.set_price(120)
    print(f"Новая цена товара: {product.get_price()} рублей")

    fixed_price_product = Product.create_fix_price('С фикцированной ценой')
    print(fixed_price_product)