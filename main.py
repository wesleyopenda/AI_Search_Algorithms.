class Environment():
    myGraph = {'1': set(['2','3']),
               '2': set(['1','4',]),
               '3': set(['1','4']),
               '4': set(['3','2'])}
    start = '2'
    goal = '4'

class Agent(Environment):
    # depth first search
    def DFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop() # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:
                    p.append(path + [next]) # keep a record of where been
                else:
                    stack.append((next, path + [next]))
        return p

    # breadth first search
    def BFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop(0) # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:
                    p.append(path + [next]) # keep a record of where been
                    return p
                else:
                    stack.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print('DFS', Agent.DFS(Environment.myGraph, Environment.start, Environment.goal)) # calling the function
        print('BFS', Agent.BFS(Environment.myGraph, Environment.start, Environment.goal))

theEnvironment = Environment()
theAgent = Agent(theEnvironment)
