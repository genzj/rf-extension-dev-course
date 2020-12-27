from robot.api.deco import library, keyword
from robot.api import logger


@library(scope='GLOBAL', version='1.1')
class Outputs:
    @keyword
    def should_be_nice(self, v):
        if v != 'nice':
            raise Exception("value '%s' is not so nice." % (v,))

    @keyword
    def should_be_nice_again(self, v):
        if v != 'nice':
            raise Exception(
                '*HTML* value "<a href="https://cn.bing.com/dict/search?q=%s">%s</a>" is not so nice.' % (v, v,)
            )

    @keyword
    def test_logs(self):
        print('*DEBUG* Debug info from a library.')
        print('*WARN* Warning from a library.')
        print('*HTML* This is <b>bold</b>.')
        logger.info('<i>This</i> is a boring example.', html=True)

