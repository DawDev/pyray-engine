import raygine


if __name__ == "__main__":
    raygine.init(raygine.Settings())
    eng = raygine.get_engine()
    eng.run()