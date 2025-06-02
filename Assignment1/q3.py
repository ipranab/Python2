Create a Book class that contains multiple Chapters, where each Chapter has a title and page count.
Write code to initialize a Book object with three chapters and display the total page count of the book.

Ans:
    class Chapter:
        def __init__(self,title,pages):
            self.title=title
			self.pages=pages

	class Book:
		def __init__(self,chapters):
			self.chapters=chapters

		def total_pages(self):
			return sum(ch.pages for ch in self.chapters)

	chapters = [Chapter("Intro", 10), Chapter("OOP", 20), Chapter("Conclusion", 15)]
	book = Book(chapters)
	print("Total pages:", book.total_pages())
