# import streamlit as st
# from collections import defaultdict
# import random

# # User Profile Class to handle KYC, Scores, and other data
# class UserProfile:
#     def __init__(self, username):
#         self.username = username
#         self.__name = None
#         self.__country = None
#         self.__age = None
#         self.__interests = []
#         self.scores = {}
#         self.asked_questions = set()

 

#     def update_fluency(self, scores):
#         self.scores['fluency'] = scores

#     def update_grammar(self, scores):
#         self.scores['grammar'] = scores
  
#     def mark_question_asked(self, question):
#         self.asked_questions.add(question)

#     def lowest_score(self):
#         lowest_score_type = min(self.scores, self.scores.get)
#         return lowest_score_type
#     def get_name(self):
#         print(self.__name)
#         return self.__name
#     def get_country(self):
#         return self.__country

#     def get_age(self):
#         return self.__age

#     def get_proficiency(self):
#         return self.__proficiency
#     def random_intrest(self):
#         return random.choice(self.__interests)
    
#     def get_interests(self):
#         return self.__interests
#     def set_name(self,name):
#         self.__name = name
#     def set_country(self,country):
#         self.__country=country
#     def set_age(self,age):
#         self.__age=age
#     def set_intrests(self,intrests):
#         self.__interests.append(intrests)        

#     def update_kyc(self, name, country, age, proficiency, interests):
#         self.set_name(name)
#         self.set_country(country)
#         self.set_age(age)
#         self.proficiency = proficiency
#         self.interests = interests

# class UserProfileManager:
#     def __init__(self):
#         self.user_profiles = defaultdict(UserProfile)

#     def user_exists(self, username):
#         return username in self.user_profiles

#     def create_user_profile(self, username):
#         self.user_profiles[username] = UserProfile(username)

#     def get_user_profile(self, username):
#         return self.user_profiles[username]

#     def update_user_scores(self, username, scores):
#         self.user_profiles[username].update_scores(scores)

#     def kyc_form(self, username):
#         user_profile = self.get_user_profile(username)
#         st.header("KYC Information")
#         with st.form(key='kyc_form'):
#             name = st.text_input("Name")
#             country = st.text_input("Country")
#             age = st.number_input("Age", min_value=0)
            
#             interests = st.text_area("Interests (separated by commas)")

#             submit = st.form_submit_button("Submit")
#             if submit:
#                 # Update KYC using the setter methods
#                 user_profile.update_kyc(name, country, age,  interests.split(","))
#                 st.sidebar.write(f"KYC completed for {username}!")

#     def display_profile(self, username):
#         user_profile = self.get_user_profile(username)
#         # Display profile using getter methods for private attributes
#         st.write(f"**Name**: {user_profile.get_name()}")
#         st.write(f"**Country**: {user_profile.get_country()}")
#         st.write(f"**Age**: {user_profile.get_age()}")
#         st.write(f"**Interests**: {', '.join(user_profile.get_interests)}")
#         if user_profile.scores:
#             st.write("### Scores")
#             st.write(user_profile.scores)

# import streamlit as st
# from collections import defaultdict
# import random

# # User Profile Class to handle KYC, Scores, and other data
# class UserProfile:
#     def __init__(self, username):
#         self.username = username
#         self.__name = None
#         self.__country = None
#         self.__age = None
#         self.__interests = []
#         self.scores = {}
#         self.asked_questions = set()

#     def update_fluency(self, scores):
#         self.scores['fluency'] = scores

#     def update_grammar(self, scores):
#         self.scores['grammar'] = scores
  
#     def mark_question_asked(self, question):
#         self.asked_questions.add(question)

#     def lowest_score(self):
#         lowest_score_type = min(self.scores, self.scores.get)
#         return lowest_score_type
    
#     # Getter and Setter methods for private attributes
#     def get_name(self):
#         return self.__name
    
#     def get_country(self):
#         return self.__country

#     def get_age(self):
#         return self.__age

#     def get_proficiency(self):
#         return self.proficiency

#     def random_interest(self):
#         return random.choice(self.__interests)
    
#     def get_interests(self):
#         return self.__interests
    
#     def set_name(self, name):
#         self.__name = name
    
#     def set_country(self, country):
#         self.__country = country
    
#     def set_age(self, age):
#         self.__age = age
    
#     def set_interests(self, interests):
#         self.__interests = interests

#     # KYC update method
#     def update_kyc(self, name, country, age, interests):
#         self.set_name(name)
#         self.set_country(country)
#         self.set_age(age)
        
