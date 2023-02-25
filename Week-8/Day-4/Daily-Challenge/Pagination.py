class Pagination:
	def __init__(self, items=[], page_size=10):
		self.items = items
		self.page_size = int(page_size)
		self.pages = {}
		page_slice = slice(int(page_size))
		i = 1 # extract this code to function like prepare pages
		while len(self.items) > 0:
			self.pages[i] = items[page_slice]
			del items[0:int(page_size)]
			i += 1
		self.total_pages = len(self.pages)
		self.current_page = 1
	def get_visible_items(self):
		return self.pages[self.current_page]
	def prev_page(self):
		self.current_page -= 1
		if self.current_page < 1:
			self.current_page = 1
		return self
	def next_page(self):
		self.current_page += 1
		if self.current_page > self.total_pages:
			self.current_page = self.total_pages
		return self
	def first_page(self):
		self.current_page = 1
		return self
	def last_page(self):
		self.current_page = self.total_pages
		return self
	def go_to_page(self, page_num):
		self.current_page = int(page_num)
		if self.current_page > self.total_pages:
			self.current_page = self.total_pages
		if self.current_page < 1:
			self.current_page = 1
		return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.current_page
print(p.get_visible_items())
p.next_page().next_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())

