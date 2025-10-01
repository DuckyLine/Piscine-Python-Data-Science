ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Change ft_list
ft_list[1] = "World!"

# Change ft_tuple
ft_list_tmp = list(ft_tuple)
ft_list_tmp[1] = "France!"
ft_tuple = ft_list_tmp

# Change ft_set
ft_set.discard("tutu!")
ft_set.add("Le Havre!")

# Change ft_dict
ft_dict["Hello"] = "42Le Havre!"

# Print message
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
