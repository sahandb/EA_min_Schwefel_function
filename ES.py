# imports
import matplotlib.pyplot as plt
import numpy as np

# initial value!!!!!!!!!!!!!!!
n = 10


# population = np.random.randint(-500, 500, (100, n))
# sigmaPop = np.random.random((100, n))


def initialPop(popLength, popSize):
    populations = []
    for i in range(popSize):
        x = np.random.uniform(-500, 500, popLength)
        sigma = np.random.random(popLength)
        populations.append([x, sigma])
    return np.array(populations)


# selection ! Rand!
def selection(pop, k):
    selectedChromosomes = []
    for i in range(k):
        r = np.random.randint(0, len(pop))
        ch = pop[r]
        selectedChromosomes.append(ch)
    return np.array(selectedChromosomes)


# fitness
def fitnessFunction(gnome):
    fit = 0
    sumPart = 0
    alpha = 418.9829

    for item in gnome[0]:
        sumPart += (-item * np.sin(np.deg2rad(np.sqrt(np.abs(item)))))
    fit = sumPart + alpha * n
    return fit


# t can be = 1 2 3 4 for 4 type of xover
def crossover(t, pop):
    child = []
    if t == 1:  # xoverNum1 (p1+p2)/2 local
        titleXover = "local intermediary"
        parent1, parent2 = selection(pop, 2)
        for i in range(n):
            child = (np.array(parent1) + np.array(parent2)) / 2
        return child
    if t == 2:  # xoverNum2 (p1+p2)/2 global
        titleXover = "global intermediary"
        for i in range(n):
            parent1, parent2 = selection(pop, 2)
            child = (np.array(parent1) + np.array(parent2)) / 2
        return child
    if t == 3:  # xoverNum3 p1 or p2 local
        titleXover = "local discrete"
        parent1, parent2 = selection(pop, 2)
        for i in range(n):
            r = np.random.rand()
            if r < 0.5:
                child = np.array(parent1)
            else:
                child = np.array(parent2)
        return child
    if t == 4:  # xoverNum4 p1 or p2 global
        titleXover = "global discrete"
        for i in range(n):
            parent1, parent2 = selection(pop, 2)
            r = np.random.rand()
            if r < 0.5:
                child = np.array(parent1)
            else:
                child = np.array(parent2)
            return child


def mutation(t, pop):
    if t == 1:  # mNum1
        titleMut = "nonAdaptive"
        ceil = 500
        floor = -500
        epsilon = 0.00001
        for i in range(n):
            pop[0, i] = pop[0, i] + pop[1, i] * np.random.random()
            if pop[0, i] < floor:
                pop[0, i] = floor + epsilon
            elif pop[0, i] > ceil:
                pop[0, i] = ceil - epsilon
        return pop
    if t == 2:  # mNum2
        titleMut = "Adaptive"
        lrA = 1 / np.sqrt(2 * np.sqrt(n))
        lrB = 1 / np.sqrt(2 * n)
        r = np.random.normal()
        ceil = 500
        floor = -500
        epsilon = 0.00001
        for i in range(n):
            pop[1, i] = pop[1, i] * np.exp(lrA * r + lrB * np.random.random())
            if pop[1, i] < epsilon:
                pop[1, i] = epsilon
            elif pop[1, i] > 1:
                pop[1, i] = 1 - epsilon
            pop[0, i] = pop[0, i] + pop[1, i] * r
            if pop[0, i] < floor:
                pop[0, i] = floor + epsilon
            elif pop[0, i] > ceil:
                pop[0, i] = ceil - epsilon
        return pop


# main!


def main(xover_t, mutation_t, survival_t, epoch, pop, runs, titles):
    meanOf10run = 0
    minList = []
    for run in range(runs):
        minFit = []
        chroLast = []
        for i in range(epoch):
            nextPop = []
            for j in range(len(pop) * 7):
                pc = np.random.rand()
                if pc < 0.5:
                    child = crossover(xover_t, pop)
                else:
                    p1, p2 = selection(pop, 2)
                    p1Vp2 = np.random.rand()
                    if p1Vp2 < 0.5:
                        child = p1
                    else:
                        child = p2
                offspring = mutation(mutation_t, child)  # child only
                nextPop.append(offspring)
            if survival_t == 1:
                titleSurvivor = "child only"
                offsprings = np.append(pop, nextPop, axis=0)  # with parents
            elif survival_t == 2:
                titleSurvivor = "par and child"
                offsprings = nextPop  # without parents

            offsprings = sorted(offsprings, key=lambda offSpringCh: fitnessFunction(offSpringCh))
            minFit.append(fitnessFunction(offsprings[0]))
            chroLast.append(offsprings[0][0])
            pop = offsprings[0:100]
            pop = np.array(pop)
        minList = minFit
        meanOf10run = np.mean(minList)
        print(meanOf10run)
        print("lasts:", np.mean(chroLast))
        plt.figure(1)
        plt.title(titles)
        plt.plot(minFit)
        plt.show()


# main(xover type, mut type,survival type, epoch, population,run)

itrationn = 4000
runPerType = 10
# main(4, 1, 100, population)
titles = ""
titles2 = ""
titles3 = ""
for xoverType in range(1, 5):
    for mutationType in range(1, 3):
        for survivalType in range(1, 3):
            population = initialPop(10, 100)
            if survivalType == 1:
                titles = "  child Only  "
                if mutationType == 1:
                    titles2 = "  nonAdaptive  "
                    if xoverType == 1:
                        titles3 = "  local intermediary  "
                    elif xoverType == 2:
                        titles3 = "  global intermediary  "
                    elif xoverType == 3:
                        titles3 = "  local discreet  "
                    elif xoverType == 4:
                        titles3 = "  global discreet  "
                elif mutationType == 2:
                    titles2 = "  adaptive  "
                    if xoverType == 1:
                        titles3 = "  local intermediary  "
                    elif xoverType == 2:
                        titles3 = "  global intermediary  "
                    elif xoverType == 3:
                        titles3 = "  local discreet  "
                    elif xoverType == 4:
                        titles3 = "  global discreet  "
            elif survivalType == 2:
                titles = "  par and child  "
                if mutationType == 1:
                    titles2 = "  nonAdaptive  "
                    if xoverType == 1:
                        titles3 = "  local intermediary  "
                    elif xoverType == 2:
                        titles3 = "  global intermediary  "
                    elif xoverType == 3:
                        titles3 = "  local discreet  "
                    elif xoverType == 4:
                        titles3 = "  global discreet  "
                elif mutationType == 2:
                    titles2 = "  adaptive  "
                    if xoverType == 1:
                        titles3 = "  local intermediary  "
                    elif xoverType == 2:
                        titles3 = "  global intermediary  "
                    elif xoverType == 3:
                        titles3 = "  local discreet  "
                    elif xoverType == 4:
                        titles3 = "  global discreet  "
            main(xoverType, mutationType, survivalType, itrationn, population, runPerType, titles + titles2 + titles3)
