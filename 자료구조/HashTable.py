# https://davinci-ai.tistory.com/19

class HashTable:
		def __init__(self):
				self.hash_table = list([0 for i in range(8)])

		def _hash_function(self, key):
				return key % 8

		def insert(self, key, value):
				gen_key = hash(key)
				hash_value = self._hash_function(gen_key)

				if self.hash_table[hash_value] == 0:
						self.hash_table[hash_value] = [[gen_key, value]]

				for i in range(len(self.hash_table[hash_value])):
						if self.hash_table[hash_value][i][0] == gen_key:
								self.hash_table[hash_value][i][1] = value
								return

				self.hash_table[hash_value].append([gen_key, value])

		def read(self, key):
				gen_key = hash(key)
				hash_value = self._hash_function(gen_key)

				if self.hash_table[hash_value] == 0:
						return None

				if self.hash_table[hash_value] != 0:
						for i in range(len(self.hash_table[hash_value])):
								if self.hash_table[hash_value][i][0] == gen_key:
										return self.hash_table[hash_value][i][1]
						return None

		def print(self):
				print(self.hash_table)


if __name__ == '__main__':
		ht = HashTable()
		ht.insert(1, 'a')
		ht.print()
		ht.insert('name', 'kang')
		ht.print()
		ht.insert(2, 'b')
		ht.print()
		ht.insert(3, 'c')
		ht.print()
		print(ht.read(2))
		ht.insert(4, 'd')
		ht.print()
