import streamlit as st
from datetime import datetime, date
import base64

from utils.storage import load_entries, save_entry, ensure_data_file
from utils.theme import get_theme
from utils.transitions import slow_render

# ---------- Page config ----------
st.set_page_config(
    page_title="Cozy Journal",
    page_icon="📖",
    layout="centered",
)

# Ensure data file exists
ensure_data_file()

# ---------- State ----------
if "current_rating" not in st.session_state:
    st.session_state.current_rating = 3  # neutral default

# ---------- Background + CSS ----------
def set_background(image_path: str, overlay_color: str = "rgba(0,0,0,0.5)"):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
    except FileNotFoundError:
        # Fallback background color if image isn't loaded yet
        encoded = ""

    css = f"""
    <style>
    /* Main Background Layout */
    .stApp {{
        background: {f'url("data:image/jpg;base64,{encoded}")' if encoded else "#14141a"} no-repeat center center fixed;
        background-size: cover;
        transition: background 0.8s ease-in-out;
    }}
    
    .overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: {overlay_color};
        z-index: -1;
        transition: background 0.8s ease-in-out;
    }}

    /* Elegant Glassmorphic Container */
    .cozy-card {{
        background: rgba(20, 20, 28, 0.65);
        padding: 2.2rem 2.5rem;
        border-radius: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin-top: 1rem;
        margin-bottom: 2rem;
    }}

    /* Typography */
    .cozy-title {{
        font-family: "Georgia", "Times New Roman", serif;
        font-size: 2.5rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }}
    
    .cozy-sub {{
        font-size: 1.05rem;
        color: #b0b3c2;
        font-style: italic;
        margin-top: 0.2rem;
    }}
    
    .cozy-label {{
        font-size: 0.95rem;
        font-weight: 500;
        color: #e2e4ed;
        margin-top: 1.2rem;
        margin-bottom: 0.4rem;
        letter-spacing: 0.03em;
    }}
    
    .cozy-meta {{
        font-size: 0.9rem;
        color: #9da0b0;
        font-family: monospace;
        letter-spacing: 0.05em;
    }}

    /* Custom Input Fields Styling */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {{
        background-color: rgba(10, 10, 15, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0.8rem !important;
        transition: all 0.3s ease;
    }}
    
    div[data-baseweb="input"]:focus-within, div[data-baseweb="textarea"]:focus-within {{
        border-color: rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.05) !important;
    }}

    /* Tab Customizations */
    button[data-baseweb="tab"] {{
        color: #8a8d9f !important;
        font-size: 1rem !important;
        transition: color 0.3s ease !important;
    }}
    
    button[data-baseweb="tab"][aria-selected="true"] {{
        color: #ffffff !important;
        border-bottom-color: #ffffff !important;
    }}

    /* Custom Cozy Notification Banners */
    .cozy-alert {{
        padding: 1rem;
        border-radius: 0.8rem;
        margin-top: 1rem;
        font-size: 0.95rem;
    }}
    .cozy-success {{
        background: rgba(40, 167, 69, 0.15);
        border: 1px solid rgba(40, 167, 69, 0.3);
        color: #a3e2ab;
    }}
    .cozy-warning {{
        background: rgba(220, 53, 69, 0.15);
        border: 1px solid rgba(220, 53, 69, 0.3);
        color: #f1aeb5;
    }}
    </style>
    <div class="overlay"></div>
    """
    st.markdown(css, unsafe_allow_html=True)


# ---------- Load entries ----------
entries = load_entries()
entries_sorted = sorted(entries, key=lambda e: e["date"], reverse=True)

# ---------- Sidebar: Diary navigation ----------
with st.sidebar:
    st.markdown("### 📚 Past Pages")
    if entries_sorted:
        options = [
            f'{e["date"]} — {e["one_liner"][:25]}{"..." if len(e["one_liner"]) > 25 else ""}'
            for e in entries_sorted
        ]
        selected_label = st.selectbox("Flip back to a day", options, index=0)
        selected_index = options.index(selected_label)
        selected_entry = entries_sorted[selected_index]
    else:
        st.info("Your diary pages are empty right now.")
        selected_entry = None

    st.markdown("---")
    st.caption("Take your time. Reflection cannot be rushed.")


# ---------- Dynamic Theme Management ----------
theme = get_theme(st.session_state.current_rating)
set_background(theme["background"], theme["overlay"])

# ---------- Main layout ----------
container = st.container()
with container:
    slow_render(0.35)
    st.markdown('<div class="cozy-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="cozy-title">Cozy Journal</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="cozy-sub">A quiet space to capture what numbers cannot track.</div>',
        unsafe_allow_html=True
    )
    with col2:
        today_str = date.today().strftime("%A, %d %B")
        st.markdown(
            f'<div style="text-align:right; margin-top:0.6rem;" class="cozy-meta">{today_str}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    tab_write, tab_read = st.tabs(["✍️ Today’s Page", "📖 Open an Entry"])

    # ---------- Tab: Write ----------
    with tab_write:
        st.markdown('<div class="cozy-label">How warm or heavy did today feel?</div>', unsafe_allow_html=True)

        rating_col, _ = st.columns([2, 1])
        with rating_col:
            rating = st.slider(
                "Day rating",
                min_value=1,
                max_value=5,
                value=st.session_state.current_rating,
                help="1 is stormy/foggy, 5 is a warm glowing room.",
                label_visibility="collapsed"
            )
        
        # Trigger an immediate visual refresh if the selector moves
        if rating != st.session_state.current_rating:
            st.session_state.current_rating = rating
            st.rerun()

        st.markdown(
            '<div class="cozy-label">Today felt like…</div>',
            unsafe_allow_html=True,
        )
        one_liner = st.text_input(
            "One liner",
            placeholder="a quiet reset after chaos...",
            label_visibility="collapsed",
        )

        st.markdown(
            '<div class="cozy-label">Pour out your thoughts</div>',
            unsafe_allow_html=True,
        )
        entry_text = st.text_area(
            "Full entry",
            height=200,
            placeholder="Unwind here. There are no patterns to analyze or things to secure. Just write...",
            label_visibility="collapsed",
        )

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.button("Close and seal today’s page", type="primary")

        if submitted:
            if not one_liner.strip() or not entry_text.strip():
                st.markdown(
                    '<div class="cozy-alert cozy-warning">Take a brief moment to fill out both fields before sealing.</div>',
                    unsafe_allow_html=True
                )
            else:
                new_entry = {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "rating": int(rating),
                    "one_liner": one_liner.strip(),
                    "entry": entry_text.strip(),
                }
                save_entry(new_entry)
                st.markdown(
                    '<div class="cozy-alert cozy-success">Your thoughts have been safely put away. It\'s tucked into your history.</div>',
                    unsafe_allow_html=True
                )
                st.balloons()

    # ---------- Tab: Read ----------
    with tab_read:
        if selected_entry:
            st.markdown(f"### {selected_entry['one_liner']}")
            st.markdown(f"<div class='cozy-meta' style='margin-bottom:1rem;'>Logged on {selected_entry['date']} • {'⭐' * selected_entry['rating']}</div>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(
                f"<div style='white-space:pre-wrap; line-height:1.8; color:#e2e4ed; font-size:1.05rem;'>{selected_entry['entry']}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.info("Once you finish your first entry, you can flip open past pages here.")

    st.markdown("</div>", unsafe_allow_html=True)
