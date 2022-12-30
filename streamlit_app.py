import streamlit
import pandas

streamlit.title('My parents new healthy Diner')

streamlit.header(" Break Fast")

streamlit.text(" \N{flexed biceps} 1--> Idli")

streamlit.text(" \N{brain} 2--> Vada")
streamlit.text(" 2--> Upma")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
