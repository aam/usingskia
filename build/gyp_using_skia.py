#!/usr/bin/python
import os
import sys

script_dir = os.path.dirname(__file__)
using_skia_src = os.path.abspath(os.path.join(script_dir, os.pardir))

sys.path.insert(0, os.path.join(using_skia_src, 'third_party', 'skia', 'third_party', 'externals', 'gyp', 'pylib'))

import gyp

if __name__ == '__main__':
  args = sys.argv[1:]

  if not os.environ.get('GYP_GENERATORS'):
    os.environ['GYP_GENERATORS'] = 'ninja'

  args.append('--check')
  args.append('-I%s/third_party/skia/gyp/common.gypi' % using_skia_src)

  args.append(os.path.join(script_dir, '..', 'using_skia.gyp'))

  print 'Updating projects from gyp files...'
  sys.stdout.flush()

  sys.exit(gyp.main(args))