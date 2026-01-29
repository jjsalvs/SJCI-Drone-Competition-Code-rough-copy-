from codrone_edu.drone import *

drone = Drone()

drone.connect()

drone.takeoff() ## note that when it takes off, it takes off at 0.8 m high. the first wall is 0.609m high
## square is 0.46m, which means that its already in the right place.

drone.hover(1) ## hover commands are used to stabilize
drone.avoid_wall(4, 15) ## this makes it go forward until its 15 cm from the square solid panel
drone.hover(2)

drone.move_distance(0, 0, 0.4, 0.2) 

## total height from bottom to top of square is 106.68 cm. since it scales 80 cm high, we have- 
## 26.68 cm of square above us, and the green arch, with 24 inches of inner diameter, and 30 inches of outer diameter, adds ((6/2)*2.54)
## cm of height. this puts us at 114.2 cm, but we need to be a little above it and we need to account for
## the people setting it up wrong can be wrong. Let's round this up to 125 cm then, or 1.25m
# 125 - 80 is 45 cm. it needs to move 0.3 to 0.5 m up 

drone.hover(2)
drone.move_distance(0.5, 0, 0, 0.2) 
drone.hover(2)

drone.land() ## drone moves a little then lands and takes off again
time.sleep(1)

drone.takeoff() ## its 0.8m takeoff, the panel is 0.91m tall, so we should be able to go to through the little whole.
drone.move_forward(distance = 200, units = "cm", speed = 0.2) 
## this is just guessing, im guessing that my teammates put the panel 1.5m away, cuz theyre supposed to 
drone.hover(2)

drone.land() ## this should land at the green pad
time.sleep(2)

drone.takeoff() 
drone.hover(2)
drone.avoid_wall(4, 30) ## using avoid wall function since theres another panel. tunnel kinda towers over it 
## so i have to make sure that its keeping some distance

drone.hover(2)
drone.move_distance(0, 0, 0.6, 0.2) ## bottom of tunnel is 1.32m high so i have to add 0.5 to 0.7m to the 0.8m my takeoff function provides

drone.hover(2)
drone.move_forward(distance = 75, units = "cm", speed = 0.2)
drone.hover(2)

drone.move_distance(0, -0.6, 0, 0.2) ## y is left to right. -y is moving me right a little to account for the yellow arch
drone.hover(1)

drone.move_distance(0, 0, -0.4, 0.2) ## to the bottom of the yellow arch, its 0.86m. i have to fit into the diameter of the yellow arch.
## therefore i will move down 0.5m, moving me from 1.4m high to 0.8m, fitting into the diameter.
drone.hover(2)


drone.move_distance(0, 1.2, 0, 0.2) ## i got through the yellow arch, and now i moved 1.2 to the left, putting me at 0.6y (think of this as coordinate geometry)
drone.hover(2)
drone.move_forward(distance = 150, units = "cm", speed = 0.2)

drone.hover(2)
drone.move_distance(0, -0.6, 0, 0.2) ## using this to put me at (x, 0) 

## note parameters are (x, y, z), (front and backward, left and right, up an down)
drone.hover(2)

drone.land()


drone.disconnect()