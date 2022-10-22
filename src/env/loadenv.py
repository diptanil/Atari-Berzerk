import gym

ENVMAP : dict[str, str] = {
    'berzerk' : 'ALE/Berzerk-v5',
    'mario' : 'ALE/MarioBros-v5'
}

class Environment:
    def __init__(self, env: str):
        env_str = None
        try:
            env_str = ENVMAP[env]
        except:
            raise ValueError('Environment not found')
        #Loading the environment
        self._env = gym.make(env_str)
    
    @property
    def env(self):
        return self._env