def get_planet_name(id):
    switch_id = {
         1: "Mercury",
         2: "Venus",
         3: "Earth",
         4: "Mars",
         5: "Jupiter",
         6: "Saturn",
         7: "Uranus", 
         8: "Neptune",
        }
    return switch_id.get(id)

print(get_planet_name(3))