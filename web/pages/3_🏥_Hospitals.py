import streamlit as st
 
st.set_page_config(
    page_title="Hospitals",
    page_icon="🏥",
)

data = {
    'latitude': [30.579121999999995, 30.582869000000002, 30.553873000000003, 30.535321000000007, 30.517218000000028],
    'longitude': [114.26234900000009, 114.27413299999989, 114.353838, 114.298947, 114.41445299999998],
    'name': ['同济医院', '协和医院', '中南医院', '人民医院', '华中科技大学校医院']
}
 
st.map(data, use_container_width=True)