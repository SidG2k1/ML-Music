import random, time, math
def roman(n):
    if n==1: return 'I 2'
    elif n==2:return 'ii 3'
    elif n==3:return 'iii 4'
    elif n==4:return 'IV 1'
    elif n==5:return 'V 2'
    elif n==6:return 'vi 3'
    elif n==7:return 'vii7 4'
def mutatate(chord, MutationIntensity):
    for _ in range(MutationIntensity):
        rr = random.randint(0, len(chord)-1)
        # rr := random chord index
        minn, maxx = 1, 7
        # max chord range
        if chord[rr] == minn: chord[rr] += random.randint(0, 1)
        elif chord[rr] == maxx: chord[rr] -= random.randint(0, 1)
        else: chord[rr] += random.randint(-1, 1)
        # chord random shifts
    return chord

def trashiness(chord,goodchord):
    min_trash = 10**10 # effectively infinity, matters for min_trash replacement
    for good in goodchord:
        # cycling through all good chords
        trash = 0
        for i in range(len(good)):
            trash += (good[i]-chord[i])**2
            # Delta(chord)^2
        if trash < min_trash: min_trash = trash
    return min_trash # difference to closest good chord

def init_chord(): return [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]
for _ in range(100):
    avgTrash = 6
    while avgTrash>5.0:
        #param
        Good_chords = [[1, 4, 6], [4, 6, 8], [2, 4, 7], [1, 5, 1], [1, 4, 1], [1, 4, 5], [1, 6, 5], [2, 5, 1], [1, 4, 5], [1, 5, 6], [1, 5, 7], [7, 5, 1], [5, 4, 1]]
        evolutions, mutationLevel, diversity = 10, 3, 10
            # diversity = music length
        #init
        mutatedSet = []
        trashSet = []
        for i in range(diversity):
            mutatedSet.append(init_chord())
            trashSet.append(0)
        # end init

        for _ in range(evolutions):
            for i in range(diversity):
                trashSet[i] = trashiness(mutatedSet[i], Good_chords)
            mintrash, maxtrash = min(trashSet), max(trashSet)
            for i in range(len(trashSet)):
                if mintrash == trashSet[i]: mintrash = i
                if maxtrash == trashSet[i]: maxtrash = i
            #mix rand set+ minset
            minset = mutatedSet[mintrash]
            randset = mutatedSet[random.randint(0,len(mutatedSet)-1)]
            outset = []
            for i in range(len(minset)):
                outset.append(int((minset[i]+randset[i])/2.))
            #
            mutatedSet[maxtrash] = mutatate(outset, mutationLevel+0)
            #mutatedSet[maxtrash] = mutatate(mutatedSet[mintrash], mutationLevel+0)
        avgTrash = 1.*sum(trashSet)/len(trashSet)
    # print avgTrash, trashSet
    romMut = []
    for i in mutatedSet:
        romMut.append(map(roman, i))
    print romMut
    #time.sleep(0.02)
    ####print romMut
raw_input()
    #time.sleep(10)
