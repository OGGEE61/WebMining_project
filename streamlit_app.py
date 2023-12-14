import streamlit as st
import temp

# Mock function to fetch city information using an API
def fetch_city_info(city_name):
    # Implement your API fetching logic here
    return f"Information about {city_name} from API"

#Layout
st.set_page_config(
    page_title="City Information App",
    layout="wide",
    initial_sidebar_state="collapsed")

st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

def display_city_details(city_name, temperature):
    st.subheader(f"City: {city_name}, Temperature: {temperature}°C")
    
    # Container for attractions
    st.write("Attractions:")
    # Add code here
    
    # Container for hotels
    st.write("Hotels:")
    # Add code here 
    
    # Container for flights
    st.write("Flights:")
    # Add code here 

def display_city_temperature(city_data):
    for city, temperature in city_data.items():
        if st.button(f"City: {city}, Temperature: {temperature}°C"):
            display_city_details(city, temperature)  # Display details for the selected city

def display_hot_cities():
    st.write("Displaying information for hot cities:")
    hot_city_data = temp.get_city_data("hot")  # Get hot city data
    if hot_city_data:
        display_city_temperature(hot_city_data)
        if st.button("Go back"):
            st.session_state.page = "Main Page"

def display_cold_cities():
    st.write("Displaying information for cold cities:")
    cold_city_data = temp.get_city_data("cold")  # Get cold city data
    if cold_city_data:
        display_city_temperature(cold_city_data)
        if st.button("Go back"):
            st.session_state.page = "Main Page"
def main():
    st.title("City Information App")
    
    # Sidebar navigation with bigger buttons
    st.sidebar.header("Navigation")
    if st.sidebar.button("Main Page", key="main_button"):
        st.session_state.page = "Main Page"
    if st.sidebar.button("About", key="about_button"):
        st.session_state.page = "About"

    # Set default page as Main Page
    if "page" not in st.session_state:
        st.session_state.page = "Main Page"

    st.divider()

    if st.session_state.page == "Main Page":
        st.header("Choose between Hot or Cold")
        # Buttons for selecting hot or cold in one line
        col1, col2 = st.columns(2)
        with col1:
            hot_selected = st.button("Hot 🔥",  key="hot_button")
        with col2:
            cold_selected = st.button("Cold ❄️",  key="cold_button")
        
        st.divider()
        
        if hot_selected:
            display_hot_cities()
        elif cold_selected:
            display_cold_cities()


    elif st.session_state.page == "About":
        st.header("About the Project")
        st.write("This app displays information about cities based on your selection of hot or cold.")
        # Add more information about the project here if needed

if __name__ == "__main__":
    main()
