from robot.api import logger


class GlobalScope:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self):
        logger.console(f"\n--> Create Lib {self.__class__.__name__}\n")
    
    def kw(self):
        pass
