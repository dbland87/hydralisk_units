# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.migrations import serializer
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from units.models import Unit
from units.serializers import UnitSerializer
from user_auth.models import Bag


class RequestUnits(APIView):
    def post(self, request, format=None):
        #Check if user exists
        data = JSONParser().parse(request)
        bag_id = data['user']['bag']
        if Bag.objects.filter(id = bag_id).exists():
            #Grab all units in that bag
            units = Unit.objects.filter(bag=bag_id)
            serializer = UnitSerializer(units, many=True)
            return Response({"bag" : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



