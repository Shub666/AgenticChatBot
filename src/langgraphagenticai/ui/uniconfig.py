from configparser import ConfigParser

class Config:
    def __init__(self, config_file='./src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')

    def get_llm_options(self):
        value = self.config["DEFAULT"].get("LLM_OPTIONS")
        return [item.strip() for item in value.split(',')] if value else []

    def get_usecase_options(self):
        value = self.config['DEFAULT'].get('USECASE_OPTIONS')
        return [item.strip() for item in value.split(',')] if value else []

    def get_groq_model_options(self):
        value = self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS')
        return [item.strip() for item in value.split(',')] if value else []