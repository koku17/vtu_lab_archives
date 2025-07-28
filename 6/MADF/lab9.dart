import 'package:flutter/material.dart';

void main() {
  runApp(const ECommerceApp());
}

class ECommerceApp extends StatelessWidget {
  const ECommerceApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'E-Commerce UI',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: const ProductListPage(),
    );
  }
}

class Product {
  final String name;
  final double price;
  final String imageUrl;

  const Product({
    required this.name,
    required this.price,
    required this.imageUrl,
  });
}

class ProductListPage extends StatefulWidget {
  const ProductListPage({super.key});

  @override
  State<ProductListPage> createState() => _ProductListPageState();
}

class _ProductListPageState extends State<ProductListPage> {
  final List<Product> products = const [
    Product(
      name: "Sneakers",
      price: 59.99,
      imageUrl: 'https://cdn.pixabay.com/photo/2017/07/13/02/53/shoe-2498994_640.jpg',
    ),
    Product(
      name: "Backpack",
      price: 39.99,
      imageUrl: 'https://cdn.pixabay.com/photo/2017/06/30/21/53/backpack-2459934_640.png',
    ),
    Product(
      name: "Watch",
      price: 99.99,
      imageUrl: 'https://cdn.pixabay.com/photo/2022/09/21/06/35/watch-7469601_640.jpg',
    ),
    Product(
      name: "T-Shirt",
      price: 19.99,
      imageUrl: 'https://cdn.pixabay.com/photo/2024/04/29/04/21/tshirt-8726716_1280.jpg ',
    ),
  ];

  final List<Product> cart = [];

  void addToCart(Product product) {
    setState(() {
      cart.add(product);
    });
  }

  void goToCartPage() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => CartPage(cartItems: cart)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("ShopNow"),
        actions: [
          Stack(
            children: [
              IconButton(
                icon: const Icon(Icons.shopping_cart),
                onPressed: goToCartPage,
              ),
              if (cart.isNotEmpty)
                Positioned(
                  right: 6,
                  top: 6,
                  child: CircleAvatar(
                    radius: 10,
                    backgroundColor: Colors.red,
                    child: Text(
                      '${cart.length}',
                      style: const TextStyle(color: Colors.white, fontSize: 12),
                    ),
                  ),
                ),
            ],
          ),
        ],
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(12),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 0.7,
        ),
        itemCount: products.length,
        itemBuilder: (context, index) {
          final product = products[index];
          return ProductCard(product: product, onAddToCart: addToCart);
        },
      ),
    );
  }
}

class ProductCard extends StatelessWidget {
  final Product product;
  final void Function(Product) onAddToCart;

  const ProductCard({
    super.key,
    required this.product,
    required this.onAddToCart,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: ClipRRect(
              borderRadius: const BorderRadius.vertical(
                top: Radius.circular(15),
              ),
              child: Image.network(
                product.imageUrl,
                width: double.infinity,
                fit: BoxFit.cover,
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(10),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  product.name,
                  style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
                const SizedBox(height: 5),
                Text(
                  "\$${product.price.toStringAsFixed(2)}",
                  style: const TextStyle(color: Colors.grey),
                ),
                const SizedBox(height: 10),
                ElevatedButton(
                  onPressed: () => onAddToCart(product),
                  style: ElevatedButton.styleFrom(
                    minimumSize: const Size.fromHeight(35),
                  ),
                  child: const Text("Add to Cart"),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class CartPage extends StatelessWidget {
  final List<Product> cartItems;

  const CartPage({super.key, required this.cartItems});

  @override
  Widget build(BuildContext context) {
    double total = cartItems.fold(0, (sum, item) => sum + item.price);

    return Scaffold(
      appBar: AppBar(title: const Text("Your Cart")),
      body: cartItems.isEmpty
          ? const Center(child: Text("Your cart is empty."))
          : ListView.builder(
              padding: const EdgeInsets.all(10),
              itemCount: cartItems.length,
              itemBuilder: (context, index) {
                final product = cartItems[index];
                return Card(
                  child: ListTile(
                    leading: Image.network(
                      product.imageUrl,
                      width: 50,
                      fit: BoxFit.cover,
                    ),
                    title: Text(product.name),
                    subtitle: Text("\$${product.price.toStringAsFixed(2)}"),
                  ),
                );
              },
            ),
      bottomNavigationBar: Container(
        padding: const EdgeInsets.all(16),
        color: Colors.indigo,
        child: Text(
          "Total: \$${total.toStringAsFixed(2)}",
          style: const TextStyle(
            color: Colors.white,
            fontSize: 18,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}
