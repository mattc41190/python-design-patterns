from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition

# Class "Process" pretends to be a computer process
@acts_as_state_machine
class Process(object):
    created =  State(initial=True)
    waiting =  State()
    running = State()
    terminated = State()   
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    wait = Event(
        from_states=(
            created,
            running,
            blocked,
            swapped_out_waiting
        ),
        to_state=waiting
    )

    run = Event(
        from_states=waiting,
        to_state=running
    )

    block = Event(
        from_states=(running, swapped_out_blocked),
        to_state=blocked
    )

    terminate = Event(
        from_states=running,
        to_state=terminated
    )

    swap_wait = Event(
        from_states=waiting,
        to_state=swapped_out_waiting
    )

    swap_block = Event(
        from_states=blocked,
        to_state=swapped_out_blocked
    )

    def __init__(self, name):
        self.name = name
    
    @after('wait')
    def wait_info(self):
        print(f'{self.name} entered waiting state')
    
    @after('run')
    def run_info(self):
        print(f'{self.name} is now running')

    @after('block')
    def block_info(self):
        print(f'{self.name} is now blocked')
    
    @before('terminate')
    def terminate_info(self):
        print(f'{self.name} will be terminated at any moment...')

    @after('swap_wait')
    def swap_wait_info(self):
        print(f'{self.name} is now swapped out and waiting')

    @after('swap_block')
    def swap_blocked_info(self):
        print(f'{self.name} is now swapped out and blocked')

def transition(process: Process, event: Event, event_name: str):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: cannot transition from: {process.current_state} to {event_name}')

def state_info(process: Process):
    print(f'state of: {process.name} is {process.current_state}')

def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED  = 'terminated'
    SWAP_BLOCKED  = 'swap_blocked'


    p1, p2 = Process('process_001'), Process('process_002')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.block, BLOCKED)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.swap_block, SWAP_BLOCKED)
    [state_info(p) for p in (p1, p2)]

if __name__ == '__main__':
    main()