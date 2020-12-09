"""Данные для тестов на регистрацию"""
from random import choice, randint
import string


class DataGenerator(object):
    """
    Попробуем "упростить" себе жизнь
    Схема 1 - валидная проверка все поля заполняются как надо (пользователь регистрируется). Ошибок не выскакивает
    Схема 2 - невалидный набор символов в поле username (встречаются пунктуационные символы пробел) (как оказалось валидный)
    Схема 3 - невалидный набор символов в поле email (встречаются пунктуационные символы пробел)
    Схема 4 - Поле пароля и поле его подтверждения не совпадают

    СХЕМЫ НА ПЕРЕПОЛНЕНИЕ ПОЛЕЙ (ЛИБО НАОБОРОТ):
    Схема 5 - Поле username имеет > 16 смимволов, либо < 6
    Схема 6 - Поле email имеет > 64 смимволов
    Схема 7 - Поле пароля имеет > 255 смимволов

    Схема 8 - Забиваем все поля некорректно
    """
    USERNAME_MAX_LENGTH = 16
    PASSWORD_MAX_LEN = 255
    EMAIL_MAX_LEN = 64 - 2
    ACCEPT_FLAG_ON = True
    ACCEPT_FLAG_OFF = False

    def generate_field(self, letters, left_border=0, right_border=1):
        """
        функция используется для генерации строки
        если строка случайным образом сгенерировалась только из пробелов, то мы ее перегенерируем
        """
        form_field = "".join(choice(letters) for _ in range(randint(left_border, right_border)))
        while self.check_field(form_field):
            form_field = "".join(choice(letters) for _ in range(randint(left_border, right_border)))
        return form_field

    @staticmethod
    def check_field(form_field):
        """
        проверка на пробельную строку
        """
        field_contains_only_whitespace_chars = True
        for char in form_field:
            if char not in string.whitespace:
                field_contains_only_whitespace_chars = False
                break
        return field_contains_only_whitespace_chars

    def generate_valid_username_field(self):
        """
        генерируем валидную строку
        """
        username = self.generate_field(
            letters=(string.digits + string.ascii_letters + string.punctuation + " "),
            left_border=6,
            right_border=self.USERNAME_MAX_LENGTH
        )
        return username

    def generate_valid_password_field(self):
        password = self.generate_field(
            letters=(string.digits + string.ascii_letters + string.punctuation + " "),
            left_border=1,
            right_border=self.PASSWORD_MAX_LEN
        )
        return password

    def generate_valid_email_field(self, random=True):
        """
        Генерируем корректную email строку
        """
        email_parts_len = (self.EMAIL_MAX_LEN - 2) // 3
        left_part = email_parts_len
        middle_part = email_parts_len
        right_part = self.EMAIL_MAX_LEN - 2 - left_part - middle_part
        quote = choice(["\"", "\'"])
        domain_part = (
                "@" + choice(string.ascii_letters) +
                self.generate_field(
                    letters=(string.digits + string.ascii_letters),
                    left_border=2,
                    right_border=middle_part - 2
                ) + choice(string.ascii_letters) + "." +
                self.generate_field(
                    letters=string.ascii_letters,
                    left_border=1,
                    right_border=right_part
                )
        )

        local_part_1 = (
                self.generate_field(
                    letters=(string.digits + string.ascii_letters),
                    left_border=1,
                    right_border=left_part
                )
        )
        local_part_2 = (
                quote +
                self.generate_field(
                    letters=(string.digits + string.ascii_letters + string.punctuation + " "),
                    left_border=1,
                    right_border=left_part - 2
                ) + quote
        )
        if random is True:
            return choice([local_part_1 + domain_part, local_part_2 + domain_part])
        else:
            return local_part_1 + domain_part

    def generate_invalid_username_field_not_enough(self):
        """
        Генерируем короткую невалидную строку (1 - 5) символов
        """
        left_border = 1
        right_border = 5
        username = self.generate_field(
            letters=(string.digits + string.ascii_letters + string.punctuation + " "),
            left_border=left_border,
            right_border=right_border
        )
        return username

    def generate_invalid_username_field_overflow(self):
        """
        Генерируем длинную невалидную строку 17+ символов
        """
        left_board = 17
        right_board = 100
        username = self.generate_field(
            letters=(string.digits + string.ascii_letters + string.punctuation + " "),
            left_border=left_board,
            right_border=right_board
        )
        return username

    def generate_invalid_password_field(self):
        """
        Генерируем невалидный длинный пароль
        """
        password = self.generate_field(
            letters=(string.digits + string.ascii_letters + string.punctuation + " "),
            left_border=self.PASSWORD_MAX_LEN + 1,
            right_border=512
        )
        return password

    def generate_invalid_email_field_length(self, not_enough=False, overflow=False):
        email = {}
        invalid_ranges = [(0, 1, "short"), (21, 42, "long")]
        for invalid_range in invalid_ranges:
            email[invalid_range[2]] = (
                    self.generate_field(
                        letters=(string.digits + string.ascii_letters + string.punctuation),
                        left_border=invalid_range[0],
                        right_border=invalid_range[1]
                    ) +
                    "@" +
                    self.generate_field(
                        letters=(string.digits + string.ascii_letters + string.punctuation),
                        left_border=invalid_range[0],
                        right_border=invalid_range[1]
                    ) +
                    "." +
                    self.generate_field(
                        letters=string.ascii_letters,
                        left_border=invalid_range[0],
                        right_border=invalid_range[1]
                    )
            )
        if not_enough is True:
            return email["short"]
        if overflow is True:
            return email["long"]

    def generate_invalid_email_field_value(self):
        """
        Генерируем строку с пунктуацией
        """
        left_border = 2
        right_border = 20
        email = (
                self.generate_field(
                    letters=(string.digits + string.ascii_letters + string.punctuation),
                    left_border=left_border,
                    right_border=right_border
                ) +
                "@" +
                self.generate_field(
                    letters=(string.digits + string.ascii_letters + string.punctuation),
                    left_border=left_border,
                    right_border=right_border
                ) +
                "." +
                self.generate_field(
                    letters=string.ascii_letters,
                    left_border=left_border,
                    right_border=right_border
                )
        )
        return email

    def scheme_1(self):
        """scheme = 1: Корректное заполнение всех полей"""
        scheme = 1
        username = self.generate_valid_username_field()
        email = self.generate_valid_email_field()
        password = self.generate_valid_password_field()
        return username, email, password, password, self.ACCEPT_FLAG_ON, scheme

    def scheme_2(self):
        """scheme = 2: Корректное заполнение всех полей кроме username"""
        scheme = 2
        username = self.generate_invalid_username_field_overflow()
        email = self.generate_valid_email_field(random=False)
        password = self.generate_valid_password_field()
        return username, email, password, password, self.ACCEPT_FLAG_ON, scheme

    def scheme_3(self):
        """
        scheme = 3:
        Корректное заполнение всех полей
        password = accepting_password = invalid
        """
        scheme = 3
        username = self.generate_valid_username_field()
        email = self.generate_valid_email_field(random=False)
        password = self.generate_invalid_password_field()
        return username, email, password, password, self.ACCEPT_FLAG_ON, scheme

    def scheme_4(self):
        """scheme = 4: Корректное заполнение всех полей кроме email(длинный)"""
        scheme = 4
        username = self.generate_valid_username_field()
        email = self.generate_invalid_email_field_length(overflow=True)
        password = self.generate_valid_password_field()
        return username, email, password, password, self.ACCEPT_FLAG_ON, scheme

    def scheme_5(self):
        """scheme = 5: Корректное заполнение всех полей, флаг принятия не выставлен"""
        scheme = 5
        username = self.generate_valid_username_field()
        email = self.generate_valid_email_field(random=False)
        password = self.generate_valid_password_field()
        return username, email, password, password, self.ACCEPT_FLAG_OFF, scheme

    def scheme_6(self):
        """scheme = 6: Корректное заполнение всех полей кроме, подтверждение пароля не заполнино"""
        scheme = 6
        username = self.generate_valid_username_field()
        email = self.generate_valid_email_field(random=False)
        password = self.generate_valid_password_field()
        return username, email, password, "", self.ACCEPT_FLAG_ON, scheme

    def scheme_7(self):
        """scheme = 7: Флаг выставлен, все поля заполнены некорректно"""
        scheme = 7
        username = self.generate_invalid_username_field_overflow()
        email = self.generate_invalid_email_field_length(overflow=True)
        password = self.generate_invalid_password_field()
        return username, email, password, "", self.ACCEPT_FLAG_ON, scheme


data_generator = DataGenerator()

VALIDATION_DATA = [
    data_generator.scheme_1(),
    data_generator.scheme_2(),
    data_generator.scheme_3(),
    data_generator.scheme_4(),
    data_generator.scheme_5(),
    data_generator.scheme_6(),
    data_generator.scheme_7()
]
print(VALIDATION_DATA)
