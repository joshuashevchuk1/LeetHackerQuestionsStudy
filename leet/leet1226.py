import threading


class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Semaphore(1) for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # left fork = philospher
        # right forkfork = (philospher - 1) % 5
        l, r = philosopher, (philosopher - 1) % 5
        if philosopher != 4:
            self.forks[r].acquire()
            pickRightFork()
            self.forks[l].acquire()
            pickLeftFork()
            eat()
            self.forks[r].release()
            self.forks[l].release()
        else:
            self.forks[l].acquire()
            pickLeftFork()
            self.forks[r].acquire()
            pickRightFork()
            eat()
            self.forks[r].release()
            self.forks[l].release()
        self.putForksDown(putLeftFork, putRightFork)

    def putForksDown(self,
                     putLeftFork: 'Callable[[], None]',
                     putRightFork: 'Callable[[], None]') -> None:
        putLeftFork()
        putRightFork()
