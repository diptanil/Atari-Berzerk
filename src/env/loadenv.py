import gym
from gym.utils.env_checker import check_env
# from gym.utils.play import play

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
        print(f"Loading environment : {env}")

        self._env = gym.make(env_str,
        obs_type='rgb',                 # ram / rgb / greyscale
        frameskip=4,                    # frame skip
        difficulty=None,
        repeat_action_probability=0.25, # sticky action probability
        full_action_space=False,        # use all actions 
        render_mode = 'human'           # None / human / rgb_array
        )

        # Doing environment check
        # print("Checking Environment")
        # check_env(self._env.unwrapped)


    
    @property
    def env(self):
        return self._env