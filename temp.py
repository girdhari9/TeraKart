import pickle

# Products = 	{
# 					1: ['Toothpaste', '25', '50'], 
# 					2: ['Bursh', '15', '100']
# 				}

# pickle_out = open("ProductList.pickle", "wb")
# pickle.dump(Products, pickle_out)

# Users = { 	
# 			1: ['Giridhari', 'Hyderabad', '7000070234', 'girdhari@']
# 		}

# pickle_out = open("UserList.pickle", "wb")
# pickle.dump(Users, pickle_out)

Transections = 	{
					1: ['1','Toothpaste', '25', '1']
				}

pickle_out = open("TransectionsFile.pickle", "wb")
pickle.dump(Transections, pickle_out)