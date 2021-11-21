import os

def capability_select():
    capability = {"platformName": "Android",
                    "platformVersion": "10.0",
                    "automationName": "Appium",
                    "appPackage": "ru.mail.search.electroscope",
                    "appActivity": "ui.activity.AssistantActivity",
                    "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                        '../stuff/Marussia_v1.50.2.apk')
                                            ),
                    "orientation": "PORTRAIT"
                    }
    return capability