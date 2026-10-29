<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quick E-Shop</title>
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans min-h-screen pb-10">

    <!-- Header -->
    <header class="bg-blue-600 text-white p-4 shadow-md sticky top-0 z-50 flex justify-between items-center">
        <h1 class="text-xl font-bold">🛒 Quick E-Commerce App</h1>
        <button onclick="toggleCart()" class="relative bg-blue-700 px-4 py-2 rounded-lg text-sm font-semibold hover:bg-blue-800 transition">
            🛍️ Cart (<span id="cart-count">0</span>)
        </button>
    </header>

    <div class="max-w-4xl mx-auto px-4 mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Products Grid -->
        <div class="md:col-span-2 space-y-4" id="products-list">
            <!-- Laptop -->
            <div class="bg-white p-4 rounded-xl shadow-sm border border-gray-200 flex flex-col justify-between">
                <div>
                    <div class="text-3xl mb-1">💻</div>
                    <h3 class="text-lg font-bold text-gray-800">Laptop</h3>
                    <p class="text-gray-500 text-sm mt-1">High performance for coding.</p>
                </div>
                <div class="flex justify-between items-center mt-4">
                    <span class="text-blue-600 font-bold text-lg">₹55,000</span>
                    <button onclick="addToCart('Laptop', 55000)" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">Add to Cart</button>
                </div>
            </div>

            <!-- Wireless Mouse -->
            <div class="bg-white p-4 rounded-xl shadow-sm border border-gray-200 flex flex-col justify-between">
                <div>
                    <div class="text-3xl mb-1">🖱️</div>
                    <h3 class="text-lg font-bold text-gray-800">Wireless Mouse</h3>
                    <p class="text-gray-500 text-sm mt-1">Ergonomic 2.4GHz mouse.</p>
                </div>
                <div class="flex justify-between items-center mt-4">
                    <span class="text-blue-600 font-bold text-lg">₹1,200</span>
                    <button onclick="addToCart('Wireless Mouse', 1200)" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">Add to Cart</button>
                </div>
            </div>

            <!-- Smart Watch -->
            <div class="bg-white p-4 rounded-xl shadow-sm border border-gray-200 flex flex-col justify-between">
                <div>
                    <div class="text-3xl mb-1">⌚</div>
                    <h3 class="text-lg font-bold text-gray-800">Smart Watch</h3>
                    <p class="text-gray-500 text-sm mt-1">Tracks steps, sleep, and heart rate.</p>
                </div>
                <div class="flex justify-between items-center mt-4">
                    <span class="text-blue-600 font-bold text-lg">₹4,500</span>
                    <button onclick="addToCart('Smart Watch', 4500)" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">Add to Cart</button>
                </div>
            </div>
        </div>

        <!-- Sidebar Cart (Hidden on tiny screens initially, controlled by toggle) -->
        <div id="cart-sidebar" class="bg-white p-6 rounded-xl shadow-md border border-gray-200 h-fit sticky top-20">
            <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">🛍️ Your Cart</h2>
            <div id="cart-items" class="space-y-3 text-sm text-gray-600">
                <p id="empty-msg">Your cart is empty.</p>
            </div>
            <hr class="my-4 border-gray-200">
            <div class="flex justify-between items-center mb-4">
                <span class="font-semibold text-gray-700">Total:</span>
                <span id="cart-total" class="text-xl font-bold text-gray-900">₹0</span>
            </div>
            <button onclick="checkout()" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-xl transition shadow-md">🚀 Checkout</button>
        </div>
    </div>

    <!-- Simple Cart Functionality Script -->
    <script>
        let cart = {};
        
        function addToCart(name, price) {
            if (cart[name]) {
                cart[name].qty += 1;
            } else {
                cart[name] = { price: price, qty: 1 };
            }
            updateCartUI();
        }

        function removeFromCart(name) {
            delete cart[name];
            updateCartUI();
        }

        function updateCartUI() {
            const itemsContainer = document.getElementById('cart-items');
            const totalContainer = document.getElementById('cart-total');
            const countContainer = document.getElementById('cart-count');
            
            itemsContainer.innerHTML = '';
            let total = 0;
            let count = 0;
            
            const keys = Object.keys(cart);
            if (keys.length === 0) {
                itemsContainer.innerHTML = '<p id="empty-msg">Your cart is empty.</p>';
            } else {
                keys.forEach(name => {
                    const itemTotal = cart[name].price * cart[name].qty;
                    total += itemTotal;
                    count += cart[name].qty;
                    
                    const itemRow = document.createElement('div');
                    itemRow.className = 'flex justify-between items-center border-b border-gray-100 pb-2';
                    itemRow.innerHTML = `
                        <div>
                            <span class="font-medium text-gray-800">${name}</span>
                            <span class="text-gray-400 text-xs block">Qty: ${cart[name].qty}</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="font-semibold text-gray-700">₹${itemTotal.toLocaleString('en-IN')}</span>
                            <button onclick="removeFromCart('${name}')" class="text-red-500 text-lg hover:scale-110 transition">❌</button>
                        </div>
                    `;
                    itemsContainer.appendChild(itemRow);
                });
            }
            
            totalContainer.innerText = '₹' + total.toLocaleString('en-IN');
            countContainer.innerText = count;
        }

        function checkout() {
            if (Object.keys(cart).length === 0) {
                alert("Add some products to your cart first!");
                return;
            }
            alert("Order Placed Successfully! 🎉");
            cart = {};
            updateCartUI();
        }
    </script>
</body>
</html>
