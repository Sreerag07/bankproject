class Book:
    def details(self,model):
        self.model=model
        print("The book model is",self.model)
class Author(Book):
    def details(self,mode):
        self.mode=mode
        print("The book model has to be",self.mode)
st=Author()
st.details(1)