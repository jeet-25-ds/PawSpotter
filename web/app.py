
import streamlit as st
from PIL import Image
import tempfile
import os
import sys

# =========================
# PATH SETUP
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_DIR)

from predict import predict_image

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="PawSpotter",
    page_icon="🐾",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#f3f6fb;
}

.block-container{
    padding-top:1rem;
    max-width:1600px;
}

/* Header */
.title{
    text-align:center;
    font-size:4rem;
    font-weight:800;
    color:#123462;
    margin-bottom:20px;
}

/* Section Titles */
.small-title{
    font-size:2rem;
    font-weight:700;
    color:#0f172a;
    margin-bottom:15px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:1px solid #e5e7eb;
}

/* Buttons */
.stButton button{
    height:55px;
    font-size:18px;
    font-weight:600;
    border-radius:12px;
}

/* Upload Box */
[data-testid="stFileUploader"]{
    background:white;
    padding:15px;
    border-radius:15px;
}

/* Progress */
[data-testid="stProgressBar"]{
    height:18px;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.06);
}

/* Hide Streamlit Footer */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("🐾 Menu")

    st.markdown("---")

    st.subheader("About")

    st.write("""
    CNN-Based Dog vs Cat Classifier
    """)

    st.markdown("### Dataset")

    st.write("• 25,000 Images")

    st.markdown("### Classes")

    st.write("• Dog")
    st.write("• Cat")

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Images", "25K")

    with c2:
        st.metric("Classes", "2")

    st.metric(
        "Val Accuracy",
        "82%"
    )

    st.markdown("---")

    st.info("Custom CNN")

# =========================
# HEADER
# =========================

st.markdown(
    """
    <div class='title'>
        🐾 PawSpotter
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# MAIN LAYOUT
# =========================

col1, col2, col3 = st.columns([1.1, 1.2, 1.1])

# =========================
# LEFT PANEL
# =========================

with col1:

    st.markdown(
        """
        <div class='small-title'>
            Control Panel
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Dog/Cat Image",
        type=["jpg", "jpeg", "png"]
    )

    confidence_threshold = st.slider(
        "Confidence Threshold",
        0,
        100,
        50
    )

    st.write("")

    predict_btn = st.button(
        "🔍 Predict Image",
        use_container_width=True
    )

# =========================
# CENTER PANEL
# =========================

with col2:

    st.markdown(
        """
        <div class='small-title'>
            Image Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    if uploaded_file:

        img = Image.open(uploaded_file)

        st.image(
            img,
            caption="Uploaded Image",
            width=550
        )

# =========================
# RIGHT PANEL
# =========================

with col3:

    st.markdown(
        """
        <div class='small-title'>
            Prediction Summary
        </div>
        """,
        unsafe_allow_html=True
    )

    if uploaded_file and predict_btn:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as temp_file:

            temp_file.write(
                uploaded_file.getvalue()
            )

            temp_path = temp_file.name

        label, confidence = predict_image(
            temp_path
        )

        if confidence >= confidence_threshold:

            emoji = "🐶" if label == "Dog" else "🐱"

            # Prediction Card

            st.markdown(
                f"""
                <div style="
                background:#ecfdf5;
                padding:25px;
                border-radius:18px;
                text-align:center;
                margin-bottom:15px;
                ">
                    <h1>{emoji}</h1>
                    <h2 style="color:#166534;">
                        {label.upper()}
                    </h2>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Confidence Card

            st.markdown(
                f"""
                <div style="
                background:white;
                padding:20px;
                border-radius:18px;
                text-align:center;
                margin-bottom:15px;
                box-shadow:0 4px 12px rgba(0,0,0,0.05);
                ">
                    <h3>Confidence Score</h3>
                    <h1 style="color:#2563eb;">
                        {confidence:.2f}%
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                min(int(confidence), 100)
            )

            st.markdown("---")

            st.subheader("Model Details")

            st.info("""
Model: Custom CNN

Input Size: 96 × 96

Classes: Dog / Cat

Framework: TensorFlow
            """)

        else:

            st.warning(
                "Prediction confidence below threshold."
            )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "🐾 PawSpotter • Built with TensorFlow, CNN & Streamlit"
)

