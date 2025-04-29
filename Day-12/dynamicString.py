name = "Rahim"
age =20

# template_string = "I am {}. I am {} years old".format(name, age)  #method 1 
# template_string = "I am {1}. I am {0} years old".format( age, name)  #method 2
template_string = "I am {user_name}. I am {user_age} years old".format( user_age =22, user_name = "karim")  #method 3

print(template_string)

# f method

age = 27
name = "jubair"

string = f"I am {name}. I am {age} years old"
print(string)