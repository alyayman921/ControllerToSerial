import pygame

class Controller:
    def __init__(self):

        self.joystick_count = 0
        pygame.init()
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        #print(f"Connected controllers: {self.joystick_count}")

    def controller(self):
        global b
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        deadzone=0.2
        axis_map = ["LSH", "LSV", "RSH", "RSV", "LTT", "RTT"]
        button_map = ['x', 'circle', 'square', 'triangle', 'share', 'ps', 'options', 'L3', 'R3', 'LB', 'RB', 'dpad_up', 'dpad_down', 'dpad_left', 'dpad_right', 'touchpad']
        String_to_send=""
        running = True
        while running:
            b=[]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.joystick_count > 0:
                joystick = pygame.joystick.Joystick(0)
                axis_count = joystick.get_numaxes()
                button_count = joystick.get_numbuttons()
                for i in range(axis_count):
                    axis_value = joystick.get_axis(i)
                    if axis_value>=0:
                        b.append(axis_map[i]) 
                        b.append(f'0{round(axis_value,2):.2f}')
                    else:
                        b.append(axis_map[i]) 
                        b.append(f'{round(axis_value,2):.2f}')

                for i in range(button_count):
                    button_pressed =joystick.get_button(i)
                    if button_pressed:
                        b.append('button')
                        b.append(button_map[i])
            return b
            #pygame.time.wait(60)

if __name__ == '__main__':
    controller_instance = Controller()
    while True:
        current_input = controller_instance.controller()
        print(current_input)
        # Perform further processing with current_input as needed
