def solution(n, words):
    before_words = []
    before_word = words[0][0]
    cnt = 0
    for word in words:
        print(cnt, before_words)
        cnt += 1
        if word[0] != before_word[-1] or word in before_words:
            return [(cnt-1)%n+1, (cnt-1)//n+1]
        before_words.append(word)
        before_word = word

    return [0,0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))