from utils.timer import timer


@timer
def solution(begin, target, words):
		from collections import deque
		visited = [False] * len(words)

		def BFS(cur, words, visited):
				queue = deque()
				queue.append((cur, 0))
				while queue:
						word, count = queue.popleft()
						if word == target:
								return count

						for idx, w in enumerate(words):
								if len(set(enumerate(word)) - set(enumerate(w))) == 1 and not visited[idx]:
										queue.append((w, count + 1))
										visited[idx] = True
				return 0

		return BFS(begin, words, visited)


if __name__ == '__main__':
		solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])  # 4
		solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])  # 0
