class Book:
    def __init__(self,  title, author, pages, is_read=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read
    
    def mark_as_read(self):
        self.is_read = True

    def info(self):
        return (f'title: {self.title}, author: {self.author},pages: {self.pages}, is_read: {self.is_read}')

b1 = Book('My Book', 'Israel Israeli', 220, False)
print (b1.info())
b1.mark_as_read()
print (b1.info())





