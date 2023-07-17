from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter
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

            user = self.request.user
            user_coordinate = user.coordinate.last()
            start_point = user_coordinate.longitude, user_coordinate.latitude

            result.append(user.pk)

            participants = queryset.exclude(pk=user.pk)

            for participant in participants:
                participant_coordinate = participant.coordinate.last()
                end_point = participant_coordinate.longitude, participant_coordinate.latitude

                distance = Distance().count_distance(start_point, end_point)

                if distance >= value:
                    result.append(participant.pk)

            return queryset.exclude(pk__in=result)

        return queryset

    class Meta:
        model = User
        fields = ['sex', 'first_name', 'last_name', 'distance']
