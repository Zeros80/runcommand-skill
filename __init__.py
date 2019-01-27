from mycroft import MycroftSkill, intent_file_handler


class Runcommand(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('runcommand.intent')
    def handle_runcommand(self, message):
        self.speak_dialog('runcommand')


def create_skill():
    return Runcommand()

