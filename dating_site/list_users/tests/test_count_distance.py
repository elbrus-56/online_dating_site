from django.test import TestCase
from list_users.services.count_distance import Distance


class DistanceTest(TestCase):

    def setUp(self) -> None:
        self.coordinate_1 = ('55.188910', '61.332720')  # Члб
        self.coordinate_2 = ('55.182517', '61.292831')  # Члб 2
        self.coordinate_3 = ('55.710801', '37.607318')  # Мск

    def test_count_distance(self):
        """
        Сторонний сайт для рассчета расстояния по двум
        географическим координатам:
        https://calculatorium.ru/geography/distance-between-two-coordinates
        Для проверки правильности расчетов
        """

        res = Distance().count_distance(self.coordinate_1, self.coordinate_2)
        self.assertEqual(2.63, round(res, 2))
