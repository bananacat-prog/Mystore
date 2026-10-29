import streamlit as st

st.set_page_config(page_title="Quick E-Shop", page_icon="🛒", layout="wide")
st.title("🛒 Quick E-Commerce App")

if "cart" not in st.session_state:
    st.session_state.cart = {}

products = {
    "Laptop": {"price": 55000, "desc": "High performance for coding.", "emoji": "💻"},
    "Wireless Mouse": {"price": 1200, "desc": "Ergonomic 2.4GHz mouse.", "emoji": "🖱️"},
    "Smart Watch": {"price": 4500, "desc": "Tracks steps, sleep, and heart rate.", "emoji": "⌚"},
    "Headphones": {"price": 3500, "desc": "Noise-cancelling over-ear headphones.", "emoji": "🎧"}
}

col1, col2 = st.columns()

with col1:
    st.subheader("Our Products")
    grid_cols = st.columns(2)
    for index, (name, info) in enumerate(products.items()):
        with grid_cols[index % 2]:
            st.write(f"### {info['emoji']} {name}")
            st.write(f"**Price:** ₹{info['price']:,}")
            st.write(info['desc'])
            
            if st.button(f"Add {name} to Cart", key=name):
                if name in st.session_state.cart:
                    st.session_state.cart[name] += 1
                else:
                    st.session_state.cart[name] = 1
                st.success(f"Added {name}!")

with col2:
    st.subheader("🛍️ Your Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
        total_price = 0
    else:
        total_price = 0
        for name, qty in list(st.session_state.cart.items()):
            item_total = products[name]['price'] * qty
            total_price += item_total
            st.write(f"**{name}** x{qty} — ₹{item_total:,}")
            if st.button("❌", key=f"remove_{name}"):
                del st.session_state.cart[name]
                st.rerun()
        st.write("---")
        st.write(f"### Total: ₹{total_price:,}")
        if st.button("🚀 Checkout", type="primary"):
            st.balloons()
            st.success("Order Placed Successfully!")
            st.session_state.cart = {}
