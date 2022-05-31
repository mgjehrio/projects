import streamlit as st
import base64


st.set_page_config(page_title="Matthew Jehrio Poster App",
    page_icon="central_poster_graphic.svg",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)




state = st.sidebar.selectbox('Page', ['Poster', 'Paper'])


def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



if state == "Poster":

        st_display_pdf("C:\\Users\\mgjeh\\Downloads\\Matthew_Jehrio_Poster_1.pdf")
elif state == "Paper":
        st_display_pdf("manuscript.pdf")

