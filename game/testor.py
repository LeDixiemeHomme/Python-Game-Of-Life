from Runner import Runner

runner = Runner()
while runner.rounds >= 0:
    print(runner)
    runner.run()