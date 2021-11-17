from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Avg, Max
from rest_framework.permissions import IsAuthenticated
from ca.api.serializers import DonateurSerializer, DonsSerializer, PromesseDonsSerializer
from django.http.response import HttpResponse
from django.template import loader
from django.views.generic.base import ContextMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from ca.models import Donateur, Dons, Cathegorie, Promesse_dons, Mensualite
from django.utils import timezone
from django.views.generic import ListView, DetailView
from ca.api.forms import DonateurCreateForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.db.models import Sum
  
      
# class DonateurListView(ListView):   
   
#    model = Donateur
#    paginate_by = 10  # if pagination is desired

    
#    def index(request):
    
#     donateur_list= Donateur.objects.order_by('-created_at')[:5]
#     template = loader.get_template('ca/donateur_list.html')
#     form = DonateurCreateForm(request.POST or None)
    
#     context = {
#         'dernier_donateur_list': donateur_list,
#         'form' : form
#     }
#     return HttpResponse(template.render(context, request))

class DonateurListAPIView(APIView):
    
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/donateur_list.html'
    

    def get(self, request):
            queryset = Donateur.objects.all().order_by('-created_at')
            return Response({'donateur_list': queryset})
    
    def post(self, request):
        serializer=DonateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        donateur= self.get_object(pk)
        serializer=DonateurSerializer(donateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        donateur = self.get_object(pk)
        donateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonateurDetail(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/donateurl_detail.html'

    def get(self, request, pk):
        donateur = get_object_or_404(Donateur, pk=pk)
        serializer = DonateurSerializer(donateur)
        return Response({'serializer': serializer, 'donateur': donateur})

    def post(self, request, pk):
        donateur = get_object_or_404(Donateur, pk=pk)
        serializer = DonateurSerializer(donateur, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'donateur': donateur})
        serializer.save()
        return redirect('donateur-list')

class DonateurCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/donateur_list.html'
    
    def get(self, request):
        donateur = Donateur.objects.all()
        serializer=DonateurSerializer(donateur,  context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer=DonateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('donateur-list')
# fin fonction donateur 

# debut fonction dons 

class PromesseDonsListAPIView(APIView):
    
    permission_classes = (IsAuthenticated,)    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/promesse_list.html'
    
    # def get(self, request):
    #     promesse = Promesse_dons.objects.all()().order_by('-created_at')
    #     serializer=PromesseDonsSerializer(promesse,
    #                                     many=True,
    #                                     context={'request': request})
    #     return Response({'promesse_list': promesse})
      
    def get(self, request):
          queryset = Promesse_dons.objects.all().order_by('-created_at')
          nbrPromese = Promesse_dons.objects.count()
          nbrdonateur = Donateur.objects.all()
          cathegorie = Cathegorie.objects.all()
          montantrPromese = Promesse_dons.objects.all().aggregate(total_prom=Sum('cathegorie'))
          return Response({
              
              'promesse_list': queryset,
              'nbrPromesse': nbrPromese,
              'donateurscrol':nbrdonateur,
              'montant':cathegorie,
              'montanttotal': montantrPromese
                           
                           })
    
    def post(self, request):
        serializer=PromesseDonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        promesse= self.get_object(pk)
        serializer=PromesseDonsSerializer(promesse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        promesse = self.get_object(pk)
        promesse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PromesseCreateApiView(APIView):
    
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/promesse_list.html'
    
    def get(self, request):
        promesse = Promesse_dons.objects.all()
        serializer=PromesseDonsSerializer(promesse,  context={'request': request})
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer=PromesseDonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('promesse-list')    
    


class DonsListAPIView(APIView):
    
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/don_list.html'
    
    # def get(self, request):
    #     promesse = Promesse_dons.objects.all()().order_by('-created_at')
    #     serializer=PromesseDonsSerializer(promesse,
    #                                     many=True,
    #                                     context={'request': request})
    #     return Response({'promesse_list': promesse})
      
    def get(self, request):
          queryset = Dons.objects.all().order_by('-created_at')
          nbrdonateur = Donateur.objects.all()
          mois = Mensualite.objects.all()
        #   montantDons = Dons.objects.all().aggregate(total_amount=Sum('montant'))
          nbrdedons = Dons.objects.count()
          montantDons = Dons.objects.all().aggregate(total_amount=Sum('montant'))

          return Response({
              
                'dons_list': queryset,
                #   'nbrPromesse': nbrPromese,
                'donateurscrol':nbrdonateur,
                'periode':mois,
                'montant': montantDons,
                'nbrdon': nbrdedons
                           
                           })
    
    def post(self, request):
        serializer=PromesseDonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        promesse= self.get_object(pk)
        serializer=PromesseDonsSerializer(promesse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        promesse = self.get_object(pk)
        promesse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DonCreateApiView(APIView):
    
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ca/don_list.html'
    
    def get(self, request):
        don = Dons.objects.all()
        serializer=DonsSerializer(don,  context={'request': request})
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer=DonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('dons-list')  
        

# class ArticleDetailAPIView(APIView):
    
#     def get_object(self, pk):
#         article = get_object_or_404(Article, pk=pk)
#         return article
    
#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         article= self.get_object(pk)
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request,pk):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class JournalistListCreateApiiView(APIView):
    
#     def get(self, request):
#         journalist = Journalist.objects.all()
#         serializer=JournalistSerializer(journalist,
#                                         many=True,
#                                         context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer=JournalistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
# @api_view(["GET", "POST"])
# def article_list_create_api_view(request):
#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(["GET", "PUT" , "DELETE"])
# def article_detail_api_view(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error": {
#                             "code":404,
#                             "message":"Article not found!"
#                         }}, status=status.HTTP_404_NOT_FOUND)
#     if request.method=="GET":
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
        
#     elif request.method=="PUT":
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method =="DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            
