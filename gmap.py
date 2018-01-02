#! python3
import webbrowser, sys, pyperclip
import conf, logging
logging.basicConfig(level=logging.DEBUG)

def googlemap(steps, start, dest=''):
  if dest == '':
    webbrowser.open(conf.PLACE + start)
  else:
    if conf.BY_DELIMIT in dest:
        real_dest, mean = dest.split(conf.BY_DELIMIT)
        real_dest = real_dest.strip()
        mean = mean.strip()
        logging.debug('Mean is %s', (mean if mean in conf.MEANS else 'car'))
        real_mean = conf.MEANS[mean] if mean in conf.MEANS else conf.MEANS['car']
        webbrowser.open(conf.DIRECTION + start + '/' + real_dest + real_mean + (conf.ENABLE_STEPS if steps else ''))
    else:
        logging.debug('No mean specifed')
        webbrowser.open(conf.DIRECTION + start + '/' + dest + (conf.ENABLE_STEPS if steps else ''))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    logging.debug('Addr from argument')
    string = ' '.join(sys.argv[1:])
  else:
    logging.debug('Addr from clipboard')
    string = pyperclip.paste()

  steps = False
  if conf.STEPS_ON in string:
    logging.debug('Steps enabled')
    steps = True
    # Remove 'withsteps' from string
    start_loc = string.find(conf.STEPS_ON)
    string = string[:start_loc-1] + string[start_loc+len(conf.STEPS_ON):]

  if conf.DR_DELIMIT not in string:
    logging.debug('Place mode')
    googlemap(False, string)
  else:
    logging.debug('Direction mode')
    start, dest = string.split(conf.DR_DELIMIT)
    googlemap(steps, start.strip(), dest.strip())
