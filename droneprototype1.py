from codrone_edu.drone import *

drone = Drone()
drone.connect()

color_data = drone.get_back_color()

drone.takeoff()

drone.hover(2)
drone.avoid_wall(4, 15)
drone.hover(2)

drone.move_distance(0, 0, 0.5, 0.25)
time.sleep(2)
drone.go("forward", 10, 1)
drone.hover(2)

drone.land()
drone.set_drone_LED(color_data)
time.sleep(2)
drone.takeoff()


drone.disconnect()