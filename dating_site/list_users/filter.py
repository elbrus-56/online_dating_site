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

            try:
                current_user_coordinate = current_user.coordinate.last()
                start_point = current_user_coordinate.longitude, current_user_coordinate.latitude
            except Exception:
                print(f'Координата пользователя {current_user} не определена')

            excluded_users.append(current_user.pk)

            target_users = queryset.exclude(pk=current_user.pk)

            for target_user in target_users:
                try:
                    target_user_coordinate = target_user.coordinate.last()
                    end_point = target_user_coordinate.longitude, target_user_coordinate.latitude
                except Exception:
                    print(f'Координата участника {target_user} не определена')

                distance = Distance().count_distance(start_point, end_point)

                if distance >= value:
                    excluded_users.append(target_user.pk)

            return queryset.exclude(pk__in=excluded_users)

        return queryset

    class Meta:
        model = User
        fields = ['sex', 'first_name', 'last_name', 'distance']
