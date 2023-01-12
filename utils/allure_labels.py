import allure


def allure_labels(feature: str, title: str):
    allure.dynamic.feature(feature)
    allure.dynamic.title(title)