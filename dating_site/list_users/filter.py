from django_filters.rest_framework import FilterSet
from django_filters import CharFilter, NumberFilter
from django.contrib.auth import get_user_model

from list_users.services.count_distance import Distance

User = get_user_model()


class MyFilter(FilterSet):
    distance = NumberFilter(field_name='coordinate', method='count_distance', lookup_expr='icontains')

    def count_distance(self, queryset, field_name, value):
        """
        Функция фильтрует пользователей по расстоянию
        """

        if value:
            result = []

            # Находим текущего пользователя и получаем его координаты
            user = queryset.get(email=self.request.user).coordinate
            start = user.longitude, user.latitude

            # Исключаем текущего пользователя
            result.append(user.id)

            # Получаем список оставшихся участников
            participants = queryset.exclude(id=user.id)

            for participant in participants:
                end = participant.coordinate.longitude, participant.coordinate.latitude

                # Считаем расстояние между пользователем и участником
                distance = Distance().count_distance(start, end)

                if distance >= value:
                    result.append(participant.id)

            return queryset.exclude(id__in=result)

        return queryset

    class Meta:
        model = User
        fields = ['sex', 'first_name', 'last_name', 'distance']
