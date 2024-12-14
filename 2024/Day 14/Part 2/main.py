# I used matplotlib to plot the grid every frame and found there is a distorted tree every 101 frames starting at frame 62
# Then just incremented by 101 until i found it
# It's probably not the best solution, you could just check if there are 10 robots next to each other and that should cover the tree
# This code will not work for other inputs if you don't find your frame offsets
# In my opinion this part 2 is an absolute bs

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

lines = open('Day 14/Part 1/input.txt').read().splitlines()
grid_size = (103, 101)

points = []
for line in lines:
    pos, vel = line.split()
    pos = pos.split('p=')[1]
    vel = vel.split('v=')[1]
    y, x = pos.split(',')
    vy, vx = vel.split(',')
    points.append((int(x), int(y), int(vx), int(vy)))

fig, ax = plt.subplots(figsize=(10, 10))


def update_grid(frame):
    # Frames: 62, 163, 264 => 163 - 62 = 101
    # Every 101 frames there is a occurence of a distorted tree
    # 7031 is somewhere around where i saw the tree
    # Ended up being 7133, but since frame is 0 in the beginning it's 7132 seconds
    frame = ((7132) + frame * 101)
    grid = np.zeros(grid_size)

    for x, y, vx, vy in points:
        new_x = (x + vx * frame) % grid_size[0]
        new_y = (y + vy * frame) % grid_size[1]
        grid[new_x, new_y] = 1

    ax.clear()
    im = ax.imshow(grid, cmap='viridis', interpolation='nearest')
    print(frame)

    return [im]


anim = animation.FuncAnimation(
    fig,
    update_grid,
    frames=100,
    interval=1000,
    repeat=False
)

plt.tight_layout()
plt.show()
