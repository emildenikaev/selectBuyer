import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли пользователь в БД"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Получаем id пользователя по его user_id в телеграме"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем пользователя в БД"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, operation):
        """Создаем запись выбора '-' - сайт, '+' - телеграм"""
        self.cursor.execute("INSERT INTO `records` (`user_id`, `operation`) VALUES (?, ?)",
                            (self.get_user_id(user_id), operation,))
        return self.conn.commit()

    def add_promo(self, user_id, promo):
        """Добавляем промокод при наличии"""
        self.cursor.execute("INSERT INTO `records` (`user_id`, `promo`) VALUES (?, ?)",
                            (self.get_user_id(user_id),
                             promo))
        return self.conn.commit()

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()
