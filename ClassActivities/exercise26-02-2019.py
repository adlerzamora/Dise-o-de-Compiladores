grammarText = "S -> A | B, A -> a, B -> B b, C -> c"

grammar = {}

productions = grammarText.split(",")


for production in productions:
    key = production.split("->")[0].strip()
    products = production.split("->")[1]
    grammar[key]=[]
    for product in products.split("|"):
        grammar[key].append(product)

print(grammar)

actual = "S"
queue = [actual]

visited = {}

while len(queue)!=0:
    actual = queue.pop()
    productions = grammar[actual]
    if not actual in visited:
        for production in productions:
            for char in production.split():
                if char in grammar:
                    queue.append(char)
        visited[actual]= True

print(visited)

notVisited = []

for key in grammar:
    if not key in visited: 
        notVisited.append(key)

print("Not visited: " + str(notVisited))