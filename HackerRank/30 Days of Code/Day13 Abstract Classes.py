from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self): pass
#title,author,price

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        return price

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()