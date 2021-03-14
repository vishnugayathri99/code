class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print(f"We have following books in our Library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book Database has been updated,you can take the book now")
        else:
            print(f"Book is already in use by {self.lendDict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to your list")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__=='__main__':
    lib=Library(['Python','c++','java','machinelearning','Data science'],"AI")
    while(True):
        print(f"Welcome to the {lib.name} Library.Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend Books")
        print("3.Add Books")
        print("4.Return Books")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            lib.displayBooks()
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name :")
            lib.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book do you want to add:")
            lib.addBook(book)
        elif user_choice==4:
            book=input("Enter the name of the book you want to return:")
            lib.returnBook(book)
        else:
            print("Not a valid option")
        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!='c' and user_choice2!='q'):
            user_choice2=input()
            if user_choice2=='q':
                exit()
            if user_choice2=='c':
                continue