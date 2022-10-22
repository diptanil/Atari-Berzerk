from .env.loadenv import Environment

class Application:
    def __init__(self, env: str, soln: str):

        self._env = Environment(env).env

        self.test_random_act()

        
    # Checks everything is working by running the environment with random action
    def test_random_act(self):

        self._env.action_space.seed(42)

        observation, info = self._env.reset(seed=42)

        for _ in range(1000):
            observation, reward, terminated, truncated, info = self._env.step(self._env.action_space.sample())

            if terminated or truncated:
                observation, info = self._env.reset()

        self._env.close()


