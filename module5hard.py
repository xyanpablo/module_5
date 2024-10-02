from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == User.__hash__(password):
                self.current_user = User
                print(f'{nickname}, вход выполнен.')
            else:
                print('Неверный пароль.')

        else:
            print('Такого пользователя не существует.')

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь с никнеймом: {nickname} уже существует.')
        else:
            self.users.append(User)
            print(f'Регистрация успешно выполнена, {nickname}')

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        if video in self.videos:
            pass
        else:
            self.videos.append(video)

    def get_videos(self, key):
        search = []
        for i in self.videos:
            if key.lower() in i.title.lower():
                search.append(i.title)
        return search

    def watch_video(self, mov):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in self.videos:
                if mov == i:
                    if i.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for j in range(i.duration):
                            i.time_now += 1
                            sleep(1)
                            print(i.time_now)
                        print("Конец видео")
                else:
                    continue
            Video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')