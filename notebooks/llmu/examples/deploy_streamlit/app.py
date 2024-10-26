import cohere
import streamlit as st
import os
import textwrap
import json

# Set up Cohere client
co = cohere.ClientV2("COHERE_API_KEY") # Get your free API key: https://dashboard.cohere.com/api-keys

def generate_idea(industry, temperature):
    
    prompt = f"""
Generate a startup idea given the industry. Return the startup idea and without additional commentary.

Industry: Workplace
Startup Idea: A platform that generates slide deck contents automatically based on a given outline

Industry: Home Decor
Startup Idea: An app that calculates the best position of your indoor plants for your apartment

Industry: Healthcare
Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week

Industry: Education
Startup Idea: An online primary school that lets students mix and match their own curriculum based on their interests and goals

Industry: {industry}
Startup Idea:"""

    # Call the Cohere Chat endpoint
    response = co.chat( 
            messages=[{"role": "user", "content": prompt}],
            model="command-r-plus-08-2024", 
            temperature=temperature)
        
    return response.message.content[0].text

def generate_name(idea, temperature):
    
    prompt= f"""
Generate a startup name given the startup idea. Return the startup name and without additional commentary.

Startup Idea: A platform that generates slide deck contents automatically based on a given outline
Startup Name: Deckerize

Startup Idea: An app that calculates the best position of your indoor plants for your apartment
Startup Name: Planteasy 

Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week
Startup Name: Hearspan

Startup Idea: An online primary school that lets students mix and match their own curriculum based on their interests and goals
Startup Name: Prime Age

Startup Idea: {idea}
Startup Name:"""

    # Call the Cohere Chat endpoint
    response = co.chat( 
            messages=[{"role": "user", "content": prompt}],
            model="command-r-plus-08-2024", 
            temperature=temperature)
        
    return response.message.content[0].text

# The front end code starts here

st.title("🚀 Startup Idea Generator")

form = st.form(key="user_settings")
with form:
  st.write("Enter an industry name [Example: Productivity, Food, Sports] ")
  # User input - Industry name
  industry_input = st.text_input("Industry", key = "industry_input")

  # Create a two-column view
  col1, col2 = st.columns(2)
  with col1:
      # User input - The number of ideas to generate
      num_input = st.slider(
        "Number of ideas", 
        value = 3, 
        key = "num_input", 
        min_value=1, 
        max_value=10,
        help="Choose to generate between 1 to 10 ideas")
  with col2:
      # User input - The 'temperature' value representing the level of creativity
      creativity_input = st.slider(
        "Creativity", value = 0.5, 
        key = "creativity_input", 
        min_value=0.1, 
        max_value=0.9,
        help="Lower values generate more “predictable” output, higher values generate more “creative” output")  
  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Generate Idea")

  if generate_button:
    if industry_input == "":
      st.error("Industry field cannot be blank")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Startup Ideas:")

      for i in range(num_input):
          st.markdown("""---""")
          startup_idea = generate_idea(industry_input,creativity_input)
          startup_name = generate_name(startup_idea,creativity_input)
          st.markdown("##### " + startup_name)
          st.write(startup_idea)
          my_bar.progress((i+1)/num_input)