from .env.loadenv import Environment

class Application:
    def __init__(self, env: str, soln: str):

        print(f"Loading environment : {env}")
        self.environment = Environment(env)