import streamlit as st
import df

# WEBSITE INFORMATION
# title
st.title("Find an Arizona-Native Plant!")

# description
site_description = '''Check out all or find a plant that is right for you and is native to Arizona so you can support our wildlife!

The plants in this website can be obtained as seeds from the **Maricopa Native Seed Library** at Scottsdale Community College's **Center for Native and Urban Wildlife** (CNUW).'''

st.markdown(site_description)

st.warning("Site is currently undergoing maintenance. Some features may not work correctly. We will be fixed by March 5th, thank you for your patience!")


# INITIALIZING VARIABLES
# for finding plants query
qry = ''
get_filtered_profiles = ''
# for checking open tab
search_criteria = False
view_all = False
# for when to run search
start_search = False

# WEBSITE TABS/SECTIONS
find_plants_tab, all_plants_tab = st.tabs(["Find a Native Plant", "View all Native Plants"])


# FIND PLANTS TAB CONTENT
with find_plants_tab:

    # SEARCH FORM AREA
    with st.container(border=True):
        # SEARCH FORM INFORMATION
        st.header("We'll help you look for the best native plant for you.")
        st.text("To get started, just fill in the blanks!")

        # divider
        st.write("---")

        # PLANT CRITERIA
        # type criteria
        plant_type = st.selectbox("The type of plant I am looking for is...", ["an annual", "a grass", "a groundcover", "a perennial", "a shrub", "a subshrub", "a tree", "a vine", "any type of plant"], index=None, placeholder="Select a Plant Type")

        # gets plant type value for filter
        if plant_type == "an annual":
            type_value = 'Annual'
        elif plant_type == "a grass":
            type_value = 'Grass'
        elif plant_type == "a groundcover":
            type_value = 'Groundcover'
        elif plant_type == "a perennial":
            type_value = 'Perennial'
        elif plant_type == "a shrub":
            type_value = 'Shrub'
        elif plant_type == "a subshrub":
            type_value = 'Subshrub'
        elif plant_type == "a tree":
            type_value = 'Tree'
        elif plant_type == "a vine":
            type_value = 'Vine'
        elif plant_type == "any type of plant":
            type_value = 'all'

        # creates query for plant type
        if plant_type == None or type_value == 'all':
            qry += ''
        elif qry == '':
            qry += 'Type == "' + type_value + '"'
        elif qry != '':
            qry += ' and Type == "' + type_value + '" '
        


        # size criteria
        plant_size = st.selectbox("I want the plant to grow in...", ["my garden, on the ground", "a container"], index=None, placeholder="Select where the plant will grow in")

        # gets plant size value for filter
        if plant_size == "my garden, on the ground":
            size_value = 'Large'
        elif plant_size == "a container":
            size_value = 'Small'

        # creates query for plant size
        if plant_size == None:
            qry += ''
        elif qry == '':
            qry += 'Size == "' + size_value + '"'
        elif qry != '':
            qry += ' and Size == "' + size_value + '" '


        # sun amount criteria
        plant_sun_amount = st.selectbox("I also prefer a plant that can handle...", ["full, direct sunlight", "partial sunlight and shade", "either full or partial sunlight"], index=None, placeholder="Select how much sun the plant will get")

        # gets plant sun amount value for filter
        if plant_sun_amount == "full, direct sunlight":
            sun_amount_value = 'Full'
        elif plant_sun_amount == "partial sunlight and shade":
            sun_amount_value = 'Partial'
        elif plant_sun_amount == "either full or partial sunlight":
            sun_amount_value = 'all'

        # creates query for plant sun amount
        if plant_sun_amount == None or sun_amount_value == 'all':
            qry += ''
        elif qry == '':
            qry += 'SunAmt == "' + sun_amount_value + '"'
        elif qry != '':
            qry += ' and SunAmt == "' + sun_amount_value + '" '


        # water amount criteria
        plant_water_amount = st.selectbox("and I would be able to provide the plant with...", ["moderate to high amount of water", "low to moderate amount of water", "very low to low amount of water", "any amount of water"], index=None, placeholder="Select how much water you can give")

        # gets plant water amount value for filter
        if plant_water_amount == "moderate to high amount of water":
            water_amount_value = ['High', 'Moderate to High', 'Moderate']
        elif plant_water_amount == "low to moderate amount of water":
            water_amount_value = ['Moderate', 'Low to Moderate', 'Low']
        elif plant_water_amount == "very low to low amount of water":
            water_amount_value = ['Low', 'Very Low']
        elif plant_water_amount == "any amount of water":
            water_amount_value = 'all'

        # creates query for plant water amount
        if plant_water_amount == None or water_amount_value == 'all':
            qry += ''
        elif qry == '':
            qry += 'WaterAmt in "' + water_amount_value + '"'
        elif qry != '':
            qry += ' and WaterAmt in "' + water_amount_value + '" '


        # wildlife benefit criteria
        plant_wildlife = st.selectbox("I also want the plant to be friendly to...", ["native bees", "hummingbirds", "butterflies", "any native wildlife"], index=None, placeholder="Select the native wildlife you want to attract")

        # gets plant wildlife value for filter
        if plant_wildlife == "native bees":
            plant_wildlife_value = 'Native Bees'
        elif plant_wildlife == "hummingbirds":
            plant_wildlife_value = 'Hummingbirds'
        elif plant_wildlife == "butterflies":
            plant_wildlife_value = 'Butterflies'
        elif plant_wildlife == "any native wildlife":
            plant_wildlife_value = 'all'

        # creates query for plant wildlife value
        if plant_wildlife == None or plant_wildlife_value == 'all':
            qry += ''
        elif qry == '':
            qry += 'WildlifeValue == "' + plant_wildlife_value + '"'
        elif qry != '':
            qry += ' and WildlifeValue == "' + plant_wildlife_value + '" '


        # experience level
        plant_difficulty = st.selectbox("My experience level with gardening is...", ["beginner - none or limited experience", "intermediate - average experience", "pro - very experienced"], index=None, placeholder="Select your gardening experience level")

        # gets plants difficulty level for filter
        if plant_difficulty == "beginner - none or limited experience":
            difficulty_value = ['Easy']
        elif plant_difficulty == "intermediate - average experience":
            difficulty_value = ['Easy', 'Medium']
        elif plant_difficulty == "pro - very experienced":
            difficulty_value = ['Easy', 'Medium', 'Difficult', 'Unknown']

        # creates query for plants difficulty value
        if plant_difficulty == None:
            qry += ''
        elif qry == '':
            qry += 'Difficulty in "' + difficulty_value + '"'
        elif qry != '':
            qry += ' and Difficulty in "' + difficulty_value + '" '


        # SEARCH BUTTON
        search_btn = st.button("Find my match!", type='primary')
        
        
        if search_btn:
            # to display plant profiles
            get_filtered_profiles = df.get_filtered_profiles(qry)

    filtered_profiles_slot = st.container()

    # CREATING PLANT PROFILES
    with filtered_profiles_slot:
        # for display notices
        filtered_info_slot = st.empty()

        # gets plant profiles 
        num_of_profiles = len(get_filtered_profiles)
        total_profiles = len(df.plant_profiles_df)

        # how profiles will display
        num_of_profile_columns = 2
        filtered_profile_rows = df.create_plant_profile_columns(get_filtered_profiles, num_of_profile_columns)

        # create profile columns
        filtered_profile_columns = st.columns(num_of_profile_columns)

        # function to add row
        def add_filtered_row(row):
            for col in filtered_profile_columns:
                index = row * num_of_profile_columns + filtered_profile_columns.index(col)

                if index < num_of_profiles:
                    filtered_profile = get_filtered_profiles.iloc[index]

                    # profile containers
                    with col.container(border=True):
                        profile_id = filtered_profile.loc['Plant ID']

                        # displays plant names
                        st.subheader(filtered_profile.loc['Common Name'])
                        st.markdown(f"*{filtered_profile.loc['Botanical Name']}*")

                        # displays plant image
                        st.image(filtered_profile.loc['Img'])
                        st.markdown(f"<p style='text-align: center;'>{filtered_profile.loc['Author']}<p>", unsafe_allow_html=True)

                        # displays plant information
                        st.markdown(f"""
                                        **Type:** {filtered_profile.loc['Type']}
                                        <br>
                                        **Germination Difficulty:** {filtered_profile.loc['Difficulty']}
                                        """, unsafe_allow_html=True)
                        st.markdown(f"""**CARE INFORMATION** 
                                        <br>
                                        **Sun Amount:** {filtered_profile.loc['SunAmt']}
                                        <br>
                                        **Water Amount:** {filtered_profile.loc['WaterAmt']}
                                        """, unsafe_allow_html=True)
        
        # function to add and create row
        def create_filtered_rows():
            for row in range(filtered_profile_rows):
                add_filtered_row(row)





