from codrone_edu.drone import *

drone = Drone()

color_data = drone.get_back_color("name")
color_rgbdata = drone.get_back_color("RGB")

drone.connect()

drone.takeoff()

drone.hover(2)
drone.avoid_wall(4, 15)
drone.hover(2)

drone.move_distance(0, 0, 0.5, 0.2)
time.sleep(2)
drone.move_distance(0.5, 0, 0, 0.2)
drone.hover(2)

drone.land()
drone.get_back_color("name")
drone.set_drone_LED()
print(color_rgbdata)

drone.disconnect()