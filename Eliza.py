import random

def splitClauses(text) :
    return map(lambda x: x.strip(' '),
            text.lower().replace(',','.').replace("'", '').split('.'))

def splitWords(text) :
    return text.split(' ')

conversions = {'i' : 'you', 'you' : 'i',
        'am' : 'are', 'are' : 'am',
        'my' : 'your', 'your' : 'my',
        'me' : 'you',
        'myself' : 'yourself', 'yourself' : 'myself',
        'dreamed' : 'dreampt',
        'maybe' : 'perhaps'
        }

# -----------------
#   importing rules
#       book provides approx 2 pages printed (3 keywords), full list (20+ keywords)
#       provided by the free resources from ineasysteps.com
# -----------------

from ELIZArules import rules

# -----------------

def transform(text) :
    return map(lambda x: conversions[x] if x in conversions else x, text)

def matchWildcard(term, text, soFar="") :
    if len(text) == 0 :
        return False, '', []

    if (isinstance(term, str) and text[0] == term) or (not isinstance(term,str) and text[0] in term) :
        return True, soFar, text

    return matchWildcard(term, text[1:], soFar + ' ' + text[0])

def matchPattern(pattern, text) :
    matches = []
    for i in range(len(pattern)) :

        if pattern[i] == 0 :

            if i + 1 == len(pattern) :
                matches.append(' '.join(text))
            else :
                success, match, text = matchWildcard(pattern[i+1], text)

                if not success :
                    return False, []
                else :
                    matches.append(match.strip())
        
        elif len(text) == 0 :
            return False, []

        elif not isinstance(pattern[i], str) :
            
            if text[0] in pattern[i] :
                matches.append(text[0])
                text = text[1:]
            else :
                return False, []

        elif pattern[i] == text[0] :
            matches.append(text[0])
            text = text[1:]

        else :
            return False, []

    return True, matches

def findKeywords(text) :
    for phrase in splitClauses(text) :
        words = list(transform(splitWords(phrase)))
        maxP = 0
        keywords = []

        for word in words :
            if word in rules :
                p = rules[word][0]
                if p > maxP :
                    keywords.insert(0, word)
                    maxP = p
                else :
                    keywords.append(word)
        if len(keywords) > 0 :
            return keywords, words
    return [], []

def answer(keywords, words) :
    for keyword in keywords :
        for test in rules[keyword][1] :
            pattern = test[0]
            responses = test[1:]

            success, matches = matchPattern(pattern, words)
            if success :
                response = random.choice(responses)
                return compose(response, matches)

def compose(template, fields) :
    result = ''
    for t in template :
        if type(t) is int :
            result += ' ' + fields[t-1]
        else :
            result += ' ' + t
    return result.strip()


# ----------------------------
#           Unit tests
# ----------------------------

def testPatterns() :
    print(matchWildcard('stop', ['stop']))
    print(matchWildcard('stop', ['stop', 'now']))
    print(matchWildcard('stop', ['I', 'stop', 'now']))
    print(matchWildcard('stop', ['I', 'can', 'stop']))
    print(matchWildcard('stop', ['I', 'can', 'stop', 'now']))
    print(matchWildcard('stop', ['I', 'can', 'finish', 'now']))

    print(matchPattern([0,'stop',0], ['stop']))
    print(matchPattern([0,'stop',0], ['stop', 'now']))
    print(matchPattern([0,'stop',0], ['I', 'stop', 'now']))
    print(matchPattern([0,'stop',0], ['I', 'can', 'stop']))
    print(matchPattern([0,'stop',0], ['I', 'stop', 'right', 'now']))
    print(matchPattern([0,'stop',0], ['I', 'can', 'finish', 'now']))

# -----------------------------
#           Main
# -----------------------------

def firstMain() :
    while(True) :
        text = input('? ')
        if len(text) == 0 :
            break
        
        # DO SOMETHING WITH THE INPUT

        for clause in splitClauses(text) :
            print(splitWords(clause))

def finalMain() :
    while(True) :
        text = input('? ')
        if len(text) == 0 :
            break
        keywords, words = findKeywords(text)
        print(answer(keywords, words))

if __name__ == "__main__" :
#    firstMain()
#    testPatterns()
    finalMain()
