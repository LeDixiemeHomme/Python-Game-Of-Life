from Runner import Runner

runner = Runner()
while runner.rounds >= 0:
    runner.stringify_map()
    print('generation ' + str(runner.rounds))
    runner.run()