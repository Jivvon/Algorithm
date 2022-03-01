from typing import List
from collections import defaultdict

from utils.timer import timer


def dfs(graph, N, key, footprint):
		print(footprint)

		if len(footprint) == N + 1:
				return footprint

		for idx, country in enumerate(graph[key]):
				graph[key].pop(idx)

				tmp = footprint[:]
				tmp.append(country)

				ret = dfs(graph, N, country, tmp)

				print(graph)
				graph[key].insert(idx, country)

				if ret:
						return ret
		print('{} -> {} 로 가는 이 경로로는 안 된다는걸 깨달아버렸다'.format(*footprint[-2:]))


@timer
def solution(tickets: List[List[str]]):
		graph = defaultdict(list)
		N = len(tickets)
		for ticket in tickets:
				graph[ticket[0]].append(ticket[1])
				graph[ticket[0]].sort()
		answer = dfs(graph, N, "ICN", ["ICN"])
		return answer


@timer
def _solution(tickets: List[List[str]]):
		answer = []
		adj = defaultdict(list)
		for ticket in tickets:
				adj[ticket[0]].append(ticket[1])

		for key in adj.keys():
				adj[key].sort(reverse=True)

		q = ['ICN']
		while q:
				tmp = q[-1]  # q의 마지막 원소
				if not adj[tmp]:
						answer.append(q.pop())
				else:
						q.append(adj[tmp].pop())
		answer.reverse()
		return answer


if __name__ == '__main__':
		solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
		solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
		solution([["ICN", "BBB"], ["ICN", "CCC"], ["BBB", "CCC"], ["CCC", "BBB"], ["CCC", "ICN"]])
