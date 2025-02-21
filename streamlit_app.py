import streamlit as st
import df

st.title("Maricopa Native Seed Library at CNUW")
st.markdown(
    "Check out the the plant seeds the **Center for Native and Urban Wildlife** currently has available!"
)

qry = ''

search_criteria = st.toggle("View all Native Seeds", value=False)

start_search = False

if search_criteria == False:
    with st.container(border=True):
        st.header("Find Native Plants")
        st.text("Answer a few questions to find a plant that suits what you want!")
        
        st.write("---")

        # SEED TYPE CRITERIA
        st.subheader("What type of plant do you want?")
        all_seed_types = st.checkbox("Any type of plant is fine", False)
        if all_seed_types == True:
            qry += ''
        else: 
            seed_type = st.selectbox("Select a type of plant", df.seed_types_options, index=None, placeholder='Select Type')

            if seed_type == None:
                qry += ''
            elif qry == '':
                qry += 'Type == "' + seed_type + '"'
            elif qry != '':
                qry += ' and Type == "' + seed_type + '" '

        st.write("---")

        # SEED DIFFICULTY CRITERIA
        st.subheader("How experienced are you with gardening?")
        seed_difficulty = st.selectbox("Select your experience level", ["Beginner - None or limited experience", "Intermediate - Average experience", "Pro - Very experienced"], index=None, placeholder="Select Gardening Experience Level")

        if seed_difficulty == "Beginner - None or limited experience":
            difficulty = ['Easy']
        elif seed_difficulty == "Intermediate - Average experience":
            difficulty = ['Easy', 'Medium']
        elif seed_difficulty == "Pro - Very experienced":
            difficulty = ['Easy', 'Medium', 'Difficult', 'Unknown']

        if seed_difficulty == None:
            qry += ''
        elif qry == '':
            qry += 'Difficulty in ' + f'{difficulty}' + ''
        elif qry != '':
            qry += ' and Difficulty in ' + f'{difficulty} ' + ''

        st.write("---")

        # SEED SUN AMOUNT CRITERIA
        st.subheader("How much sunlight can the plant(s) get in your home garden?")

        all_seed_sun_amt = st.checkbox("I can work with either full sun or part shade plants", False)
        if all_seed_sun_amt == True:
            qry += ''
        else: 
            sun_amt = st.selectbox("Select sunlight", ["Full Sunlight Only", "Full or Partial Sunlight", "Partial Sunlight Only"], index=None, placeholder='Select Sunlight Amount')

            if sun_amt == "Full Sunlight Only":
                sun_amt_selected = ['Full']
            elif sun_amt == "Full or Partial Sunlight":
                sun_amt_selected = ['Full or Partial']
            elif sun_amt == "Partial Sunlight Only":
                sun_amt_selected = ['Partial']

            if sun_amt == None:
                qry += ''
            elif qry == '':
                qry += 'SumAmt in ' + f'{sun_amt_selected}' + ''
            elif qry != '':
                qry += ' and SunAmt in ' + f'{sun_amt_selected}' + ''

        st.write("---")

        # SEED WATER AMOUNT CRITERIA
        st.subheader("Do you want a high water maintenance or low water maintenance plant?")

        all_seed_water_amt = st.checkbox("I can work with any water maintenance level", False)
        if all_seed_water_amt == True:
            qry += ''
        else: 
            water_amt = st.selectbox("Select water maintenance level", ["High Water Maintenance", "Moderate to High Water Maintenance", "Moderate Water Maintenance", "Low to Moderate Water Maintenance", "Low Water Maintenance", "Very Low Water Maintenance"], index=None, placeholder="Select Maintenance Level")

            if water_amt == "High Water Maintenance":
                water_amt_selected = ['High']
            elif water_amt == "Moderate to High Water Maintenance":
                water_amt_selected = ['Moderate to High']
            elif water_amt == "Moderate Water Maintenance":
                water_amt_selected = ['Moderate']
            elif water_amt == "Low to Moderate Water Maintenance":
                water_amt_selected = ['Low to Moderate']
            elif water_amt == "Low Water Maintenance":
                water_amt_selected = ['Low']
            elif water_amt == "Very Low Water Maintenance":
                water_amt_selected = ['Very Low']

            if water_amt == None:
                qry += ''
            elif qry == '':
                qry += 'WaterAmt in ' + f'{water_amt_selected}' + ''
            elif qry != '':
                qry += ' and WaterAmt in ' + f'{water_amt_selected}' + ''

        if st.button("Search", type='primary'):
            if qry == '':
                st.warning("Search criteria can't be empty! Please answer select from at least one dropdown list.")
            else: 
                start_search = True

elif search_criteria == True:
    qry = ''    
    

# display seed profiles    
with st.container():
    info_slot = st.empty()

    seed_profiles = df.get_filtered_profiles(qry)
    num_of_profiles = len(seed_profiles)
    total_profiles = len(df.seed_profiles_df)
    num_of_profile_columns = 2
    rows = df.create_seed_profile_columns(seed_profiles, num_of_profile_columns)

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

                    st.image(profile.loc['Img'])
                    st.markdown(f"<p style='text-align: center;'>{profile.loc['Author']}<p>", unsafe_allow_html=True)

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

    if search_criteria == True:
        with info_slot.container():
            st.warning("Search Criteria cleared. Viewing all available native seed packets.")
            st.caption(f"Showing {num_of_profiles} out of {total_profiles} native seed packets")
        qry = ''
        create_rows()

    elif search_criteria == False and start_search == True:
        with info_slot.container():
            if num_of_profiles == 0:
                st.warning("Sorry, we don't have native seed plants for your specific search right now. Edit your search to check out something else!")
            st.caption(f"Showing {num_of_profiles} out of {total_profiles} native seed packets")
        create_rows()

    