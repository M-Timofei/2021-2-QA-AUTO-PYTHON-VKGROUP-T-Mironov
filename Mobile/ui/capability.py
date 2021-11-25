import os

def capability_select(version):
    capability = {"platformName": "Android",
                    "platformVersion": "10.0",
                    "automationName": "Appium",
                    "appPackage": "ru.mail.search.electroscope",
                    "appActivity": "ui.activity.AssistantActivity",
                    'autoGrantPermissions': True,
                    "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                        f'../stuff/Marussia_v{version}.apk')
                                            ),
                    "orientation": "PORTRAIT"
                    }
    return capability