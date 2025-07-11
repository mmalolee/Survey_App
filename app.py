import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(':handshake: Welcome Survey Analysis :handshake:')

df = pd.read_csv('data_prepared.csv', sep=';')

# Creating tabs
t_metr, t_visual = st.tabs(['Metrics', 'Charts'])

# Creating sidebar with filters
with st.sidebar:

    st.header('Filters')
    
    # Gender filtering
    gend = st.radio('Gender', ['All', 'Females', 'Males'])
    if gend == 'All': df = df
    elif gend == 'Females': df = df[df['gender'] == 'Female']
    elif gend == 'Males': df = df[df['gender'] == 'Male']

    age = st.multiselect('Age range', sorted(df['age'].unique()), default=[])
    if age == []: df = df
    else: df = df[df['age'].isin(age)]

    # Education level filter
    st.write('Education')
    edu_filter = []
    c0, c1, c2 = st.columns(3)
    with c0: 
        primary_filter = st.checkbox('Primary', value=True)
        if primary_filter: edu_filter.append('Primary')
    with c1: 
        secondary_filter = st.checkbox('Secondary', value=True)
        if secondary_filter: edu_filter.append('Secondary')
    with c2: 
        college_filter = st.checkbox('College', value=True)
        if college_filter: edu_filter.append('College')
    df = df[df['edu_level'].isin(edu_filter)]

    # Favourite animal filter
    fav_animal = st.multiselect('Favourite animal', df['fav_animals'].unique(), default=[])
    if fav_animal:
        df = df[df['fav_animals'].isin(fav_animal)]

    # Taste filter
    sweet_or_salty = st.radio('Taste', ['All', 'Sweet', 'Salty', 'No data'])
    if sweet_or_salty == 'All': df = df
    elif sweet_or_salty == 'Sweet': df = df[df['sweet_or_salty'] == sweet_or_salty]
    elif sweet_or_salty == 'Salty': df = df[df['sweet_or_salty'] == sweet_or_salty]
    else: df = df[df['sweet_or_salty'] == sweet_or_salty]
    
    # Favourite place filter
    fav_place = st.multiselect('Favourite place', df['fav_place'].unique(), default=[])
    if fav_place:
        df = df[df['fav_place'].isin(fav_place)]

# Metrics tab  
with t_metr:

    c0, c1 = st.columns(2)

    with c0:
        st.header('Five or less random rows')
    with c1:
        x = st.button('Draw', use_container_width=True)

    st.dataframe(df.sample(min(5, len(df))), hide_index=True, use_container_width=True)

    c0, c1, c2, c3 = st.columns(4)

    with c0:
        st.metric('Number of participants', len(df))
    with c1:
        st.metric('Females', len(df[df['gender'] == 'Female']))
    with c2:
        st.metric('Males', len(df[df['gender'] == 'Male']))
    with c3:
        st.metric('No data', len(df[df['gender'] == 'No data']))

    c0, c1 = st.columns([1,2])
    
    with c0:
        st.dataframe(df['fav_animals'].value_counts().nlargest(3))
    with c1:
        st.header(':dog: Most popular animals among interviewed :dog:')

    if df.empty: st.error('No data')
    else: st.success('Filtering completed successfully') 

# Charts tab
with t_visual:
    c0, c1, c2 = st.columns([1, 5, 1])
    with c1:
        with st.expander('Gender'):
            if df.empty:
                st.warning('Not enough data')
            else:
                fig1, ax1 = plt.subplots()
                df['gender'].value_counts().plot(kind='pie', 
                                                    autopct='%.1f',
                                                    ax=ax1,
                                                    textprops={'color':'white'},
                                                    title='Percent distribution of gender',
                                                    legend=True,
                                                    fontsize=20,
                                                    ylabel='')
                st.pyplot(fig1)  
           
        with st.expander('Age'):
            if df.empty:
                st.warning('Not enough data')
            else:
                fig1, ax1 = plt.subplots()
                plt.title('Age histogram')
                plt.ylabel('Age count')
                plt.xlabel('Age')
                sns.histplot(data=df, x='age', color='g')
                st.pyplot(fig1)

        with st.expander('Education level'):
            if df.empty:
                st.warning('Not enough data')
            else:
                fig1, ax1 = plt.subplots()
                sns.countplot(data=df, x='edu_level', hue='gender', stat='percent', saturation=0.8, ax=ax1)
                plt.xlabel('Education level')
                plt.ylabel('Percentage')
                plt.title('Education level among females and males')
                plt.legend(title='Gender')
                st.pyplot(fig1)
                fig1, ax1 = plt.subplots()
                sns.countplot(data=df, x='edu_level', hue='age', stat='percent', saturation=0.8, ax=ax1)
                plt.ylabel('Percentage')
                plt.xlabel('Education level')
                plt.title('Education level distribution according to age')
                st.pyplot(fig1)

        with st.expander('Favourite animals'):
            if df.empty:
                st.warning('Not enough data')
            else:
                fig1, ax1 = plt.subplots()
                plt.title('Favourite animal histogram')
                plt.ylabel('Animal count')
                plt.xlabel('Age')
                plt.legend(title='Gender')
                sns.histplot(data=df, x='fav_animals', color='b', hue='gender')
                st.pyplot(fig1)
            
        with st.expander('Taste'):
            if df.empty:
                st.warning('Not enough data')
            else:            
                fig1, ax1 = plt.subplots()
                plt.xlabel('Taste')
                plt.ylabel('Percentage')
                plt.title('Taste preferences distribution')
                plt.legend(title='Gender') 
                sns.countplot(data=df, x='sweet_or_salty', hue='gender', stat='percent', saturation=0.8, ax=ax1)
                st.pyplot(fig1)

        with st.expander('Favourite place'):
            if df.empty:
                st.warning('Not enough data')
            else:            
                fig1, ax1 = plt.subplots()
                plt.title('Places histogram')
                plt.ylabel('Place count')
                plt.xlabel('Place')
                plt.legend(title='Gender')
                sns.histplot(data=df, x='fav_place', color='g', hue='gender', ax=ax1)
                st.pyplot(fig1)