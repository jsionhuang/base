#基于用户的推荐类算法
from math import sqrt

#计算两个person的欧几里德距离
def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs(person1):
        if item in prefs(person2):
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return  1/(1+sqrt(sum_of_squares))
#计算两个person 的皮尔逊相关系数
def sim_person(prefs,p1,p2,n=5):#n指的时电影评分满分是5
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            return  1
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

    pSum = sum([prefs[p1][it]*prefs[p2][it],2] for it in si)

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))

    if den == 0:
        return 0
    r = num/den
    return r
#返回跟输入person的相似排名结果
def topMatches(prefs,person,n=5,similarity = sim_person):
    scores = [(similarity(prefs,person,other,n),other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]
#针对person进行推荐
def getRecommenddation(prefs,person,similarity = sim_person):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs,person,other)
        if sim < 0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item,0)
                totals[item] += prefs[other][item]*sim

                simSums.setdefault(item,0)
                simSums[item] += sim
    rankings = [(totals/simSums[item],item) for item,totals in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings

critics = {
    'Jack':{'See You Again':4.5,'Try Everything':3.5,'Let it Go':5.0,'Sugar':3.5,'Sorry':2.5,'Baby':3.0},
    'Michael':{'See You Again':2.5,'Try Everything':3.0,'Let it Go':3.0,'Sorry':3.5},
    'Petter':{'See You Again':2.5,'Try Everything':3.5,'Let it Go':3.0,'Sugar':4.5,'Sorry':4.5,'Animals':2.0},
    'Tom':{'See You Again':4.5,'Try Everything':4.0,'Let it Go':5.0},
}
#w为tom进行电影推荐
print(getRecommenddation(critics,"Tom"))