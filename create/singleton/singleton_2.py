def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)

        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        print("Oi")
        self.theme = "Tema escuro"
        self.font = "18px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = "Tema claro"
    print(as1.theme)

    as2 = AppSettings()
    print(as1.theme)
