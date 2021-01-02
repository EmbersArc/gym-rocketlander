from gym.envs.registration import register

register(
    id="rocketlander-v0",
    entry_point="gym_rocketlander.envs:RocketLander",
)