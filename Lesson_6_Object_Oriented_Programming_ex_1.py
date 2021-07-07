from termcolor import colored
import time
class TrafficLight:
    color = 'green', 'yellow', 'red'

    def running(self):
        for el in self.color:
            if el == self.color[0]:
                print(colored(f'TrafficLight changing color \n  Traffic light color is - {el}', 'green'))
                time.sleep(8)
            elif el == self.color[1]:
                print(colored(f'TrafficLight changing color \n  Traffic light color is - {el}', 'yellow'))
                time.sleep(2)
            else:
                print(colored(f'TrafficLight changing color \n  Traffic light color is - {el}', 'red'))
                time.sleep(7)


color_light = TrafficLight()
color_light.running()
