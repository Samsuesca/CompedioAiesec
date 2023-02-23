import streamlit as st
from datetime import date
import locale
# # Configura el idioma y la localización
# locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

# Set page config
st.set_page_config(page_title="COMPEDIO AIESEC", page_icon=":owl:", initial_sidebar_state="expanded")

today = date.today().strftime("%B %d del %Y")
def title(text,size=50):
    st.markdown(f'<h1 style="text-align: center;font-size: {size}pt;">{text}</h1>',
             unsafe_allow_html=True)

def text(text,size=16,align='center'):
    st.markdown(
    f"""
    <p style="text-align: {align};font-size:{size}pt; text-justify: inter-word;">
        {text}
    </p>
    """,
    unsafe_allow_html=True,)


st.write('---')

# Portada
title('Bienvenidos al Compendio EAFIT')
text('Espacio de gobernabilidad')
text(today.title(), 16)

st.write('---')

# Sección 1: Qué es Gobernabilidad
title('¿Qué es Gobernabilidad?')
text('Participación en espacios formales de asamblea y asociados')
st.write('---')

# Sección 2: Qué son las Asambleas
title('¿Qué son las Asambleas?')
text('Son espacios legislativos donde se dan a conocer y aprobar temas como gestión de la EB, solicitudes de alumni, cambios de compendio, presupuesto, entre otros.')
text('Las asambleas pueden ser ordinarias y extraordinarias.')
text('En las asambleas votan para aprobar o reprobar las personas que tienen pleno derecho, lo que se gana con criterios como performance superior al 80%, haber asistido a las dos asambleas ordinarias inmediatamente anteriores, entre otros.')
st.write('---')

# Agregar imagen a la sección
c1,c2,c3 = st.columns([1,3,7])
with c2:
    st.image('aiesec.png', width=600)
st.write('---')

# Sección 3: Qué es el Compendio
title('¿Qué es el Compendio?')
text('CONTENIDO DEL COMPENDIO')
text('Título I: Compendio Local')
text('Capítulo 1: Generalidades')
text('Artículo 1: Nombre')
text('Artículo 2: Naturaleza')
text('Artículo 3: Misión')
text('Artículo 4: Visión')
text('Artículo 5: Objetivo')
text('Parágrafo 1')
text('Parágrafo 2')
text('Artículo 6: Valores Organizacionales')
st.write('---')
# Agregar imagen a la sección
c1,c2,c3 = st.columns([1,3,7])
with c2:
    st.image('compedio.jpeg', width=600)
st.write('---')

# Sección 4: Actividad Grupal
title('Actividad Grupal')
text('Crear algo que resuma el espacio en sus propias palabras y exponer. Puede ser a mano o presentar en la computadora.')
st.write('---')