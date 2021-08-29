from typing import List

from utils.timer import timer


@timer
def solution(table: List[str], languages: List[str], preference: List[int]):
		score = {}
		for t in table:
				for lang, pref in zip(languages, preference):
						if lang in t.split():
								score[t.split()[0]] = score.get(t.split()[0], 0) + (6 - t.split().index(lang)) * pref
		return sorted(score.items(), key=lambda item: [-item[1], item[0]])[0][0]


@timer
def _solution(table: List[str], languages: List[str], preference: List[int]):
		def job(row):
				return row.split()[0]

		def scores(row):
				return {lang: 5 - i for i, lang in enumerate(row.split()[1:])}

		def total(job):
				def score(job, lang):
						return jobs[job][lang] if lang in jobs[job] else 0

				return -sum(score(job, lang) * pref for lang, pref in zip(languages, preference))

		jobs = {job(row): scores(row) for row in table}
		return sorted((total(job), job) for job in jobs.keys())[0][1]


@timer
def _solution(table: List[str], languages: List[str], preference: List[int]):
		"""

		:param table: "직업군 5 -> 1점" 순 형식의 문자열. 공백으로 구분.
		:param languages: len <= 9. 중복x
		:param preference: languages의 길이와 같음. i번째 원소는 languages의 i번째 원소의 언어 선호도
		:return: 언어 선호도 x 직업군 언어 점수의 총합이 가장 높은 직업군. 여러 개라면 이름순으로 가장 빠른거 하나.
		"""
		dic = {}
		for i in table:
				l = i.split()
				professional = l[0]
				lans = l[1:]
				lans.reverse()
				dic[professional] = [""] + lans

		answers = []
		for key, val in dic.items():
				total = 0
				for lan, prefer in zip(languages, preference):
						if lan in val:
								total += val.index(lan) * prefer
				answers.append((total, key))

		answers.sort(reverse=True)
		answer = [i for i in answers if i[0] == answers[0][0]]
		answer.sort(key=lambda x: x[1])

		return answer[0][1]


if __name__ == '__main__':
		table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
		         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
		         "GAME C++ C# JAVASCRIPT C JAVA"]
		languages = ["PYTHON", "C++", "SQL"]
		preference = [7, 5, 5]
		solution(table, languages, preference)

		languages = ["JAVA", "JAVASCRIPT"]
		preference = [7, 5]
		solution(table, languages, preference)
