import re

class WordNode():
    def __init__(self, word = "", num = 0):
        self.word = word
        self.num = num

def solution(begin, target, words):
    queue = [WordNode(begin, 0)]

    while queue:
        now = queue.pop(0)
        for i in range(len(begin)):
            regex = re.compile(now.word[:i] + '.' + now.word[i+1:])
            matches = [string for string in words if re.match(regex, string)]

            for match in matches:
                queue.append(WordNode(match, now.num+1))

        try:
            del words[words.index(now.word)]
        except ValueError:
            continue

        if now.word == target:
            return now.num
    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))