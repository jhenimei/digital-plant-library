import streamlit as st
import df

st.title("Maricopa Native Seed Library at CNUW")
st.markdown(
    "Check out the the plant seeds the **Center for Native and Urban Wildlife** currently have available!"
)

qry = ''
search_criteria = True

if st.button("View All Available Plant Seeds", type='primary'):
    search_criteria = False
    qry = ''

with st.popover("Search Specific Plant Seeds"):
    search_criteria = True
    # SEED TYPE CRITERIA
    all_seed_types = st.checkbox("View All Available Seed Types", False)
    if all_seed_types == True:
        qry += ''
    else: 
        seed_type = st.selectbox("What **type** of plant(s) are you looking for?", df.seed_types_options, index=None, placeholder='Select Type')

        if seed_type == None:
            qry += ''
        elif qry == '':
            qry += 'Type == "' + seed_type + '"'
        elif qry != '':
            qry += ' and Type == "' + seed_type + '" '

    # SEED DIFFICULTY CRITERIA
    all_seed_difficulties = st.checkbox("View All Available Seeds for Any Gardening Experience Level", False)
    if all_seed_difficulties == True:
        qry += ''
    else: 
        seed_difficulty = st.selectbox("How experienced are you with gardening?", ["Beginner - None or limited experience", "Intermediate - Average experience", "Pro - Very experienced"], index=None, placeholder="Select Gardening Experience Level")

        if seed_difficulty == "Beginner - None or limited experience":
            difficulty = ['Easy']
        elif seed_difficulty == "Intermediate - Average experience":
            difficulty = ['Easy', 'Medium']
        elif "Pro - Very experienced":
            difficulty = ['Easy', 'Medium', 'Difficult', 'Unknown']

        if seed_difficulty == None:
            qry += ''
        elif qry == '':
            qry += 'Difficulty in ' + f'{difficulty}' + ''
        elif qry != '':
            qry += ' and Difficulty in ' + f'{difficulty} ' + ''

    # SEED SUN AMOUNT CRITERIA
    all_seed_sun_amt = st.checkbox("View All Available Seeds for Any Amount of Sunlight", False)
    if all_seed_sun_amt == True:
        qry += ''
    else: 
        sun_amt = st.selectbox("How much sunlight can the plant(s) get in your home garden?", df.seed_sun_amt_options, index=None, placeholder='Select Sun Amount')

        if sun_amt == None:
            qry += ''
        elif qry == '':
            qry += 'SunAmt == "' + sun_amt + '"'
        elif qry != '':
            qry += ' and SunAmt == "' + sun_amt + '" '  

    # SEED WATER AMOUNT CRITERIA
    all_seed_water_amt = st.checkbox("View All Available Seeds for Any Amount of Water", False)
    if all_seed_water_amt == True:
        qry += ''
    else: 
        water_amt = st.selectbox("How much water can you provide the plant(s) on average?", df.seed_water_amt_options, index=None, placeholder="Select Water Amount")

        if water_amt == None:
            qry += ''
        elif qry == '':
            qry += 'WaterAmt == "' + water_amt + '"'
        elif qry != '':
            qry += ' and WaterAmt == "' + water_amt + '" '

    if st.button("Search", type='primary'):
        None

# display seed profiles    
with st.container():
    seed_profiles = df.get_filtered_profiles(qry)
    num_of_profiles = len(seed_profiles)
    total_profiles = len(df.seed_profiles_df)
    num_of_profile_columns = 2
    rows = df.create_seed_profile_columns(seed_profiles, num_of_profile_columns)

    st.caption(f"Showing {num_of_profiles} out of {total_profiles} native seed packets")

    profile_columns = st.columns(num_of_profile_columns)

    def add_row(row):
        for col in profile_columns:
            index = row * num_of_profile_columns + profile_columns.index(col)

            if index < num_of_profiles: 
                profile = seed_profiles.iloc[index]

                with col.container(border=True):
                    profile_id = profile.loc['Seed ID']
                    st.subheader(profile.loc['Common Name'])
                    st.markdown(f"*{profile.loc['Botanical Name']}*")
                    st.markdown(f"""
                                    **Type:** {profile.loc['Type']}
                                    <br>
                                    **Germination Difficulty:** {profile.loc['Difficulty']}
                                    """, unsafe_allow_html=True)
                    st.markdown(f"""**CARE INFORMATION** 
                                    <br>
                                    **Sun Amount:** {profile.loc['SunAmt']}
                                    <br>
                                    **Water Amount:** {profile.loc['WaterAmt']}
                                    """, unsafe_allow_html=True)
                    
    def create_rows():
            for row in range(rows):
                add_row(row)

    if search_criteria == False and qry != '':
        st.warning("Search Criteria cleared. Viewing all available native seed packets.")
        create_rows()

    elif search_criteria == True:
        create_rows()
        df.full_seed_profiles_df
        