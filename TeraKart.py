import pickle
import os
import getpass
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

class Admin (Cart):
	ProductFileName = "ProductList.pickle"
	UserFileName = "UserList.pickle"
	TransectionFile = "TransectionsFile.pickle"
	adminId = None
	adminLogin = None
	ProductId = None
	def __init__():
		self.ProductName = None
		self.ProductPrice = None
		self.ProductPieces = None

	def ViewProducts(self):
		if os.path.exists(Guest.ProductsListName):
			with open(Guest.ProductsListName,"rb") as FilePtr:
				ShowProducts = pickle.load(FilePtr)
				FilePtr.close()
				print("Products:\n")
				print("S[.] Product Name\t\tPrice\t\t\tQuantity")
				for item in ShowProducts:
					print("",str(item) + ".", ShowProducts[item][0].ljust(20) + "\tRs.",
						(ShowProducts[item][1]).ljust(20), ShowProducts[item][2])
		else:
			print("OOPS!!! No Products are Available!")

	def AddProducts(self):
		if os.path.exists(Admin.ProductFileName):
			FilePtr = open(Admin.ProductFileName,"rb") 
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			# print(ProductsList)
		HighestId = sum(len(products) for products in ProductsList.values())
		self.ProductId = int(HighestId / 3) + 1
		self.ProductName = input("Enter Product Name: ")
		if self.ProductName.isdigit():
			print("Invalid Input!")
			return
		self.ProductPrice = input("Enter Product Price: ")
		if self.ProductPrice.isdigit() == False:
			print("Invalid Input!")
			return
		self.ProductPieces = input("Enter Product Quantity Available: ")
		if self.ProductPieces.isdigit() == False:
			print("Invalid Input!")
			return

		ProductDetail =	str(self.ProductName) + "," + \
						str(self.ProductPrice) + "," + str(self.ProductPieces) 
		ProductsList[self.ProductId] = ProductDetail.split(',')

		with open(Admin.ProductFileName,'wb') as FilePtr:
			pickle.dump(ProductsList, FilePtr)
			FilePtr.close()
			print("Product Added!")
			print("Product Id is:",self.ProductId)

	def DeleteProducts(self,ProductId):
		self.ProductId = ProductId
		if os.path.exists(Admin.ProductFileName):
			FilePtr = open(Admin.ProductFileName, "rb") 
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			if(int(self.ProductId) in ProductsList):
				print(	"Product Name:",ProductsList[int(self.ProductId)][0],
						"\nProduct Price:",ProductsList[int(self.ProductId)][1],
						"\nProduct Quantity:",ProductsList[int(self.ProductId)][2]
					)
				del ProductsList[int(self.ProductId)]
			else:
				print("Invalid Product Id!")
				return

			with open(Admin.ProductFileName, "wb") as FilePtr:
				pickle.dump(ProductsList, FilePtr)
				FilePtr.close()
				print("Delete Product",int(self.ProductId), "Successfully!")
		else:
			print("Something went Wrong!")


	def ModifyProducts(self,ProductId):
		self.ProductId = ProductId
		if os.path.exists(Admin.ProductFileName):
			FilePtr = open(Admin.ProductFileName, "rb") 
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
		else:
			print("Something went Wrong!")
			return

		if int(self.ProductId) in ProductsList:
			print(	
					"Product Name:",ProductsList[int(self.ProductId)][0],
					"\nProduct Price:",ProductsList[int(self.ProductId)][1],
					"\nProduct Quantity:",ProductsList[int(self.ProductId)][2]
				)
		else:
			print("Invalid Product Id!")
			return

		if(int(self.ProductId) in ProductsList):
			ProductsList[int(self.ProductId)][0] = input("Enter Product Name: ")
			ProductsList[int(self.ProductId)][1] = input("Enter Product Price: ")
			ProductsList[int(self.ProductId)][2] = input("Enter Product Quantity Available: ")
		else:
			print("Invalid Input!")
			return

		with open(Admin.ProductFileName,'wb') as FilePtr:
			pickle.dump(ProductsList, FilePtr)
			FilePtr.close()
			print("Product Modified!")
		with open(Admin.ProductFileName, "rb") as FilePtr:
			ProductsList = pickle.load(FilePtr)
			FilePtr.close()
			print(	
					"Product Name:",ProductsList[int(self.ProductId)][0],
					"\nProduct Price:",ProductsList[int(self.ProductId)][1],
					"\nProduct Quantity:",ProductsList[int(self.ProductId)][2]
				)
		
	def MakeShipment(self, Products):
		if os.path.exists(self.ProductFileName):
			FilePtr = open(self.ProductFileName, "rb") 
			ProductDetail = pickle.load(FilePtr)
			FilePtr.close()

		for item in self.Products:
			ProductDetail[int(self.Products[item][4])][2] = int(ProductDetail[int(self.Products[item][4])][2]) - int(self.Products[item][3])

		if os.path.exists(self.ProductFileName):
			FilePtr = open(self.ProductFileName, "wb") 
			pickle.dump(ProductDetail, FilePtr)
			FilePtr.close()

	def ConfirmDelivery(self):
		if os.path.exists(self.TransectionFile):
			FilePtr = open(self.TransectionFile, "rb") 
			TransDetail = pickle.load(FilePtr)
			FilePtr.close()
			
		else:
			print("Something Went Wrong!")

		if os.path.exists(self.UserFileName):
			FilePtr = open(self.UserFileName, "rb") 
			UserDetail = pickle.load(FilePtr)
			FilePtr.close()
			
		else:
			print("Something Went Wrong!")
		size = sum(len(trans) for trans in TransDetail.values())
		arr = [1] * size
		
		print("\nTransection Details: \n")
		for item in TransDetail:
			flag = 0
			index = 1
			Total = 0
			if arr[item]:
				print("User Name: " + UserDetail[int(TransDetail[item][0])][0])
			for i in TransDetail:
				if TransDetail[item][0] == TransDetail[i][0] and arr[i]:
					flag = 1
					Total += int(TransDetail[i][2]) * int(TransDetail[i][3])
					print("Order No.:",index)
					print(
						"Product Name: \t" + TransDetail[i][1] + "\n" \
						"No of piece: \t" + TransDetail[i][3] + "\n" \
						"Cost: \t\t" + TransDetail[i][2]
					)
					index += 1
					arr[i] = 0
			if flag:
				print("Total Amount Paid: \t", Total,"\n")

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
		Payment.CustId = None
		Payment.CustName = None
		Payment.CardType = None
		Payment.CardNo = True

	def BuyProducts(self):
		if os.path.exists(self.TransectionFile):
			FilePtr = open(self.TransectionFile, "rb") 
			TransDetail = pickle.load(FilePtr)
			FilePtr.close()
		else:
			print("Something Went Wrong!")
		# HighestId = sum(len(trans) for trans in TransDetail.values())
		# self.TransId = int(HighestId / 4) + 1

		if(len(self.Products) > 0):
			self.ViewCart()
			Admin.MakeShipment(self,self.Products)
			self.ProceedToPay(TransDetail)
		else:
			pid = input("Enter Product Id: ")
			if pid.isdigit() == False:
				print("Invalid Input!")
				return
			Quantity = input("No of Piece: ")
			if Quantity.isdigit() == False:
				print("Invalid Input!")
				return
			self.AddToCart(pid, Quantity)
			Admin.MakeShipment(self,self.Products)
			self.ProceedToPay(TransDetail)

	def ProceedToPay(self, TransDetail):
		print("\nProceed to Payment Press [Yes/No]: ")
		op_task = input()
		if(str(op_task) == "Yes" or str(op_task) == "yes"):
			Customer.MakePayment(self)
		elif(str(op_task) == "No" or str(op_task) == "no"):
			self.ViewProducts()
			return 
		for item in self.Products:
			TransDetail[item] = self.Products[item] #Fixed

		with open(self.TransectionFile,'wb') as FilePtr:
			# print(TransDetail)
			pickle.dump(TransDetail, FilePtr)
			FilePtr.close()
			print("Transection Successful!!")
			print("Your have purchased these items:")
			self.ViewCart()  # View Cart
			self.EmptyCart() # Empty Cart
			print("Your items will be delivered with in 2 days!") 

	def MakePayment(self):
		self.CustId = self.CustomerId
		self.CardType = input("Enter card Type: ")
		if self.CardType.isdigit():
			print("Invalid Input!")
			return
		self.CardName = input("Enter Card Name: ")
		if self.CardName.isdigit():
			print("Invalid Input!")
			return
		self.CardNo = input("Enter Card No.: ")
		if self.CardNo.isdigit() == False:
			print("Invalid Input!")
			return
		print("Processing...")

	def AddToCart(self, ProductId, Quantity):
		flag = 1
		if os.path.exists(self.ProductFileName):
				FilePtr = open(self.ProductFileName, "rb") 
				ProductList = pickle.load(FilePtr)
				FilePtr.close()
		else:
			print("Something Went Wrong!")
		if(int(ProductId) in ProductList):
			ProductDetail =	str(Customer.CustomerId) + "," + \
							ProductList[int(ProductId)][0] + "," + \
							ProductList[int(ProductId)][1] + "," + \
							str(Quantity) + "," + str(ProductId)

			for item in self.Products:
				if ProductList[int(ProductId)][0] == self.Products[item][1]:
					if int(ProductList[int(ProductId)][2]) > int(self.Products[item][3]) + int(Quantity):
						self.Products[item][3] = str(int(self.Products[item][3]) + int(Quantity))
						flag = 0
						break
					else:
						print("Product is not Available or Quantity is high!")

			if flag:
				if int(ProductList[int(ProductId)][2]) > int(Quantity):
					HighestId = sum(len(prod) for prod in ProductList.values())
					HID = sum(len(prod) for prod in self.Products.values())
					HighestId = int(HighestId / 4) + int(HID / 4) 
					# if HighestId in self.Products:
					# 	self.Products[HighestId].append(ProductDetail.split(',')) 
					# else:
					self.Products[HighestId] = ProductDetail.split(',') 
				else:
					print("Product is not Available or Quantity is high!")

			self.NoOfProducts += 1
			self.Total += int(Quantity) * int(ProductList[int(ProductId)][1])
			print("Product", ProductId, "added into cart!")
			# print(self.Products)
		else:
			print("Invalid Product Id!")

	def EmptyCart(self):
		self.Products = {} 
		self.Total = 0
		self.NoOfProducts = 0

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
		TempCartId = cartId
		if len(self.Products) > 0:
			if os.path.exists(self.ProductFileName):
				FilePtr = open(self.ProductFileName, "rb") 
				ProductList = pickle.load(FilePtr)
				FilePtr.close()
			HighestId = sum(len(prod) for prod in ProductList.values())

			if(len(self.Products) >= int(cartId)):
				cartId = int(cartId) + int(HighestId / 4) -1
				if(int(self.Products[cartId][3]) == int(Quantity)):
					self.NoOfProducts -= 1
					self.Total -= int(Quantity) * int(self.Products[cartId][2])
					del self.Products[cartId] 
					print("Product", TempCartId, "removed!")

				else:
					self.Total -= int(Quantity) * int(self.Products[cartId][2])
					self.Products[cartId][3] = int(self.Products[cartId][3]) - int(Quantity)
					print("Quantity of Product", TempCartId, "is reduced!")
					print("Total Quantity of Product", TempCartId, "is:",int(self.Products[cartId][3]) - int(Quantity))
			else:
				print("Invalid Product Id!")
		else:
			print("Cart is empty!")
			self.ViewProducts()

	def ShowTrasections(self):
		if os.path.exists(self.TransectionFile):
			FilePtr = open(self.TransectionFile, "rb") 
			TransDetail = pickle.load(FilePtr)
			FilePtr.close()
		else:
			print("Something Went Wrong!")

		print("\nTransection Details: ")
		index = 1
		for item in TransDetail:
			Total = 0
			if int(TransDetail[item][0]) == int(self.CustomerId):
				Total += int(TransDetail[item][2]) * int(TransDetail[item][3])
				print("Order No.:",index)
				print(
					"Product Name: \t" + TransDetail[item][1] + "\n" \
					"No of piece: \t" + TransDetail[item][3] + "\n" \
					"Cost: \t\t" + TransDetail[item][2]
				)
				index += 1
				print("Total Amount Paid: \t", Total)				

