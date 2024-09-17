from member import Member
from book import Book
import pandas as pd
from datetime import datetime

class Library():
    '''
    this class to manage books and members.
    '''

    def choice(self):
        choice=input("Your choice : ")
        while choice not in ["1","2","3","4","5","6","7"]:
            choice=input("Your choice must be a number from 1 to 7 : ")
        return int(choice)

    def start(self):
        lib=Library()
        while True:
            print("""
    Welcom to Library Management System

    ####################################
    #  Choices:                        #
    #                                  #
    #     1) Add a new book            #
    #     2) Remove a book             #
    #     3) Search a book             #
    #     4) Check out a book          #
    #     5) Return a book             #
    #     6) Add a new member          #
    #     7) Exit                      #
    #                                  #
    #     8) Back                      #
    #                                  #
    ####################################  
    """)

            choice=self.choice()
            if choice==7:
                break
            method_list=[lib.add_book,lib.remove_book,lib.search_book,lib.check_out_book,lib.return_book,lib.add_member]
            method_list[choice-1]()
            
    def exist(self,name1,file,key="",name2=""):
        data=pd.read_csv(file)
        if name2=="" and key=="":
            dat=data[data.title==name1].index
        elif key=='name':
            dat=data[data.name==name1].index
        else:
            dat=data[(data.name==name1) & (data.title==name2)].index
        lst=[ d for d in dat]
        return len(lst)>0

    def gener(self,message):
        string=input(message+' : ')
        while string!="8" and not(string.replace(" ","")).isalpha() :
            string=input(message+' : ')
        if string=="8":
                self.start()
        return string

    def gener_date(self,message):
        test=False
        while not test:
            try:
                date=input(message+' : ')
                Format = "%Y-%m-%d"
                test = bool(datetime.strptime(date, Format)) and (datetime.strptime(date, Format)>datetime.now())
                if not test:
                    print("the date must be after today")
            except ValueError:
                print("make the date in the format YYYY-MM-DD. ")
                test=False
        return date

    def add_book(self):
        title=self.gener("write the title of the book")
        author=self.gener("write the author of the book")
        if self.exist(title,"book.csv"):
            print("this book is already added\n")
            self.add_book()
        book=Book()
        book.add_book(title,author)
    
    def remove_book(self):
        title=self.gener("write the title of the book")
        if not self.exist(title,"book.csv"):
            print("this book is not found\n")
            self.remove_book()
        book=Book()
        book.remove_book(title)

    def search_book(self):

        print("""

    ####################################
    #  Choices:                        #
    #     1) Search on title           #
    #     2) Search on author          #
    #                                  #
    ####################################  
    """)
        num=input("choice  : ")
        while num not in ["1","2"]:
            num=input("Your choice must be 1 or 2 : ")
        book=Book()
        if num == "1":
            title=self.gener("write the title of the book")
            book.search_book(title)
        else:
            name=self.gener("write the name of the author")
            book.search_author(name)
    
    def add_member(self):
        name=self.gener("write the name of the member")
        if self.exist(name,"member.csv","name")):
            self.add_member()
        member=Member()
        member.add_member(name)
    
    def check_out_book(self):
        name=self.gener("write the name of the member")
        if not self.exist(name,"member.csv",'name'):
            print("this name is not found")
            print("try again")
            self.check_out_book()
        title=self.gener("write the title of the book")
        if not self.exist(title,"book.csv"):
            print("try again")
            print("this book is not found")
            self.check_out_book()
        elif self.exist(title,"borrow_book.csv"):
            print("this book is cheked")
        else:
            date=self.gener_date("write the return date")
            book=Member()
            book.check_out_book(name,title,date)

    def return_book(self):
        name=self.gener("write the name of the member")
        title=self.gener("write the title of the book")
        if not self.exist(name,"borrow_book.csv","",title):
            self.return_book()
        book=Member()
        book.return_book(name,title)


lib=Library()

lib.start()













