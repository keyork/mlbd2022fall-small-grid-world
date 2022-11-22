import argparse
from model import SmallGridWorld
from utils import LOGGER
import numpy as np

EQUAL_THRESHOLD = 5
OUTPUT_ITER = [0, 1, 2, 3, 10, 100]
MAX_ITERS = 1000000


def main(config):
    LOGGER.warning("Start!")
    LOGGER.info("config:")
    print("world size: {}".format(config.ws))
    print("agent mind: {}".format(config.am))
    print("            [left, right, up, down]")
    if np.array(config.am).sum() != 1:
        LOGGER.error(
            "The sum of agent mind MUST be 1 but got {}, EXIT!".format(config.am)
        )
        return 0
    world_model = SmallGridWorld(world_size=config.ws, agent_mind=config.am)
    world = world_model.world
    equal_times = 0
    for iter in range(MAX_ITERS):
        world_model.value_iter()
        if (world == world_model.world).all():
            equal_times += 1
            world = world_model.world
        else:
            equal_times = 0
        if equal_times == EQUAL_THRESHOLD:
            LOGGER.info("Iter: {}".format(iter - EQUAL_THRESHOLD + 1))
            print(world)
            break
        else:
            world = world_model.world
            if iter in OUTPUT_ITER:
                LOGGER.info("Iter: {}".format(iter))
                print(world)
    LOGGER.warning("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ws", type=int, default=4, help="world size")
    parser.add_argument(
        "--am",
        type=float,
        nargs="+",
        default=[0.25, 0.25, 0.25, 0.25],
        help="agent mind, [left, right, up, down]",
    )
    args = parser.parse_args()
    main(args)
