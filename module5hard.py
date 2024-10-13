from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if not isinstance(other, (str, User)):
            raise TypeError('Операнд должен иметь тип "str" или "User"')
        res = other if isinstance(other, str) else other.nickname
        return self.nickname == res

    def __lt__(self, other):
        if not isinstance(other, (int, User)):
            raise TypeError('Операнд должен иметь тип "int" или "User"')
        res = other if isinstance(other, int) else other.age
        return self.age < res


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        name_video = '\n'.join(video.title for video in self.videos)
        return name_video

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    self.current_user = User
                    print(f'{nickname}, вход выполнен.')
                    return
                else:
                    print('Неверный пароль.')
                    return
            print('Такого пользователя не существует.')

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь с никнеймом: {nickname} уже существует.')
                return
        self.users.append(User(nickname, password, age))
        print(f'Регистрация успешно выполнена, {nickname}')
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if i in self.videos:
                pass
            else:
                self.videos.append(i)

    def get_videos(self, keyword):
        search = []
        for i in self.videos:
            if keyword.lower() in i.title.lower():
                search.append(i.title)
        return search

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in self.videos:
            if title == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for j in range(i.duration):
                    i.time_now += 1
                    sleep(1)
                    print(i.time_now)
                print("Конец видео")
                i.time_now = 0
                return
        print('Видео не найдено')


# Пример использования класса UrTube
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