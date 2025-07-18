import streamlit as st
from PIL import Image

st.title("CheckMyCar.AI – Fahrzeug-Schadenanalyse (Prototyp)")

st.markdown("""
🚗 **Willkommen zur Demo-App!**  
Lade ein Fahrzeugbild hoch, um visuelle Schäden erkennen zu lassen (Beta-Version).  
In der finalen Version wird eine KI automatisch Schäden markieren & beschreiben.
""")

uploaded_file = st.file_uploader("📸 Fahrzeugfoto hochladen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Hochgeladenes Fahrzeugbild', use_column_width=True)
    
    st.success("✅ Bild erfolgreich hochgeladen.")
    st.info("🧠 KI-Analyse folgt in der nächsten Version...")

else:
    st.warning("Bitte lade ein Bild hoch.")
