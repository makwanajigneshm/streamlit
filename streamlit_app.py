import streamlit as sl
import pandas as p
sl.write("Hello")
sl.header("New World")
sl.text("Welcome to the party!")
my_fruit_list=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#sl.dataframe(my_fruit_list)
my_fruit_list=my_fruit_list.set_index("Fruit")
fruits_selected=sl.multiselect("Pick some Fruits",list(my_fruit_list.index),["Apple","Cantaloupe"])
sl.dataframe(my_fruit_list)
chosen_fruits=my_fruit_list.loc[fruits_selected]
sl.dataframe(chosen_fruits)



