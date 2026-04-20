from aiogram.fsm.state import State, StatesGroup


class LeaderDistributionFlow(StatesGroup):
    choose_event = State()
    distribute_scores = State()
    submit = State()
