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
			print(	
					"Product Name:",ProductsList[int(self.ProductId)][0],
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
			print(	
					"Product Name:",ProductsList[int(self.ProductId)][0],
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
	Products = {}
	Total = 0
	def __init__():
		pass

class Payment:
	def __init__():
		CustId
		CustName
		CardType
		CardNo

class Customer (Cart, Payment):
	ProductFileName = "ProductList.pickle"
	TransectionFile = "TransectionsFile.pickle"
	CustomerPass = None
	CustomerId = None
	CustomerLogin = None
	CustomerName = None
	def __init__(self):
		Cart.CartId = CartId + 1
		Cart.NoOfProducts = 0
		Cart.Products = {}
		Cart.Total = 0

	def BuyProducts(self):
		Customer.ViewCart(self)
		print("\nProceed to Payment Press [Yes/No]: ")
		op_task = input()
		if(str(op_task) == "Yes" or str(op_task) == "yes"):
			Customer.MakePayment(self)

		if os.path.exists(self.TransectionFile):
			FilePtr = open(self.TransectionFile, "rb") 
			TransDetail = pickle.load(FilePtr)
			FilePtr.close()
		else:
			print("Something Went Wrong!")

		HighestId = sum(len(trans) for trans in TransDetail.values())
		self.TransId = int(HighestId / 4) + 1
		TransDetail[self.TransId] = Cart.Products

		with open(self.TransectionFile,'wb') as FilePtr:
			pickle.dump(TransDetail, FilePtr)
			FilePtr.close()
			print("Transection Successful!!")
			print("Your have purchased these items:")
			Customer.ViewCart(self)
			print("Your items will be delivered with in 2 days!")

	def MakePayment(self):
		print("Processing...")

	def AddToCart(self, ProductId, Quantity):
		if os.path.exists(self.ProductFileName):
				FilePtr = open(self.ProductFileName, "rb") 
				ProductList = pickle.load(FilePtr)
				FilePtr.close()
		else:
			print("Something Went Wrong!")
		if(int(ProductId) in ProductList):
			ProductDetail =	str(Customer.CustomerId) + ", " + \
							ProductList[int(ProductId)][0] + ", " + \
							ProductList[int(ProductId)][1] + ", " + str(Quantity)

			self.Products[int(self.NoOfProducts)] = ProductDetail.split(',')
			self.NoOfProducts += 1
			self.Total += int(Quantity) * int(ProductList[int(ProductId)][1])
			print("Product", ProductId, "added into cart!")
		else:
			print("Invalid Product Id!")

	def ViewCart(self):
		if(len(self.Products) > 0):
			index = 1
			for item in self.Products:
				print(
						str(index) + ". ",self.Products[item][1],"\t\t",
						self.Products[item][2],"\t\t",self.Products[item][3]
					)
				index += 1
			print("Total Products: ",self.NoOfProducts,"\tTotal Amount: ",self.Total)
		else:
			print("Cart is empty!")
			

	def DeleteFromCart(self, cartId, Quantity):
		if(len(self.Products) >= int(cartId)):
			cartId = int(cartId)-1
			if(self.Products[cartId][3] == int(Quantity)):
				self.NoOfProducts -= 1
				self.Total -= int(Quantity) * self.Products[cartId][2]
				del self.Products[cartId] 

			else:
				self.Total -= int(Quantity) * int(self.Products[cartId][2])
				self.Products[cartId][3] = int(self.Products[cartId][3]) - int(Quantity)
			print("Product", cartId, "removed!")
		else:
			print("Invalid Product Id!")

	def ShowTrasections(self):
		if os.path.exists(self.TransectionFile):
			FilePtr = open(self.TransectionFile, "rb") 
			TransDetail = pickle.load(FilePtr)
			FilePtr.close()
			print(TransDetail)
		else:
			print("Something Went Wrong!")


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
			want_login = input("\n1. Admin Login\t2. User Login\nChoose Option: ")
			if(int(want_login) == 1):
				adminObject = Login(1)
				if(Admin.adminLogin == True):
					print("Login Successfully!")
					adminObject.ViewProducts()
					while(1):
						space = ' '
						space_count = 4
						print(	
								"\n1. Add Products" + space_count * space + \
								"2. Modify Products"+ space_count * space + \
								"3. Delete Products"+ space_count * space + \
								"4. View Products"+ space_count * space + \
								"5. Exit\nOperation: "
							)
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
						print(
								"\n1. Add Into Cart" + space_count * space + \
								"2. View Cart" + space_count * space + \
								"3. Delete From Card" + space_count * space + \
								"4. Buy Products" + space_count * space + \
								"5. View Products" + space_count * space + \
								"6. Show All Trasections" + space_count * space + \
								"7. Exit\nOperation:" \
								)
						op_task = input()
						if(str(op_task) == "1"):
							pid = input("Enter Product Id:")
							Quantity = input("No of Piece:")
							userObject.AddToCart(pid, Quantity)
						elif(str(op_task) == "2"):
							userObject.ViewCart()
						elif(str(op_task) == "3"):
							cid = input("Enter Product Cart Id:")
							Quantity = input("No of Piece:")
							userObject.DeleteFromCart(cid, Quantity)
						elif(str(op_task) == "4"):
							userObject.BuyProducts()
						elif(str(op_task) == "5"):
							userObject.ViewProducts()
						elif(str(op_task) == "6"):
							userObject.ViewProducts()
						elif(str(op_task) == "7"):
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