import streamlit as st
st.set_page_config(layout="wide")
from PIL import Image
st.title("Social Media and the Curve")
st.subheader('Matthew Jehrio')


st.text('Introduction: Flattening the curve is a critical aspect of managing an epidemic. When')
st.text('hospitals are put over a critical amount of stress at any particular time, limited ')
st.text('resources can be spread thin enough to disrupt care and cause diststrous results for')
st.text('patient care, but also for the well being of healthcare staff as well.')
st.text('')
st.text('To this end taking measures to prevent disease transmission is of critical importance')
st.text('not only for the sake of preventing the spread of disease directly, but also to avert')
st.text('a catastrophic situation in which hospitals are overwhelmed by a particular spike in')
st.text('the infection curve. With social distancing, masking, and basic hygeine being our')
st.text('strongest defense against he transmission of the novel coronavirus before the development')
st.text('of the vaccines, a significant social responsibility of protecting the public lies with')
st.text('individuals and their willingness to comply with public health meaasures. Drawing on the')
st.text('Health Belief Model from public health resources, the volition of individuals to practice')
st.text('infection control procedures derives from the individuals perception of the threat posed,')
st.text('as well as the perceived benefits of compliance, among others. This report looks at')
st.text('both the extent to which different localities were effective in flattening the infection')
st.text('curve. This report also takes an exploratory approach to examining the roles and associations')
st.text('of elected officials activity on social media and the possible effect it has on compliance')
st.text('with public health infection control guidance')
st.text('')
st.text('Part 1: The Curve')
st.text('')
st.text('Data on daily covid-19 infections was gathered on a county level basis from 2020-01-22 to')
st.text('2020-05-07. Due to the fact that, at the time this data was collected and when this report')
st.text('was written, the coronavirus epidemic was an evolving situation, there will be some important')
st.text('caveats attached to the results presented here. To measure each counties effectiveness at')
st.text('flattening the curve, and thus reducing transmission rates the maximum value of the daily')
st.text('increase in infections, adjusted for population size was used.')
st.latex(r'''Maximum\ Differential = argmax(\frac{County\ Daily\ Incidence\ Rate}{County\ Population})\ \forall\ dates\ in\ time\ range  ''')
st.text('')
st.text('The following figure shows the maximum differential for each county in the US')
st.text('')
#st.image(".\\choropleth_2.png")
st.image('maximum_differentials.png')
st.text('')
st.text('And the following tool allows you to examine the individual changes per county on a day to day basis. The title is')
st.text('currently an artifact and will be fixed shortly.')
st.text('')

day_number = st.slider("Day Number: ",2,93)
st.text("")
fig_file = "jpeg_choropleth_" +str(day_number)+".png"
fig_file = fig_file.strip()
st.image(fig_file)

st.write('')
st.write('Of particular note here is that While there are clusters that correspond to population centers,')
st.write('there are counties that appear to have increased maximum daily increases in spite of population.')
st.write('')
st.write('')
st.write('')
st.subheader('Part 2: Social Media')
st.write('')
st.write('The second part of this report utilizes exploratory methods to investigate the potential role that')
st.write('social media may play in the adoption of preventative public health measures. In particular, this')
st.write('report focuses on the social media accounts of public officials, and governors in particular. To do')
st.write('this, twitter data was gathered from the governors of all 50 states as of May 2020.')
st.write('')
st.write('Due to the nature of textual data, preprocessing was necessary. Punctuation was stripped away and')
st.write('capitalization was removed. Additionally, in the english language, many words such as "the", "a",')
st.write('"that", etc. are frequently used in conversation, but dont really denote any information of substance')
st.write('In natural language processing and text mining, these are known as stop words. For this reason, these')
st.write('words are also removed from the text corpus.')
st.write('')
st.write('This report implements the apriori algorithm to model the associations in each governors twitter feed')
st.write('The apriori algorithm is an unsupervised model that is used to learn associations between items that')
st.write('are bundled together, like figuring out which items are most likely to be bought together at a store.')
st.write('Here, the market baskets, or collections of items, are the governors individual tweets, and the goal')
st.write('is to assess which phrases different governors in different states, especially ones who were less')
st.write('successful at flattening the curve, were most likely to use. Furthermore, this report seeks to identify')
st.write('any trends that may exist between states to see if there may be a relationship between social media')
st.write('accounts of elected officials and effectiveness at flattening the curve.')
st.write('')
st.write('To this end the data needs to be preprocessed further by using word2vec. This process represents tweets')
st.write('as numerical vectors so that the apriori algorithm can be used.')
st.write('')
st.write('As a first step, lets visualize the relative frequencies of the words used by the governors to get a')
st.write('sense of what this data looks like:')
st.write('')
items_select = st.selectbox('Choose Governor',["charlie_baker_ma","andrew_cuomo_ny","brad_little_id","brian_kemp_ga","chris_sununu_nh","doug_ducey_az","gavin_newsom_ca","greg_abbott_tx","gretchen_whitmer_mi","john_bel_edwards_la","phil_murphy_nj","ron_desantis_fl","steven_bullock_mt"])
item_file = "item_counts_" + str(items_select)+ ".jpeg"
item_file = item_file.strip()
st.image(item_file)
