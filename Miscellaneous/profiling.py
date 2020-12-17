# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Profiling

import cProfile
pr = cProfile.Profile()
pr.enable()

# --------------------------------------
# Lines of code that you want to profile
# --------------------------------------

pr.disable()
pr.dump_stats("/tmp/profile.cprof")
