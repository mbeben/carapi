from rest_framework import mixins, viewsets


class CreateDestroyModelViewset(mixins.ListModelMixin, mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    """
    A viewset that provides `create`, `list`, and `destroy` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
