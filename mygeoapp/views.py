from django.shortcuts import render
from .models import SupportBt,BranchementBt,PosteHtaBt,DepartBt,DerivationBt,PointAncrageBt,TableauComptage
import json
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

def index (request): 
    #support 
    points = SupportBt.objects.all()
    markers = []
    for point in points:
        lat, lon = point.geom_point.y, point.geom_point.x  
        markers.append({'lat': lat, 'lon': lon, 'name': point.code_sup})
    markers_json = json.dumps(markers)

    # branchement lignes
    lines = BranchementBt.objects.all()
    lines_2=[]
    for line in lines:
        geometriedeslines = line.geom_line
        geometriedeslinesjson = GEOSGeometry(geometriedeslines).geojson
        lines_2.append({'coord' : geometriedeslinesjson, 'name': line.code_bra})
    lines_json = json.dumps(lines_2)
    
    #poste hta bt 
    poste = PosteHtaBt.objects.all()
    postes=[]
    for post in poste :
        geomposte = post.geom_pt
        geometrieposte = GEOSGeometry(geomposte).geojson
        postes.append({'coord' : geometrieposte , 'name' : post.code_pt})
    poste_json = json.dumps(postes)

    #les lignes départs 

    depart = DepartBt.objects.all()
    departs = []
    for dep in depart :
        geom_dep = dep.geom_line
        geom_dep_json = GEOSGeometry(geom_dep).geojson
        departs.append({'coord' : geom_dep_json, 'name' : dep.code_dep})
    depart_json = json.dumps(departs)

    #les lignes derivation 

    derivation = DerivationBt.objects.all()
    derivations = []
    for der in derivation :
        geom_der = der.geom_line
        geom_der_json = GEOSGeometry(geom_der).geojson
        derivations.append({'coord' : geom_der_json, 'name' : der.code_der})
    derivation_json = json.dumps(derivations)

    #pt d'ancrage 

    ancrage = PointAncrageBt.objects.all()
    ancrages = []
    for anc in ancrage:
        lat_anc, lon_anc = anc.geom_point.y, anc.geom_point.x  
        ancrages.append({'lat_anc': lat_anc, 'lon_anc': lon_anc, 'name': anc.code_anc})
    ancrages_json = json.dumps(ancrages)

    #tableaux de comptages 

    comptage = TableauComptage.objects.all()
    comptages = []
    for com in comptage:
        lat_com, lon_com = com.geom_point.y, com.geom_point.x  
        comptages.append({'lat_com': lat_com, 'lon_com': lon_com, 'name': com.code_tc})
    comptage_json = json.dumps(comptages)

    return render(request,'index.html',{
        'markers_json': markers_json,
        'lines_json':lines_json,
        'poste_json' : poste_json,
        'depart_json' : depart_json,
        'derivation_json' : derivation_json,
        'ancrages_json' : ancrages_json,
        'comptage_json' : comptage_json,
        })

    