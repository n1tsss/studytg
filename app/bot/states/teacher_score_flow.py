from aiogram.fsm.state import State, StatesGroup


class TeacherScoreFlow(StatesGroup):
    choose_event = State()
    choose_mode = State()
    fill_scores = State()
    confirm = State()