#         self.set_interests(interests)

# # User Profile Manager Class to handle multiple profiles
# class UserProfileManager:
#     def __init__(self):
#         self.user_profiles = defaultdict(UserProfile)

#     def user_exists(self, username):
#         return username in self.user_profiles

#     def create_user_profile(self, username):
#         self.user_profiles[username] = UserProfile(username)

#     def get_user_profile(self, username):
#         return self.user_profiles[username]

#     def update_user_scores(self, username, scores):
#         self.user_profiles[username].update_scores(scores)

#     def kyc_form(self, username):
#         user_profile = self.get_user_profile(username)
#         st.header("KYC Information")
#         with st.form(key='kyc_form'):
#             name = st.text_input("Name")
#             country = st.text_input("Country")
#             age = st.number_input("Age", min_value=0)
    
#             interests = st.text_area("Interests (separated by commas)")

#             submit = st.form_submit_button("Submit")
#             if submit:
#                 # Update KYC using the setter methods
#                 user_profile.update_kyc(name, country, age, interests.split(","))
#                 st.sidebar.write(f"KYC completed for {username}!")

#     def display_profile(self, username):
#         user_profile = self.get_user_profile(username)
#         # Display profile using getter methods for private attributes
#         st.write(f"**Name**: {user_profile.get_name()}")
#         st.write(f"**Country**: {user_profile.get_country()}")
#         st.write(f"**Age**: {user_profile.get_age()}")
#         st.write(f"**Interests**: {', '.join(user_profile.get_interests())}")
#         if user_profile.scores:
#             st.write("### Scores")
#             st.write(user_profile.scores)
from collections import defaultdict
import random

# User Profile Class to handle KYC, Scores, and other data
class UserProfile:
    def __init__(self, username):
        self.username = username
        self.__name = None
        self.__country = None
        self.__age = None
        self.__interests = []
        self.scores = {}
        self.asked_questions = set()

    def update_fluency(self, scores):
        self.scores['fluency'] = scores

    def update_grammar(self, scores):
        self.scores['grammar'] = scores
  
    def mark_question_asked(self, question):
        self.asked_questions.add(question)

    def lowest_score(self):
        if not self.scores:
            return None
        lowest_score_type = min(self.scores, key=self.scores.get)
        return lowest_score_type
    
    # Getter and Setter methods for private attributes
    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country

    def get_age(self):
        return self.__age

    def get_proficiency(self):
        return getattr(self, 'proficiency', None)

    def random_interest(self):
        return random.choice(self.__interests) if self.__interests else None
    
    def get_interests(self):
        return self.__interests
    
    def set_name(self, name):
        self.__name = name
    
    def set_country(self, country):
        self.__country = country
    
    def set_age(self, age):
        self.__age = age
    
    def set_interests(self, interests):
        self.__interests = interests

    # KYC update method
    def update_kyc(self, name, country, age, interests):
        self.set_name(name)
        self.set_country(country)
        self.set_age(age)
        self.set_interests(interests)

# User Profile Manager Class to handle multiple profiles
class UserProfileManager:
    def __init__(self):
        self.user_profiles = defaultdict(UserProfile)

    def user_exists(self, username):
        return username in self.user_profiles

    def create_user_profile(self, username):
        self.user_profiles[username] = UserProfile(username)

    def get_user_profile(self, username):
        return self.user_profiles[username]

    def update_user_scores(self, username, scores):
        user_profile = self.get_user_profile(username)
        if 'fluency' in scores:
            user_profile.update_fluency(scores['fluency'])
        if 'grammar' in scores:
            user_profile.update_grammar(scores['grammar'])

    def kyc_form(self, username):
        user_profile = self.get_user_profile(username)
        print("KYC Information")
        name = input("Name: ")
        country = input("Country: ")
        age = int(input("Age: "))
        interests = input("Interests (separated by commas): ").split(",")

        # Update KYC using the setter methods
        user_profile.update_kyc(name, country, age, interests)
        print(f"KYC completed for {username}!")

    def display_profile(self, username):
        user_profile = self.get_user_profile(username)
        # Display profile using getter methods for private attributes
        print(f"**Name**: {user_profile.get_name()}")
        print(f"**Country**: {user_profile.get_country()}")
        print(f"**Age**: {user_profile.get_age()}")
        print(f"**Interests**: {', '.join(user_profile.get_interests())}")
        if user_profile.scores:
            print("### Scores")
            for score_type, score in user_profile.scores.items():
                print(f"{score_type.capitalize()}: {score}")
