import configparser

data_configuration = configparser.RawConfigParser()
data_configuration.read("C:\\Users\\Elitebook\\PycharmProjects\\pythonProject\\Roshen\\Configuration\\config.ini")

class ReadDataConfiguraton:
    @staticmethod
    def get_application_url():
        base_login_url = data_configuration.get('common info', 'base_login_url')
        return base_login_url

