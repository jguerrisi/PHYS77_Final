from rotating_bodies import SolarSystem, Sun, Planet

solar_system = SolarSystem(400, projection_2d=True)

sun = Sun(solar_system, name="Sun")

planets = (
    Planet(
        solar_system,
        name = "Earth",
        position=(150, 50, 0),
        velocity=(0, 5, 0),
    ),
    Planet(
        solar_system,
        name = "Mars", 
        position=(100, -50, 0 ),
        velocity=(5, 0, 0), 
    ),
    Planet(
        solar_system,
        name = "Venus",
        position = (0, 20 , 0), 
        velocity = (3, 4, 2),
    ), 
    Planet(
        solar_system,
        name="Neptune",
        position=(30, 20, 0),
        velocity = (1, 1, 1)
    )
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.plot_all()