import streamlit as st

def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

st.title("Find the largest among 3")

a = st.number_input("Enter the first num")
b = st.number_input("Enter the second num")
c = st.number_input("Enter the third num")

if st.button("Find the largest"):
    largest = find_largest(a, b, c)
    st.write("The largest num is:", largest)
