from Runner import Runner

runner = Runner()
for round in range(runner.rounds):
    print(runner)
    runner.run()