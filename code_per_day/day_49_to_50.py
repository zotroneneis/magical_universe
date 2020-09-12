import sys
sys.path.append('../')

import yaml
from magical_universe import CastleKilmereMember, Pupil

if __name__ == "__main__":

    with open('config.yaml', 'r') as c:
        config = yaml.load(c)

        bromley = CastleKilmereMember(**config['bromley'])
        print('bromley: ', bromley)

        lissy = Pupil(**config['lissy'])
        print('lissy: ', lissy)

        luke = Pupil(**config['luke'])
        print('luke: ', luke)