# VIEW ALL PLANTS TAB
with all_plants_tab:
    
    get_all_profiles = df.get_filtered_profiles("")
    all_profiles_slot = st.container()

    # CREATING PLANT PROFILES
    with all_profiles_slot:
        # for display notices
        info_slot = st.empty()

        # gets plant profiles
        total_profiles = len(df.plant_profiles_df)

        # determines how profiles will display
        num_of_profile_columns = 2
        profile_rows = df.create_plant_profile_columns(get_all_profiles, num_of_profile_columns)

        # creates profile columns
        profile_columns = st.columns(num_of_profile_columns)

        # function to add row 
        def add_row(row):
            for col in profile_columns:
                index = row * total_profiles + profile_columns.index(col)

                if index < total_profiles:
                    profile = get_all_profiles.iloc[index]

                    # creates plant profile containers
                    with col.container(border=True):
                        profile_id = profile.loc['Plant ID']

                        # displays plant names
                        st.subheader(profile.loc['Common Name'])
                        st.markdown(f"*{profile.loc['Botanical Name']}*")

                        # displays plant image
                        st.image(profile.loc['Img'])
                        st.markdown(f"<p style='text-align: center;'>{profile.loc['Author']}<p>", unsafe_allow_html=True)

                        # displays plant information
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




        # function to add and create row
        def create_rows():
            for row in range(profile_rows):
                add_row(row)

# enables search to display plant profiles
with all_profiles_slot:
    create_rows()

    # creates notices
    with info_slot.container():
        st.info("Showing all avilable native plants")
        st.caption(f"Showing {total_profiles} Arizona-Native Plants")

if search_btn:
    with filtered_profiles_slot.container():

        # creates notices
        with filtered_info_slot.container():
            if num_of_profiles == 0:
                st.error("Sorry, we don't have any native plants that matches your requirements right now.")
            else: 
                st.info("Criteria updated. Showing you native plants that match your search.")
            st.caption(f"Showing {num_of_profiles} out of {total_profiles} Arizona-Native Plants")

        create_filtered_rows()


