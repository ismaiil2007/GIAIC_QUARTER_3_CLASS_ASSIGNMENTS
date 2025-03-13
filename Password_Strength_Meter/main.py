

# " FIRST ATTEMPT - WORKED VERY STRICT - DOES'T ALLOW ANY REPETITION OF A SINGLE CHARACTERS"

#Live Link: https://password-generator-by-ismail.streamlit.app/

import streamlit as st

st.title("Password Strength Meter")

password = st.text_input("Enter Password")
password_validation_letters = 'abcdefghijklmnopqrstuvwxyz'
password_validation_char="!@#$%^*()_-=+`~<>/?|"
password_validation_numbers="1234567890"
password_set=set(password)
score=" "

if password:

    if len(password)>=8:    
        has_letter = len(password_set & set(password_validation_letters)) > 6  
        has_special_char = len(password_set & set(password_validation_char)) > 0  
        has_number = len(password_set & set(password_validation_numbers)) > 3 
        has_capital = len(password_set & set(password_validation_letters.upper())) > 0 

        if  has_letter and has_special_char and has_number and has_capital:  
           st.success("Your Password is Strong")  
        else:  
            st.error("Your password must include at least contain 6 Unique lowercase letter, 1 Uppercase letter, 3 Unique number, and one special character [!,#,@,,$....]")  
    else:
        st.error("Your password should be atleast 8 characters")
else:
    st.error("Please Enter a password")

    
# "SECOND ATTEMPT - WORKED - NOT OPTIMIZED -  DON'T ALLOWS REPITITION OF CHARACTERS"

# import streamlit as st

# st.title("Password Strenght Meter")

# password = st.text_input("Enter Password")
# password_validation_letters = 'abcdefghijklmnopqrstuvwxyz'
# password_validation_char="!@#$%^*()_-=+`~<>/?|"
# password_validation_numbers="1234567890"


# if password:

#     if len(password)>=8:
#         has_lowercase = 0
#         has_uppercase = 0
#         has_number = 0
#         has_special_char = 0
        
#         for i in range(len(password_validation_letters)): 
#             if password_validation_letters[i] in password:
#                 has_lowercase+=1  
           
#         for i in range(len(password_validation_char)):
#              if password_validation_char[i] in password:
#                 has_special_char+=1
                  
#         for i in range(len(password_validation_numbers)):
#              if password_validation_numbers[i] in password:
#                 has_number+=1

#         for i in range(len(password_validation_letters)):         
#             if password_validation_letters.upper()[i] in password:
#                 has_uppercase+=1
           

        

#         if has_lowercase >= 6 and has_uppercase >= 1 and has_number >= 3 and has_special_char >= 1:
#                st.success("Your Password is Strong")  
#         else:  
#                st.error("Your password must include at least contain 6 Unique lowercase letter, 1 Uppercase letter, 3 Unique number, and one special character [!,#,@,,$....]")  
#     else:
#         st.error("Your password should be atleast 8 characters")
# else:
#     st.error("Please Enter a password")


# "THIRD ATTEMPT - WORKED - OPTIMIZED - BUT ALSO ALLOWS REPETITION OF CHARACTERS"


# import streamlit as st

# st.title("Password Strenght Meter")

# password = st.text_input("Enter Password")
# password_validation_letters = 'abcdefghijklmnopqrstuvwxyz'
# password_validation_char="!@#$%^*()_-=+`~<>/?|"
# password_validation_numbers="1234567890"


# if password:

#     if len(password)>=8:
#         has_lowercase = 0
#         has_uppercase = 0
#         has_number = 0
#         has_special_char = 0

#         for i in range(len(password)):
        
#             if password[i] in password_validation_letters:
#                 has_lowercase+=1  
           
#             if password[i] in password_validation_char:
#                 has_special_char+=1
                
#             if password[i] in password_validation_numbers:
#                 has_number+=1

#             if password[i] in password_validation_letters.upper():  
#                 has_uppercase+=1
        

#         if has_lowercase >= 6 and has_uppercase >= 1 and has_number >= 3 and has_special_char >= 1:
#                st.success("Your Password is Strong")  
#         else:  
#                st.error("Your password must include at least contain 6  lowercase letter, 1 Uppercase letter, 3 number, and one special character [!,#,@,,$....]")  
#     else:
#         st.error("Your password should be atleast 8 characters")
# else:
#     st.error("Please Enter a password")


# "FOURTH ATTEMPT BY AI - ALSO ALLOWS REPTITION OF CHARACTERS"

# import streamlit as st

# st.title("Password Strength Meter")

# password = st.text_input("Enter Password")
# password_validation_letters = 'abcdefghijklmnopqrstuvwxyz'
# password_validation_char = "!@#$%^*()_-=+`~<>/?|"
# password_validation_numbers = "1234567890"

# if password:
#     if len(password) >= 8:
#         has_lowercase = sum(1 for char in password if char in password_validation_letters) >= 6
#         has_uppercase = any(char.isupper() for char in password)
#         has_number = sum(1 for char in password if char in password_validation_numbers) >= 3
#         has_special_char = any(char in password_validation_char for char in password)

#         if has_lowercase and has_uppercase and has_number and has_special_char:
#             st.success("Your Password is Strong")
#         else:
#             st.error("Your password must include at least 6 lowercase letters, 1 uppercase letter, 3 numbers, and 1 special character [!, #, @, $, ...]")
#     else:
#         st.error("Your password should be at least 8 characters")
# else:
#     st.error("Please Enter a password")     