class Guest (Customer):
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
				print("Products:\n")
				print("S[.] Product Name\t\tPrice\t\t\tQuantity")
				for item in ShowProducts:
					print("",str(item) + ".", ShowProducts[item][0].ljust(20) + "\tRs.",
						(ShowProducts[item][1]).ljust(20), ShowProducts[item][2])
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
		if self.UserName.isdigit():
			print("Invalid Input!")
			return
		self.UserAdd = input("Enter Your Address: ")
		if self.UserAdd.isdigit():
			print("Invalid Input!")
			return
		self.UserPhone = input("Enter Your Contact No: ")
		if self.UserPhone.isdigit() == False:
			print("Invalid Input!")
			return
		self.Password = getpass.getpass('Enter Password: ')
		ConfPassword = getpass.getpass('Enter Confirm Password: ')
		if self.Password != ConfPassword:
			print("Passwords do not match!")
			return 0

		self.UserData =	str(self.UserName) + "," + \
						str(self.UserAdd) + "," + str(self.UserPhone) + \
						"," + str(self.Password)

		UserDetail[self.UserId] = self.UserData.split(',')
		with open(Guest.UserFileName,'wb') as FilePtr:
			pickle.dump(UserDetail, FilePtr)
			FilePtr.close()
			print("Registered Successfully!")
			print("Your user Id is: " + str(self.UserId) + ". Keep save for future login.")
		return 1

		
