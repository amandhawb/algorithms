# Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

def total_treasure(treasure_map):
    counter = 0
    for treasure in treasure_map.values():
        counter += treasure
    return counter

print(total_treasure({
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
})) # 15 

print(total_treasure({
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
})) # 50