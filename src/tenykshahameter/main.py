# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time

from tenyksservice import TenyksService, run_service
from tenyksservice.config import settings


class HahaMeter(TenyksService):

    direct_only = False

    irc_message_filters = {
        'haha': [r'haha']
    }

    def __init__(self, *args, **kwargs):
        self.HAHAFILE = settings.DATA_WORKING_DIR + '/hahas.db'
        super(HahaMeter, self).__init__(*args, **kwargs)

    def handle_haha(self, data, match):
        self.logger.debug("Haha offender; logging the incident.")
        with open(self.HAHAFILE, 'w+') as f:
            f.write('{} {}\n'.format(int(time.time()), data['nick']))


def main():
    run_service(HahaMeter)


if __name__ == '__main__':
    main()
