import numpy as np


class SmallGridWorld:
    def __init__(self, world_size, agent_mind):
        self.world_size = world_size
        self.world = np.zeros((self.world_size, self.world_size))
        self.agent_mind = agent_mind
        self.iter = 0

    def value_iter(self):

        self.iter += 1
        left_world = np.roll(self.world, 1, axis=1)
        left_world[:, 0] = left_world[:, 1]
        right_world = np.roll(self.world, -1, axis=1)
        right_world[:, -1] = right_world[:, -2]
        up_world = np.roll(self.world, 1, axis=0)
        up_world[0, :] = up_world[1, :]
        down_world = np.roll(self.world, -1, axis=0)
        down_world[-1, :] = down_world[-2, :]
        self.world = -1 + (
            self.agent_mind[0] * left_world
            + self.agent_mind[1] * right_world
            + self.agent_mind[2] * up_world
            + self.agent_mind[3] * down_world
        )
        self.world[0, 0] = 0.0
        self.world[-1, -1] = 0.0
        self.world = np.around(self.world, 2)
        # print(self.world)
