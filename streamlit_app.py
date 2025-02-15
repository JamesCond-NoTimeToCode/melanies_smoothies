# Import python packages
import streamlit as st

cnx = st.connection('snowflake')
session = cnx.session()

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """choose the fruits you want in your custom smoothie! :apple: :pineapple:
    """
)

import streamlit as st

    ##option = st.selectbox("what is your favorite fruit",("Banana", "Strawberries", "peaches"), )
    
    ##st.write("your favorite fruit is:", option)


from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col('Fruit_Name'))
##st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "choose upto 5 ingredients",
    my_dataframe 
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text (ingredients_list)
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    #st.write (ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)

    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")





         
