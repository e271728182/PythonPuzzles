

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle,_,_ = [1, 2, 3,4,5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )



def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items'%(
        fn.__name__, result, c.starts, c.items))
    
def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
def pour_problem(X,Y,goal,start=(0,0)):
    if goal in start:
        return [start]
    explored=set()
    frontier=[[start]]
    while frontier:
        path=frontier.pop()
        x,y=path[-1] #last state in the first path of the frontier
        for state,action in successor(x,y,X,Y).items():
            if state not in explored:
                explored.add(state)
            path2=path+[action,state]
            if goal in state:
                return path2
            else:
                frontier.append(path2)
                
    return Fail

Fail=[]
                
def successor(x,y,X,Y):
    #return a dict of state action pairs {state:actions} describing what can be reached from the (x,y) state and how
    assert x<=X and y<=Y
    