class Login (Admin, Customer):
	UserFileName = "UserList.pickle"
	def __init__(self, LoginAs):
		CustomerPass = False
		Admin.adminLogin = False
		Customer.CustomerLogin = False
		print("Login here: ")
		self.UserId = input("Enter UserId: ")
		if self.UserId.isdigit() == False:
			print("Invalid User id!")
			return 0
		self.Password = getpass.getpass('Enter Password: ')

		if(LoginAs == 1):
			if(str(self.UserId) == "1325" and str(self.Password) == "girdhari"):
				Admin.adminLogin = True
				Login.SetScreen(0)
			else:
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
		if(self.adminLogin == True or self.CustomerLogin == True):
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

class operation:
	def __init__(self):
		pass

	def CustomerOperation(self,userObject):
		space = ' '
		space_count = 4
		if(Customer.CustomerLogin == True):
			print("Login Successfully!")
			userObject.ViewProducts()
			while(1):
				print(
						"\n1. Add To Cart" + space_count * space + \
						"2. View Cart" + space_count * space + \
						"3. Empty Cart" + space_count * space + \
						"4. Delete From Cart" + space_count * space + \
						"5. Buy Products" + space_count * space + \
						"6. View Products" + space_count * space + \
						"7. Show All Trasections" + space_count * space + \
						"8. Logout\n[Enter the choice]: ", end = "", flush = True
					)
				op_task = input()
				if(str(op_task) == "1"):
					pid = input("Enter Product Id: ").replace(" ","")
					Quantity = input("No of Piece: ").replace(" ","")
					if pid.isdigit() and Quantity.isdigit():
						userObject.AddToCart(pid, Quantity)
					else:
						print("Invalid Input!")

				elif(str(op_task) == "2"):
					userObject.ViewCart()
				elif(str(op_task) == "3"):
					userObject.EmptyCart()
				elif(str(op_task) == "4"):
					cid = input("Enter Product Cart Id: ").replace(" ","")
					Quantity = input("No of Piece: ").replace(" ","")
					if cid.isdigit() and Quantity.isdigit():
						userObject.DeleteFromCart(cid, Quantity)
					else:
						print("Invalid Input!")
					
				elif(str(op_task) == "5"):
					userObject.BuyProducts()
				elif(str(op_task) == "6"):
					userObject.ViewProducts()
				elif(str(op_task) == "7"):
					userObject.ShowTrasections()
				elif(str(op_task) == "8"):
					Login.SetScreen(2)
					exit(0)
				else:
					print("Invalid Input!")
					continue
		else:
			print("Try Again!")
			Login.SetScreen(1)

