import monkeys
import cppstandards
import tarpits

valid_input = ['c++98', 'c++03', 'c++11', 'c++14']

choice = input('C++ standard')

if choice in valid_input:
    spec = cppstandards.standard(choice)

    monkey = monkeys.monkey(arms=float('inf'))

    while True:
        output = monkey.typewriter.type()

        if not spec.complaint(output):
            monkey.evolve(inplace = True)

        else:
            tarpits.tarball(output, location = '')
else:
    tarpits.sacrifice(__owner__)