from robot.api import logger


class CaseScope:
    ROBOT_LIBRARY_SCOPE = "TEST CASE"
    
    def __init__(self):
        logger.console(f"\n--> Create Lib {self.__class__.__name__}\n")

    def kw(self):
        pass
