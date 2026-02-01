import streamlit as st
from datetime import date

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Modern Alpine 2025 | Book Your Stay",
    page_icon="🏔️",
    layout="centered"
)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://assets.squarespace.com/universal/images-v6/parking-page/backgrounds/img101-portrait.avif");
        background-size: cover;
        background-position: center center;  /* Centers the image */
        background-repeat: no-repeat;
        background-attachment: local; /* Ensures the background scrolls with content */
    }}
    </style>
    """,
    unsafe_allow_html=True
)



# --------------------
# Listing Data
# --------------------
PROPERTY_NAME = "Modern Alpine 2025"
TAGLINE = "Modern Loft Cabin With Stairs"
PRICE_PER_NIGHT = 299
MAX_GUESTS = 4

DESCRIPTION = """
**Introducing the Modern Alpine 2025** — the next evolution in mountain modern living.

This reimagined design features a dramatic **floor-to-ceiling glass gable wall**
that frames your surroundings like a living masterpiece.

The thoughtfully planned interior flows seamlessly from a welcoming entryway
to a **fully enclosed bedroom**, **contemporary kitchen**, and inviting living space.
At its heart, a **code-compliant staircase** adds both safety and architectural presence.

Perfect for **hospitality ventures or private retreats**, the Modern Alpine 2025
delivers sophisticated space planning and stunning views that truly bring the outside in.
"""

FEATURES = [
    "🏠 880 sq ft (40' x 16' plus loft)",
    "📐 Approx. 21' height (foundation to roof peak)",
    "🛏️ Sleeps 4",
    "🛌 Lofted bedroom",
    "🛌 First-floor bedroom",
    "🛁 Full bathroom with soaking tub",
    "🍳 Full kitchen with 4-burner stove",
    "🌲 Integrated outdoor deck",
    "🪟 Entire 16' wall of glass"
]

# --------------------
# Header
# --------------------
st.title("🏔️ Modern Alpine 2025")
st.subheader(TAGLINE)
st.caption("Mountain Modern • Real Builds • Hospitality Ready")

# --------------------
# Hero Image
# --------------------
st.image(
    "images/front.png",
    caption="Floor-to-ceiling glass gable wall with alpine views"
)

# --------------------
# Description
# --------------------
st.markdown(DESCRIPTION)

# --------------------
# Features
# --------------------
st.header("✨ Features")

for feature in FEATURES:
    st.write(feature)

st.divider()

# --------------------
# Booking Section
# --------------------
st.header("📅 Book Your Stay")

col1, col2 = st.columns(2)

with col1:
    check_in = st.date_input(
        "Check-in",
        min_value=date.today()
    )

with col2:
    check_out = st.date_input(
        "Check-out",
        min_value=check_in
    )

guests = st.number_input(
    "Guests",
    min_value=1,
    max_value=MAX_GUESTS,
    value=2
)

# --------------------
# Pricing Logic
# --------------------
nights = (check_out - check_in).days

if nights > 0:
    total_price = nights * PRICE_PER_NIGHT

    st.success(f"💲 ${PRICE_PER_NIGHT} per night")
    st.info(f"🛏️ {nights} nights × ${PRICE_PER_NIGHT} = **${total_price}**")

    if st.button("🛒 Reserve Now"):
        st.balloons()
        st.success("🎉 Reservation Confirmed!")
        st.write("### Reservation Summary")
        st.write(f"**Property:** {PROPERTY_NAME}")
        st.write(f"**Dates:** {check_in} → {check_out}")
        st.write(f"**Guests:** {guests}")
        st.write(f"**Total:** ${total_price}")
else:
    st.warning("⚠️ Check-out date must be after check-in.")

# --------------------
# Footer
# --------------------
st.divider()
st.caption("© 2026 Modern Alpine Stays • Demo booking experience built with Streamlit")
