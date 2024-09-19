# Import python packages
import streamlit as st
cnx=st.connection("snowflake")

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

import streamlit as st

option = st.selectbox(
    "name on smoothie",
    ("bettyjean"),
)

st.write("my smoothiw will be:", option)


from snowflake.snowpark.functions import col

session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    ,my_dataframe
)

if  ingredients_list:
    ingredients_string = ''

for fruit_chosen in ingredients_list:
    ingredients_string += fruit_chosen +''

#st.write(ingredients_string)

my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

#st.write(my_insert_stmt)
time_to_insert = st.button('Submit order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()


    st.success('Your Smoothie is ordered!', icon="✅")



