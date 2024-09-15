from csv import DictWriter
import pandas as pd
from datetime import datetime

class Member():

    '''
    this class to represent a library member and track borrowed books.
    '''

    def add_member(self,name):
        member = {'name':name}
        fieldname=["name"]
        with open('member.csv',"a") as f:
            memb=DictWriter(f,fieldnames=fieldname)
            memb.writerow(member)
        f.close() 
        print(f'the member {name} is added with succesfully')
        
    def check_out_book(self,name,title,date):
        dt = datetime.strptime(date,'%Y-%m-%d').strftime('%Y-%m-%d')
        borrowed_books={"name":name,"title":title,"date":dt}
        fieldname=["name","title","date"]
        with open('borrow_book.csv',"a") as f:
            bor_book=DictWriter(f,fieldnames=fieldname)
            bor_book.writerow(borrowed_books)
        f.close()

    def return_book(self,name,title):
        data=pd.read_csv("borrow_book.csv")
        data=data.drop(data[(data.title==title) & (data.name==name)].index)
        data.to_csv('borrow_book.csv', index=False)





"""
    def replace_check(self,check,title):
        try:
            data=pd.read_csv("book.csv")
            i=next(iter(data[data.title==title].index))
            data.loc[i,'check']=check
            data.to_csv('book.csv', index=False) 
        except:
            print() 
"""