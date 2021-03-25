from mycroft import MycroftSkill, intent_file_handler


class NusTemperatureDeclaration(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('declaration.temperature.nus.intent')
    def handle_declaration_temperature_nus(self, message):
        self.speak_dialog('declaration.temperature.nus')


def create_skill():
    return NusTemperatureDeclaration()

