from django.shortcuts import render, redirect
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Books
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class KitapListesi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'kitaplarlistesi.html'
    style = {'template_pack': 'rest_framework/vertical/'}


    def get(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializers(queryset)
        return Response({'serializer':serializer, 'queryset':queryset, 'style': self.style})
    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'style': self.style})
        serializer.save()
        return redirect('Books:kitaplar')

class KitapDetay(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'kitapdetay.html'

    def get_object(self, id):
        try:
            return Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = BookSerializers(queryset)
        return Response({'serializer':serializer, 'queryset':queryset})

    def post(self, request, id):
            
        queryset = get_object_or_404(Books, id=id)
        serializer = BookSerializers(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'queryset': queryset})
        serializer.save()
        return redirect('Books:kitaplar')

    def put(self, request):
        cari = self.get_object(id)
        serializer = BookSerializers(cari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cari = self.get_object(id)
        cari.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenericBooksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = BookSerializers
    queryset = Books.objects.all()
    lookup_field = 'id'

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'kitaplarlistesi2.html'
    style = {'template_pack': 'rest_framework/vertical/'}
    
    #authentication_classes=[SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request, id=None):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)