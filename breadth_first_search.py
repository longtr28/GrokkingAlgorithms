def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person_is_seller(person):
            print(person)
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False