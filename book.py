from csv import DictWriter
import pandas as pd

class Book():

    '''
    This class to represent a book.
    '''

    def __init__(self):
        self.book = {}

    def Search(self,title,data,key):
        lst=[book for book in data[key] if title in book]
        return lst

    def give_books(self,authors,data):
        lst=[book for author in authors for book in data[data.author==author]["title"]]
        print(lst) 

    def add_book(self,title,author):
        book = {'title':title,'author':author}
        fieldname=["title",'author']
        with open('book.csv',"a") as f:
            b=DictWriter(f,fieldnames=fieldname)
            b.writerow(book)
        f.close()
        print("the book is added with succesfuly") 

    def remove_book(self,title):
        data=pd.read_csv("book.csv")
        data=data.drop(data[data.title==title].index)
        data.to_csv('book.csv', index=False)
        print(f"the book {title} is removed with succesfuly")

    def search_book(self,title):
        data=pd.read_csv("book.csv")
        lst_book=self.Search(title,data,"title")
        if len(lst_book)==0:
            print("this book is not found") 
        else:
            print(lst_book)
    
    def search_author(self,author):
        data=pd.read_csv("book.csv")
        lst_author=self.Search(author,data,"author")
        if len(lst_author)==0:
            print("this author is not found") 
        else:
            print(lst_author)
            self.give_books(lst_author,data)

