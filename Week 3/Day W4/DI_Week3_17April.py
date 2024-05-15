#Pagination
class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.page_size = pageSize
        self.current_page = 0

    def getVisibleItems(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1

    def nextPage(self):
        if self.current_page < self.getNumPages() - 1:
            self.current_page += 1

    def firstPage(self):
        self.current_page = 0

    def lastPage(self):
        self.current_page = self.getNumPages() - 1

    def goToPage(self, pageNum):
        if pageNum >= 0 and pageNum < self.getNumPages():
            self.current_page = pageNum

    def getNumPages(self):
        return (len(self.items) + self.page_size - 1) // self.page_size
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  

p.nextPage()
print(p.getVisibleItems())

p.goToPage(2)
print(p.getVisibleItems())

p.lastPage()
print(p.getVisibleItems())
