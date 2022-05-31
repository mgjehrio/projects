import streamlit as st
import base64


st.set_page_config(page_title="Matthew Jehrio Poster App",
    page_icon="C:\\Users\\mgjeh\\Desktop\\thesis\\figures\\poster_graphics\\central_poster_graphic.svg",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)




state = st.sidebar.selectbox('Page', ['Poster', 'Paper', 'Figures'])


def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



if state == "Poster":

        st_display_pdf("C:\\Users\\mgjeh\\Downloads\\Matthew_Jehrio_Poster_1.pdf")
elif state == "Paper":
        st_display_pdf("C:\\Users\\mgjeh\\Desktop\\thesis\\manuscript.pdf")

if state == "Figures":

    # Histogram display input
        hist_case = st.selectbox('Isolation Strategy',['Infected', 'Susceptible'])
        hist_infections = st.selectbox('Number of Initial Infections',range(10,101,10) )
        hist_isolations = st.selectbox('Number of Isolations', range(5,101,5))
        hist_filename = f'{hist_infections}  Initial Infections,  {hist_isolations} Nodes Isolated'
        hist_string = f'C:\\Users\\mgjeh\\Desktop\\thesis\\companion_app\\app_figures\\histograms\\{hist_case.lower()}\\{hist_filename}.png'
        hist_string = hist_string.strip()
        st.write(hist_string)

        st.image("C:\\Users\\mgjeh\\Desktop\\thesis\\companion_app\\app_figures\\error_bar_plots\\infected\\jpg_infected_20_initial_infections.jpg")



        # Error bar plots
        errorbar_case = st.selectbox('Isolation Strategy',['Infected', 'Susceptible','Mixed'])
        errorbar__initial_infections = st.selectbox('Number of Initial Infections eb', range(20,101,10))
        errorbar_convert = f"C:\\Users\\mgjeh\\Desktop\\thesis\\companion_app\\app_figures\\error_bar_plots\\{errorbar_case.lower()}\\infected_{errorbar__initial_infections}_initial_infections.png"
        errorbar_convert = errorbar_convert.strip()
        st.write(errorbar_convert)
        st.image(errorbar_convert)
