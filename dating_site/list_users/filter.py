from django.contrib.auth import get_user_model
from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet
from list_users.services.count_distance import Distance

User = get_user_model()


class MyFilter(FilterSet):
    distance = NumberFilter(field_name='coordinate',
                            method='count_distance',
                            lookup_expr='icontains')

    def count_distance(self, queryset, field_name, value: int):
        """
        Функция фильтрует пользователей по расстоянию
        """

        if value:
            excluded_users = []

            current_user = self.request.user
            start_point = self._get_user_coordinate(current_user)

            if start_point:

                excluded_users.append(current_user.pk)

                target_users = queryset.exclude(pk=current_user.pk)

                for target_user in target_users:

                    end_point = self._get_user_coordinate(target_user)

                    distance = Distance().count_distance(start_point, end_point)

                    if distance >= value:
                        excluded_users.append(target_user.pk)

                return queryset.exclude(pk__in=excluded_users)

        return queryset

    class Meta:
        model = User
        fields = ['sex', 'first_name', 'last_name', 'distance']

    def _get_user_coordinate(self, user):
        """
        Функция возвращает координаты пользователя
        """
        user_coordinate = user.coordinate.last()

        if user_coordinate:
            start_point = user_coordinate.longitude, user_coordinate.latitude
            return start_point
        else:
            print(f'Координата пользователя {user} не определена')
            return None
