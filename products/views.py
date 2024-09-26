from authentication.permission import GlobalPermissionClass
from rest_framework.filters import SearchFilter
from .serializers import ProductsSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.generics import (

    # Admins
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,

    # Clients
    ListAPIView,
    RetrieveAPIView
)


from rest_framework.views import APIView


class ProductsListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'seller__enterprise_name', 'genres__name']
    


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'seller__enterprise_name', 'genres__name']  



class ProductsGenericView(APIView):

    def get(self, request):
        produtos = Product.objects.prefetch_related('filhos')  # 'filhos' é o related_name em Review

        avaliacoes = []
        for produto in produtos:
            avaliacoes_do_produto = produto.filhos.all()
            for avaliacao in avaliacoes_do_produto:
                avaliacoes.append({
                    'product': produto.name,
                    'user': avaliacao.user.username,
                    'rate': avaliacao.rate,
                    'date': avaliacao.date
                })

        return Response(data={'avaliacoes': avaliacoes}, status=HTTP_200_OK)





class ProductsRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer



class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer
    
    