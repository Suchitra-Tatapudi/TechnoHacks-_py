import random
combi_PW="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+}{:"
len_password=15
random_pw_gen="".join(random.sample(combi_PW,len_password))
print(f"{random_pw_gen}")