def main():
	Login.SetScreen(0)
	start = None
	while(1):
		if(Admin.adminLogin == True or Customer.CustomerLogin == True):
			pass
		else:
			start = input("\nDo you want to login?[Yes/No/Exit]: ")

		if(start == "Yes" or start == "yes"):
			want_login = input("\n1. Admin Login\t2. User Login\n[Enter Your Choice]: ")
			if want_login.isdigit() == False:
				print("Invalid Choice!")
				continue
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
								"5. Confrim Delivery"+ space_count * space + \
								"6. Logout\n[Enter the choice]: ", end = "", flush = True
							)
						op_task = input()
						if(str(op_task) == "1"):
							adminObject.AddProducts()
						elif(str(op_task) == "2"):
							adminObject.ModifyProducts(input("Enter Product Id: ").replace(" ",""))
						elif(str(op_task) == "3"):
							adminObject.DeleteProducts(input("Enter Product Id: ").replace(" ",""))
						elif(str(op_task) == "4"):
							adminObject.ViewProducts()
						elif(str(op_task) == "5"):
							adminObject.ConfirmDelivery()
						elif(str(op_task) == "6"):
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
				op = operation()
				op.CustomerOperation(userObject)
				continue

		elif(start == "No" or start == "no"):
			GuestObject = Guest()
			print("\nYou are entered as Guest!")
			GuestObject.ViewProducts()
			is_user = input("\nYou are already user?[Yes/No]: ")
			if(is_user == "Yes" or is_user == "yes"):
				CustomerObject = Login(2)
				op = operation()
				op.CustomerOperation(CustomerObject)
			else:
				ret = GuestObject.GetRegistered()
				if ret:
					CustomerObject = Login(2)
					op = operation()
					op.CustomerOperation(CustomerObject)

		elif(start == "exit" or start == "Exit"):
			print("Thank You and Welcome Again!")
			exit(0)
		else:
			print("Invalid Input!")
			continue

if __name__ == '__main__':
    main() 