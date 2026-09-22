import random
import time

import streamlit as st

from random_question_v1.selector import rand_draw


st.set_page_config(page_title="Random Question", page_icon="?")


for key, default in {
    "names": [],
    "questions": [],
    "used_names": set(),
    "used_questions": set(),
    "last_draw": None,
    "form_message": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def add_item(list_key, input_key, label):
    value = st.session_state[input_key].strip()
    if not value:
        st.session_state.form_message = f"Enter a {label.lower()} before adding it."
        return

    st.session_state[list_key].append(value)
    st.session_state[input_key] = ""
    st.session_state.form_message = None


st.title("Random Question")
st.write("Build a roster and a question list, then draw a pair.")

if st.session_state.form_message:
    st.warning(st.session_state.form_message)

name_column, question_column = st.columns(2)
with name_column:
    st.subheader("Roster")
    st.text_input("Name", key="name_input", label_visibility="collapsed", placeholder="Add a name")
    st.button(
        "Add name",
        on_click=add_item,
        args=("names", "name_input", "name"),
        use_container_width=True,
    )
    if st.session_state.names:
        st.write(st.session_state.names)
    else:
        st.caption("No names added yet.")

with question_column:
    st.subheader("Questions")
    st.text_input(
        "Question",
        key="question_input",
        label_visibility="collapsed",
        placeholder="Add a question",
    )
    st.button(
        "Add question",
        on_click=add_item,
        args=("questions", "question_input", "question"),
        use_container_width=True,
    )
    if st.session_state.questions:
        st.write(st.session_state.questions)
    else:
        st.caption("No questions added yet.")

st.divider()
no_repeats = st.checkbox("No repeats", key="no_repeats")

if no_repeats:
    available_names = [name for name in st.session_state.names if name not in st.session_state.used_names]
    available_questions = [
        question
        for question in st.session_state.questions
        if question not in st.session_state.used_questions
    ]
else:
    available_names = st.session_state.names
    available_questions = st.session_state.questions

can_draw = bool(available_names and available_questions)
if no_repeats and not can_draw and st.session_state.names and st.session_state.questions:
    st.info("No-repeat draws are exhausted. Add another name and question to continue.")
elif not can_draw:
    st.info("Add at least one name and one question to draw.")

if st.button("Draw", type="primary", disabled=not can_draw, use_container_width=True):
    chosen_name, chosen_question = rand_draw(available_names, available_questions)

    if no_repeats:
        st.session_state.used_names.add(chosen_name)
        st.session_state.used_questions.add(chosen_question)

    flash = st.empty()
    for _ in range(6):
        flash_name, flash_question = rand_draw(available_names, available_questions)
        flash.info(f"**{flash_name}**\n\n{flash_question}")
        time.sleep(0.5)

    st.session_state.last_draw = (chosen_name, chosen_question)
    flash.empty()

if st.session_state.last_draw:
    chosen_name, chosen_question = st.session_state.last_draw
    st.success(f"**{chosen_name}**, please answer:\n\n{chosen_question}")
