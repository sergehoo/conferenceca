from datetime import datetime,timezone
from django.utils.timesince import timesince
from rest_framework import serializers
from ca.models import Donateur, Cathegorie , Mensualite, Promesse_dons,Dons




class DonateurSerializer(serializers.ModelSerializer):
    
    time_since_publication=serializers.SerializerMethodField()
    #author = JournalistSerializer(read_only=True)
    
    class Meta:
        model = Donateur
        exclude=("id",)
        #fields = '__all__' #all the fields
    
    def get_time_since_publication(self, object):
        publication_date = object.created_at
        now = datetime.now(timezone.utc)
        time_delta = timesince(publication_date, now)
        return time_delta
    
   
    
class DonsSerializer(serializers.ModelSerializer):
  #  Dons = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Dons
        fields="__all__"
        
class CathegorieSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Cathegorie
        fields = '__all__' #all the fields
        

class MensualiteSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Mensualite
        fields = '__all__' #all the fields


class PromesseDonsSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Promesse_dons
        fields = '__all__' #all the fields