import streamlit as st
from groq import Groq

# 1. Nastavení vzhledu (To, co uvidíš v mobilu)
st.set_page_config(page_title="SÍTO v1.0", layout="centered")

st.title("🛡️ SÍTO")
st.subheader("Geniální jednoduchost")

# 2. Vstupní pole
input_text = st.text_area("Vlož text k přežvýkání:", placeholder="Sem vlož ten chaos...", height=200)

# 3. Tlačítko pro akci
if st.button("VYČISTIT (SÍTO)"):
    if input_text:
        try:
            # Tady se napojíme na tvůj Groq (klíč vložíme později do schovky)
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            completion = client.chat.completions.create(
                model="llama-3.3-70b-specdec",
                messages=[
                    {"role": "system", "content": "Jsi Síto. Tvůj úkol je vzít text a vytáhnout z něj jen to podstatné. Odstraň omáčku, zdvořilosti a balast. Buď stručný a geniálně jednoduchý."},
                    {"role": "user", "content": input_text}
                ]
            )
            
            # 4. Výstupní pole
            st.success("Tady máš vyčištěné jádro:")
            st.write(completion.choices[0].message.content)
            
        except Exception as e:
            st.error(f"Něco se zaseklo (klasika): {e}")
    else:
        st.warning("Nejdřív tam musíš něco hodit!")
