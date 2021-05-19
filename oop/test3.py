class Book:
    def val(self,lname,bname,author,pages):
        self.lname=lname
        self.bname=bname
        self.author=author
        self.pages=pages
        print("Library name:",self.lname)
        print("Bookname:",self.bname)
        print("Author:",self.author)
        print("pages:",self.pages)
b=Book()
b.val("ksd","eye","john",101)