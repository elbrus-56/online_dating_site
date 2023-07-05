from geopy.distance import great_circle


class Distance:

    def count_distance(self, point_from: tuple, point_to: tuple) -> int:
        """
        Функция рассчитывает расстояние между двумя координатами,
        Используя расстояние по дуге большого круга

        :param point_from: Координаты начала отсчета
        :param point_to: Координаты конечной точки
        :return: Расстояние в километрах
        """

        return great_circle(point_from, point_to).km
