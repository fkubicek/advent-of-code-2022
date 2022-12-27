from aoc22_util.input import *

class VideoSystem:
    WIDTH = 40
    HEIGHT = 6

    def __init__(self) -> None:
        self.cycle = 0
        self.register_X = 1
        
        self.total_signal_strength = 0
        self.screen = [False for _ in range(self.WIDTH * self.HEIGHT)]

    def draw(self):
        beam_pos = self.cycle - 1
        sprite_pos = self.register_X
        if abs(sprite_pos - (beam_pos % self.WIDTH)) <= 1:
            self.screen[beam_pos] = True
    
    def count_signal_strength(self):
        if self.cycle == 20 or (self.cycle > 20 and self.cycle <= 220 and (self.cycle - 20) % 40 == 0):
            signal_strength = self.cycle * self.register_X
            self.total_signal_strength += signal_strength

    def tick(self):
        self.cycle += 1
        self.draw()
        self.count_signal_strength()

    def noop(self):
        self.tick()
    
    def addx(self, a1):
        for _ in range(2):
            self.tick()
        self.register_X += a1
    
    def print_screen(self):
        buffer = []
        for beam_pos in range(self.WIDTH * self.HEIGHT):
            if beam_pos > 0 and beam_pos % self.WIDTH == 0:
                buffer.append("\n")
            buffer.append("#" if self.screen[beam_pos] else ".")
        print("".join(buffer))

if __name__ == "__main__":

    video_system = VideoSystem()

    for line in file_readlines_stripped("10/input.txt"):
        line = line.split()
        instruction = line[0]
        match instruction:
            case "noop":
                video_system.noop()
            case "addx":
                video_system.addx(int(line[1]))
            case _:
                raise Exception("Unknown instruction.")

    print(video_system.total_signal_strength)
    video_system.print_screen()
