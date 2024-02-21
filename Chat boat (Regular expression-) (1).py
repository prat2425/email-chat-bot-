#!/usr/bin/env python
# coding: utf-8

# # Extracting information with message id-

# In[10]:


import re
import pandas as pd

def extract_city_state(subject):
    # Regular expression pattern to match city, state, and message ID information
    city_state_pattern = re.compile(r'([A-Z][\w\s]+),?\s*([A-Z]{2}).*?(\w{16,})$', re.IGNORECASE)
    
    # Search for city, state, and message ID matches in the subject
    match = city_state_pattern.search(subject)
    
    if match:
        city = match.group(1).strip()
        state = match.group(2).strip()
        message_id = match.group(3).strip()

        # Exclude specific words from the city
        exclude_words = ["Load availability", "Interested on the load", "Truck available"]
        for word in exclude_words:
            if word in city:
                city = city.replace(word, "").strip()

        return city, state, message_id
    else:
        return None, None, None

def extract_origin_destination(email_subjects):
    origin_cities = []
    origin_states = []
    dest_cities = []
    dest_states = []
    message_ids = []

    for subject in email_subjects:
        # Extract city, state, and message ID information from the subject
        city, state, message_id = extract_city_state(subject)

        # Assign extracted city, state, and message ID to origin, destination, and message IDs lists
        if city and state and message_id:
            origin_cities.append(city)
            origin_states.append(state)
            dest_cities.append(city)  # Assuming destination city is the same as the origin city
            dest_states.append(state)  # Assuming destination state is the same as the origin state
            message_ids.append(message_id)

    return origin_cities, origin_states, dest_cities, dest_states, message_ids

def is_valid_destination(city, state):
    # Add your validation logic here
    # For example, check if the city and state are valid in a database or using an API
    # Return True if valid, False otherwise
    if city.lower() == "india" or state.lower() == "na":
        return False
    return True

# Read the email subjects from the text file into a list
with open(r'C:\Users\prate\email_subjects.txt', 'r') as f:
    email_subjects = f.readlines()

# Remove newline characters from each subject
email_subjects = [subject.strip() for subject in email_subjects]

# Create a DataFrame from the list of email subjects
df = pd.DataFrame({'Subject': email_subjects})

# Display the DataFrame
df
# Extract origin, destination, and message IDs
origin_cities, origin_states, dest_cities, dest_states, message_ids = extract_origin_destination(df['Subject'])

# Print the extracted information
for i in range(len(origin_cities)):
    if is_valid_destination(dest_cities[i], dest_states[i]):
        print(f"Origin city: {origin_cities[i]}, origin state: {origin_states[i]}, Destination city: {dest_cities[i]}, destination state: {dest_states[i]}, Message ID: {message_ids[i]}")
    else:
        print(f"Invalid destination: {dest_cities[i]}, {dest_states[i]}")


# # Getting the result saved in data frame-

# In[13]:


import re
import pandas as pd

def extract_city_state(subject):
    # Regular expression pattern to match city, state, and message ID information
    city_state_pattern = re.compile(r'([A-Z][\w\s]+),?\s*([A-Z]{2}).*?(\w{16,})$', re.IGNORECASE)
    
    # Search for city, state, and message ID matches in the subject
    match = city_state_pattern.search(subject)
    
    if match:
        city = match.group(1).strip()
        state = match.group(2).strip()
        message_id = match.group(3).strip()

        # Exclude specific words from the city
        exclude_words = ["Load availability", "Interested on the load", "Truck available"]
        for word in exclude_words:
            if word in city:
                city = city.replace(word, "").strip()

        return city, state, message_id
    else:
        return None, None, None

def extract_origin_destination(email_subjects):
    origin_cities = []
    origin_states = []
    dest_cities = []
    dest_states = []
    message_ids = []

    for subject in email_subjects:
        # Extract city, state, and message ID information from the subject
        city, state, message_id = extract_city_state(subject)

        # Assign extracted city, state, and message ID to origin, destination, and message IDs lists
        if city and state and message_id:
            origin_cities.append(city)
            origin_states.append(state)
            dest_cities.append(city)  # Assuming destination city is the same as the origin city
            dest_states.append(state)  # Assuming destination state is the same as the origin state
            message_ids.append(message_id)

    return origin_cities, origin_states, dest_cities, dest_states, message_ids

def is_valid_destination(city, state):
    # Add your validation logic here
    # For example, check if the city and state are valid in a database or using an API
    # Return True if valid, False otherwise
    if city.lower() == "india" or state.lower() == "na":
        return False
    return True

# Read the email subjects from the text file into a list
with open(r'C:\Users\prate\email_subjects.txt', 'r') as f:
    email_subjects = f.readlines()

# Remove newline characters from each subject
email_subjects = [subject.strip() for subject in email_subjects]

# Extract origin, destination, and message IDs
origin_cities, origin_states, dest_cities, dest_states, message_ids = extract_origin_destination(email_subjects)

# Create a DataFrame with the extracted information
result_df = pd.DataFrame({
    'Origin City': origin_cities,
    'Origin State': origin_states,
    'Destination City': dest_cities,
    'Destination State': dest_states,
    'Message ID': message_ids
})

# Save the DataFrame to a CSV file
result_df.to_csv(r'C:\Users\prate\extracted_details_with_message_ids.csv', index=False)

# Display the DataFrame
result_df


# # Read this saved data frame-

# In[4]:


import pandas as pd

# Specify the file path of your text file
file_path = r'C:\Users\prate\extracted_details.csv'

# Read the text file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
df


# # 

# In[ ]:




