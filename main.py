import pickle
import pprint
import os
import shelve

class Admin:
	FileName = "ProductList.pickle"
	adminId = None
	adminLogin = None
	ProductId = None
	def __init__():
		# self.
		self.ProductName = None
		self.ProductPrice = None
		self.ProductPieces = None

	def ViewProducts(self):
		if os.path.exists(Guest.ProductsListName):
			with open(Guest.ProductsListName,"rb") as FilePtr:
				ShowProducts = pickle.load(FilePtr)
				FilePtr.close()
				print("Products:")
				for item in ShowProducts:
					print(str(item) + ".", ShowProducts[item][0],"\t\t",
						ShowProducts[item][1],"\t\t", ShowProducts[item][2])
		else:
			print("OOPS!!! No Products are Available!")

	def AddProducts(self):
		if os.path.exists(Admin.FileName):
			FilePtr = open(Admin.FileName,"rb") # we can use with open() as fileptr:
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			print(ProductsList)
		HighestId = sum(len(products) for products in ProductsList.values())
		self.ProductId = int(HighestId / 3) + 1
		self.ProductName = input("Enter Product Name:")
		self.ProductPrice = input("Enter Product Price:")
		self.ProductPieces = input("Enter Product Quantity Available:")

		ProductDetail =	str(self.ProductName) + ", " + \
						str(self.ProductPrice) + ", " + str(self.ProductPieces) 
		ProductsList[self.ProductId] = ProductDetail.split(',')

		with open(Admin.FileName,'wb') as FilePtr:
			pickle.dump(ProductsList, FilePtr)
			FilePtr.close()
			print("Product Added!")
			print("Product Id is: ",self.ProductId)

	def DeleteProducts(self,ProductId):
		self.ProductId = ProductId
		if os.path.exists(Admin.FileName):
			FilePtr = open(Admin.FileName, "rb") 
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			if(int(self.ProductId) in ProductsList):
				print(	"Product Name:",ProductsList[int(self.ProductId)][0],
						"Product Price:",ProductsList[int(self.ProductId)][1],
						"Product Quantity:",ProductsList[int(self.ProductId)][2]
					)
				del ProductsList[int(self.ProductId)]
			else:
				print("Invalid Product Id!")

			with open(Admin.FileName, "wb") as FilePtr:
				pickle.dump(ProductsList, FilePtr)
				FilePtr.close()
				print("Delete Product",int(self.ProductId), "Successfully!")
		else:
			print("Something went Wrong!")


	def ModifyProducts(self,ProductId):
		self.ProductId = ProductId
		if os.path.exists(Admin.FileName):
			FilePtr = open(Admin.FileName, "rb") 
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			print(	"Product Name:",ProductsList[int(self.ProductId)][0],
					"\nProduct Price:",ProductsList[int(self.ProductId)][1],
					"\nProduct Quantity:",ProductsList[int(self.ProductId)][2]
				)
		else:
			print("Something went Wrong!")

		if(int(self.ProductId) in ProductsList):
			ProductsList[int(self.ProductId)][0] = input("Enter Product Name:")
			ProductsList[int(self.ProductId)][1] = input("Enter Product Price:")
			ProductsList[int(self.ProductId)][2] = input("Enter Product Quantity Available:")
		else:
			print("Invalid Input!")

		with open(Admin.FileName,'wb') as FilePtr:
			pickle.dump(ProductsList, FilePtr)
			FilePtr.close()
			print("Product Modified!")
		with open(Admin.FileName, "rb") as FilePtr:
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			print(	"Product Name:",ProductsList[int(self.ProductId)][0],
					"Product Price:",ProductsList[int(self.ProductId)][1],
					"Product Quantity:",ProductsList[int(self.ProductId)][2]
				)
		

	def MarkShipment(self):
		pass
	def ConfirmDelivery(self):
		pass

class Guest:
	GuestId = 0
	UserData = None
	UserFileName = "UserList.pickle"
	ProductsListName = "ProductList.pickle"
	def __init__(self):
		self.GuestId += 1

	def ViewProducts(self):
		if os.path.exists(Guest.ProductsListName):
			with open(Guest.ProductsListName,"rb") as FilePtr:
				ShowProducts = pickle.load(FilePtr)
				FilePtr.close()
				print("Products:")
				for item in ShowProducts:
					print(str(item) + ".", ShowProducts[item][0],"\t\t",
						ShowProducts[item][1],"\t\t", ShowProducts[item][2])
		else:
			print("OOPS!!! No Products are Available!")

	def GetRegistered(self):
		print("\nPlease! Register yourself to purchase products.")
		if os.path.exists(Guest.UserFileName):
			FilePtr = open(Guest.UserFileName,"rb") 
			UserDetail = pickle.load(FilePtr)
			FilePtr.close()
		else:
			print("Something Went Wrong!")

		HighestId = sum(len(users) for users in UserDetail.values())
		self.UserId = int(HighestId / 4) + 1
		self.UserName = input("Enter Your Name: ")
		self.UserAdd = input("Enter Your Address: ")
		self.UserPhone = input("Enter Your Contact No: ")
		self.Password = input("Enter Your Password: ")
		  
		self.UserData =	str(self.UserName) + ", " + \
						str(self.UserPhone) + ", " + str(self.UserData) + \
						", " + str(self.Password)

		UserDetail[self.UserId] = self.UserData.split(',')
		with open(Guest.UserFileName,'wb') as FilePtr:
			pickle.dump(UserDetail, FilePtr)
			FilePtr.close()
			print("Registered Successfully!")
			print("Your user Id is: ",self.UserId,". Keep save for future login.")

class Cart:
	CartId = 0
	NoOfProducts = 0
	Products = []
	Price = 0
	Total = 0
	def __init__():
		pass

class Payment:
	def __init__():
		CustId
		CustName
		CardType
		CardNo

class Customer (Guest, Cart, Payment):
	ProductFileName = "ProductList.pickle"
	CustomerPass = None
	CustomerId = None
	CustomerLogin = None
	CustomerName = None
	def __init__(self):
		Cart.CartId = CartId + 1
		Cart.NoOfProducts = 0
		Cart.Products = []
		Cart.Price = 0
		Cart.Total = 0

	def BuyProducts(self):
		pass
	def MakePayment(self):
		pass
	def AddToCart(self, ProductId):
		self.Products.append(ProductId)
		print("Product", ProductId, "added into cart!")

	def ViewCart(self):
		for item in Cart.Products:
			print(item)

	def DeleteFromCart(self, ProductId):
		if(ProductId in self.Products):
			del self.Products[0] 
			print("Product", ProductId, "removed!")
		else:
			print("Invalid Product Id!")



class Login (Admin, Customer):
	UserFileName = "UserList.pickle"
	def __init__(self, LoginAs):
		CustomerPass = False
		Admin.adminLogin = False
		Customer.CustomerLogin = False
		self.UserId = input("Enter UserId: ")
		self.Password = input("Enter Password: ")

		if(LoginAs == 1):
			if(str(self.UserId) == "1325" and str(self.Password) == "girdhari"):
				Admin.adminLogin = True
				Login.SetScreen(0)
			else:
				Admin.adminLogin = False
				print("Wrong Credential. Try Again!")

		if(LoginAs == 2):	
			if os.path.exists(Login.UserFileName):
				FilePtr = open(Login.UserFileName, "rb") 
				UserList = pickle.load(FilePtr)
				FilePtr.close()

			if(int(self.UserId) in UserList):
				self.CustomerPass = UserList[int(self.UserId)][-1]
			else:
				print("Invalid User Id!")

			if(self.Password == self.CustomerPass):
				Customer.CustomerPass = True
				Customer.CustomerLogin = True
				Customer.CustomerId = self.UserId
				Customer.CustomerName = UserList[int(self.UserId)][0]
				Login.SetScreen(0)
			else:
				print("Invalid Password!")

	def __del__(self):
		print("Logout Successfully!")

	def SetScreen(flag):
	    if(flag == 0):
	        print("\033[H\033[J", end = '', flush = True)
	        print("\t\t\t\tWelcome to Terakart\t\t\t", end = "", flush = True)
	    if(flag == 1 or flag == 0):
	        if(Admin.adminLogin == True):
	        	print("Username: Admin")
	        if(Customer.CustomerLogin == True):
	        	print("Username:",Customer.CustomerName)

def main():
	Login.SetScreen(0)
	while(1):
		start = input("\nDo you want to login?[Yes/No]: ")
		if(start == "Yes" or start == "yes"):
			want_login = input("Admin Login: Press 1 and Enter\nUser Login: Press 2 and Enter\nChoose Option: ")
			if(int(want_login) == 1):
				adminObject = Login(1)
				if(Admin.adminLogin == True):
					print("Login Successfully!")
					adminObject.ViewProducts()
					while(1):
						print("\n1. Add Products\n2. Modify Products\n3. Delete Products\n4. View Products\n5. Exit\nOperation: ")
						op_task = input()
						if(str(op_task) == "1"):
							adminObject.AddProducts()
						elif(str(op_task) == "2"):
							adminObject.ModifyProducts(input("Enter Product Id:"))
						elif(str(op_task) == "3"):
							adminObject.DeleteProducts(input("Enter Product Id:"))
						elif(str(op_task) == "4"):
							adminObject.ViewProducts()
						elif(str(op_task) == "5"):
							Login.SetScreen(2)
							exit(0)
						else:
							print("Invalid Input!")
				else:
					print("Try Again!")
					Login.SetScreen(1)
					continue

			elif(int(want_login) == 2):
				userObject = Login(2)
				if(Customer.CustomerLogin == True):
					print("Login Successfully!")
					userObject.ViewProducts()
					while(1):
						print("\n1. Add Into Cart\n2. View Cart\n3. Delete From Card\n4. Buy Products\n5. View Products\n6. Exit\nOperation: ")
						op_task = input()
						if(str(op_task) == "1"):
							userObject.AddToCart(input("Enter Product Id:"))
						elif(str(op_task) == "2"):
							userObject.ViewCart()
						elif(str(op_task) == "3"):
							userObject.DeleteFromCart(input("Enter Product Id:"))
						elif(str(op_task) == "4"):
							userObject.BuyProducts()
						elif(str(op_task) == "5"):
							userObject.ViewProducts()
						elif(str(op_task) == "6"):
							Login.SetScreen(2)
							exit(0)
						else:
							print("Invalid Input!")
							continue
				else:
					print("Try Again!")
					Login.SetScreen(1)
					continue

		elif(start == "No" or start == "no"):
			GuestObject = Customer()
			print("\nYou are entered as Guest!")
			GuestObject.ViewProducts()
			is_user = input("\nYou are already user?[Yes/No]: ")
			if(is_user == "Yes" or is_user == "yes"):
				CustomerObject = Login(2)
			else:
				CustomerObject.GetRegistered()

		else:
			print("Invalid Input!")
			continue

if __name__ == '__main__':
    main() 