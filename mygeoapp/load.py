from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import PosteHtaBt,CoffretDisjoncteurBt,LiaisonBt,TransfoHtaBt,LiaisonHta,TableauDistributionHta,TableauDistributionBt,DepartBt,NoeudBt,DerivationBt,BranchementBt,PointAncrageBt,SupportBt,TableauComptage,TerrainPoste,InstallationPv
import pandas as pd
from django.db import models
from django.contrib.gis.db import models as gis_models
from osgeo import ogr
from django.contrib.gis.geos import GEOSGeometry


mapping2 = {
    'id_pt' : 'id_pt',
    'code_pt' : 'code_pt',
    'nom_pt' : 'nom_pt',
    'ur' :'ur',
    'uf':'uf',
    'ut' :'ut',
    'gouv' :'gouv', 
    'deleg' :'deleg',
    'localite' :'localite',
    'gto_pt' :'gto_pt',
    'dep_hta' :'dep_hta',
    'gto_dep' :'gto_dep',
    'deriv_prin' :'deriv_prin',
    'fonct_pt' :'fonct_pt',
    'etat_pt' :'etat_pt',
    'type_pt':'type_pt',
    'phase_racc' :'phase_racc',
    'struct_pt' :'struct_pt',
    'u_prim' :'u_prim_kv',
    'u_sec' :'u_sec_v',
    'mod_racc' :'mod_racc',
    'nb_transf' :'nb_transf',
    'pui_kva' :'pui_kva',
    'nb_dep_tot' :'nb_dep_tot',
    'sect_fusib' :'sect_fusib',
    'type_paraf' :'type_paraf',
    'telecomm' :'telecomm',
    'racc_bcc' :'racc_bcc',
    'pre_ild' :'pre_ild',
    'type_comp': 'type_comp',
    'milieu' :'milieu',
    'dms' :'dms',
    'sch_unif':'sch_unif',
    'photo' :'photo',
    'surf_pt' :'surf_m2',
    'x_cent' :'x_cent',
    'y_cent' :'y_cent',
    'geom_pt' :'Polygon',
    'cree_par' :'cree_par',
    'cree_le' :'cree_le',
    'maj_par' :'maj_par',
    'maj_le' :'maj_le',
    'dist_par':'dist_par',
    'dist_le' :'dist_le',
    'ddsf_par' :'ddsf_par',
    'ddsf_le':'ddsf_le',
    'sigt_par': 'sigt_par',
    'sigt_le' :'sigt_le',
    'obs' :'obs',
}


def run(verbose=True):
    lm = LayerMapping(PosteHtaBt,'C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/poste_hta_bt.shp',
        mapping2 ,
        transform=False)
    lm.save(verbose=verbose)



def run1():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/coffret_disjoncteur_bt.xlsx')
    code_leb_instances = {leb.code_leb.strip(): leb for leb in LiaisonBt.objects.all()}
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    # Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        code_leb_value = row['code_leb']

        if code_leb_value is not None:
            code_leb_instance = code_leb_instances.get(str(code_leb_value).strip())
        else:
            code_leb_instance = None
        
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None

        my_model = CoffretDisjoncteurBt(id_cdb=row['id_cdb'],
            code_cdb=row['code_cdb'],
            code_pt=code_pt_instance,
            code_leb=code_leb_instance,
            type_coff=row['type_coff'],
            nb_dep_bt=row['nb_dep_bt'],
            marq_disj=row['marq_disj'],
            type_disj=row['type_disj'],
            calib_disj=row['calib_disj'],
            photo=row['photo'],
            cree_par=row['cree_par'],
            cree_le=row['cree_le'],
            maj_par=row['maj_par'],
            maj_le=row['maj_le'],
            dist_par=row['dist_par'],
            dist_le=row['dist_le'],
            ddsf_par=row['ddsf_par'],
            ddsf_le=row['ddsf_le'],
            sigt_par=row['sigt_par'],
            sigt_le=row['sigt_le'],
            obs=row['obs'])
        my_model.save()



def run2():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/liaison_bt.xlsx')
    code_tra_instances = {tra.code_tra.strip(): tra for tra in TransfoHtaBt.objects.all()}
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        code_tra_value = row['code_tra']
        if code_tra_value is not None:
            code_tra_instance = code_tra_instances.get(str(code_tra_value).strip())
        else:
            code_tra_instance = None
        
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        print(code_pt_instance)
        print(code_tra_instance)
        my_model = LiaisonBt(id_leb=row['id_leb'], code_leb=row['code_leb'],nat_cond1=row['nat_cond1'],nat_cond2=row['nat_cond2'],nat_cond3=row['nat_cond3'],nat_cond4=row['nat_cond4'],sect_ph=row['sect_ph'],sect_n=row['sect_n'],cree_par=row['cree_par'],cree_le=row['cree_le'],maj_par=row['maj_par'],dist_par=row['dist_par'],dist_le=row['dist_le'],ddsf_par=row['ddsf_par'],ddsf_le=row['ddsf_le'],sigt_par=row['sigt_par'],sigt_le=row['sigt_le'],obs=row['obs'],code_pt=code_pt_instance,code_tra=code_tra_instance)
        my_model.save()
    

def run3():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/transfo_hta_bt.xlsx')
    code_leh_instances = {leh.code_leh.strip(): leh for leh in LiaisonHta.objects.all()}
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        code_leh_value = row['code_leh']
        if code_leh_value is not None:
            code_leh_instance = code_leh_instances.get(str(code_leh_value).strip())
        else:
            code_leh_instance = None
        
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        print(code_pt_instance)
        my_model = TransfoHtaBt(id_tra=row['id_tra'], code_tra=row['code_tra'],pui_kva=row['puiss_kva'],type_tra=row['type_tra'],marque_tra=row['marque_tra'],n_serie_tra=row['n_seri_tra'],annee_fab=row['annee_fab'],racc_hta=row['racc_hta'],photo=row['photo'],cree_par=row['cree_par'],cree_le=row['cree_le'],maj_par=row['maj_par'],maj_le=row['maj_le'],dist_par=row['dist_par'],dist_le=row['dist_le'],ddsf_par=row['ddsf_par'],ddsf_le=row['ddsf_le'],sigt_par=row['sigt_par'],sigt_le=row['sigt_le'],obs=row['obs'],code_pt=code_pt_instance,code_leh=code_leh_instance)
        my_model.save()

def run4():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/liaison_hta.xlsx')
    code_tdh_instances = {tdh.code_tdh: tdh for tdh in TableauDistributionHta.objects.all()}
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    print(code_pt_instances)
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        print(str(code_pt_value))
        code_tdh_value = row['code_tdh']
        if code_tdh_value is not None:
            code_tdh_instance = code_tdh_instances.get(code_tdh_value)
        else:
            code_tdh_instance = None
        
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        print(code_pt_instance)
        
        my_model = LiaisonHta(id_leh=row['id_leh'], code_leh=row['code_leh'],sect_ph=row['sect_ph'],type_cond=row['type_cond'],metal_cond=row['metal_cond'],long_m=row['long_m'],cree_par=row['cree_par'],cree_le=row['cree_le'],maj_par=row['maj_par'],maj_le=row['maj_le'],dist_par=row['dist_par'],dist_le=row['dist_le'],ddsf_par=row['ddsf_par'],ddsf_le=row['ddsf_le'],sigt_par=row['sigt_par'],obs=row['obs'],code_pt=code_pt_instance ,code_tdh=code_tdh_instance)
        my_model.save()

def run5():
    # Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/tableau_distribution_hta.xlsx')
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    print(code_pt_instances)
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        print(str(code_pt_value))

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        print(code_pt_instance)
        
        my_model = TableauDistributionHta(
            id_tdh=row['id_tdh'],
            code_tdh=row['code_tdh'],
            code_pt=code_pt_instance,
            type_tdh=row['type_tdh'],
            config_tdh=row['config_tdh'],
            marque_tdh=row['marque_tdh'],
            ref_tdh=row['ref_tdh'],
            isol_jdb=row['isol_jdb'],
            type_cell=row['type_cell'],
            cmd_cell=row['cmd_cell'],
            mq_inters=row['mq_inters'],
            sect_jdb=row['sect_jdb'],
            isola_jdb=row['isola_jdb'],
            num_serie1=row['num_serie1'],
            obs=row['obs'],
            num_serie2=row['num_serie2'],
            num_serie3=row['num_serie3'],
            num_serie4=row['num_serie4'],
            num_serie5=row['num_serie5'],
            num_serie6=row['num_serie6'],
            annee_fab=row['annee_fab'],
            photo=row['photo'],
            cree_par=row['cree_par'],
            cree_le=row['cree_le'],
            maj_par=row['maj_par'],
            maj_le=row['maj_le'],
            dist_par=row['dist_par'],
            dist_le=row['dist_le'],
            ddsf_par=row['ddsf_par'],
            ddsf_le=row['ddsf_le'],
            sigt_par=row['sigt_par'])
        my_model.save()


def run6():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/tableau_distribution_bt.xlsx')
    code_leb_instances = {leb.code_leb.strip(): leb for leb in LiaisonBt.objects.all()}
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        code_leb_value = row['code_leb']
        if code_leb_value is not None:
            code_leb_instance = code_leb_instances.get(str(code_leb_value).strip())
        else:
            code_leb_instance = None
        
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        my_model = TableauDistributionBt(
            id_tdb=row['id_tdb'],
            code_tdb=row['code_tdb'],
            type_tdb=row['type_tdb'],
            nb_dep_tot=row['nb_dep_tot'],
            nb_dep_aff=row['nb_dep_aff'],
            marque_tdb=row['marque_tdb'],
            num_serie=row['num_serie'],
            annee_fab=row['annee_fab'],
            photo=row['photo'],
            cree_par=row['cree_par'],
            cree_le=row['cree_le'],
            maj_par=row['maj_par'],
            maj_le=row['maj_le'],
            dist_par=row['dist_par'],
            dist_le=row['dist_le'],
            ddsf_par=row['ddsf_par'],
            ddsf_le=row['ddsf_le'],
            sigt_par=row['sigt_par'],
            sigt_le=row['sigt_le'],
            code_pt=code_pt_instance,
            obs=row['obs'],
            code_leb = code_leb_instance)
        my_model.save()




def run7(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    code_tdb_instances = {tdb.code_tdb.strip(): tdb for tdb in TableauDistributionBt.objects.all()}
    code_cdb_instances = {cdb.code_cdb.strip(): cdb for cdb in CoffretDisjoncteurBt.objects.all()}
    code_nda_instances = {nda.code_nod.strip(): nda for nda in NoeudBt.objects.all()}
    code_ndav_instances = {ndav.code_nod.strip(): ndav for ndav in NoeudBt.objects.all()}
    
  
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/depart_bt.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')
        code_tdb_value = feature.GetField('code_tdb')
        code_cdb_value = feature.GetField('code_cdb')
        code_nda_value = feature.GetField('nd_amont')
        code_ndav_value = feature.GetField('nd_aval')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None  

        if code_tdb_value is not None:
            code_tdb_instance = code_tdb_instances.get(str(code_tdb_value).strip())
        else:
            code_tdb_instance = None      

        if code_cdb_value is not None:
            code_cdb_instance = code_cdb_instances.get(str(code_cdb_value).strip())
        else:
            code_cdb_instance = None      

        if code_nda_value is not None:
            code_nda_instance = code_nda_instances.get(str(code_nda_value).strip())
        else:
            code_nda_instance = None  

        if code_ndav_value is not None:
            code_ndav_instance = code_ndav_instances.get(str(code_ndav_value).strip())
        else:
            code_ndav_instance = None  

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = DepartBt(
            id_dep=feature.GetField('id_dep'),
            code_dep=feature.GetField('code_dep'),
            nom_dep=feature.GetField('nom_dep'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            nat_res_bt=feature.GetField('nat_res_bt'),
            type_tronc=feature.GetField('type_tronc'),
            sect_ph=feature.GetField('sect_ph'),
            sect_n=feature.GetField('sect_n'),
            metal_cond=feature.GetField('metal_cond'),
            long_m=feature.GetField('long_m'),
            geom_line=geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le=feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            sigt_le=feature.GetField('sigt_le'),
            obs=feature.GetField('obs'),
            code_pt = code_pt_instance ,
            code_tdb = code_tdb_instance ,
            code_cdb = code_cdb_instance ,
            nd_amont = code_nda_instance ,
            nd_aval = code_ndav_instance )
        objet.save()


def run8(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
  
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/nd.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None  
 

        geometry_ogr = feature.GetGeometryRef()
        if geometry_ogr:
            geometry_wkt = geometry_ogr.ExportToWkt()
            geos_geometry = GEOSGeometry(geometry_wkt)  
        else:
            print("No valid geometry found for this feature.")

    # Créer un objet de modèle avec les champs du feature
        objet = NoeudBt(
            id_nod=feature.GetField('id_nod'),
            code_nod=feature.GetField('code_nod'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            localite=feature.GetField('localite'),
            eqt_nod=feature.GetField('eqt_nod'),
            cal_fus=feature.GetField('cal_fus'),
            sortie_pt=feature.GetField('sortie_pt'),
            derivation=feature.GetField('derivation'),
            branch=feature.GetField('branch'),
            chgt_carac=feature.GetField('chgt_carac'),
            bout_res=feature.GetField('bout_res'),
            aero_st=feature.GetField('aero_st'),
            limit_dist=feature.GetField('limit_dist'),
            pl_ind=feature.GetField('pl_ind'),
            pl_col=feature.GetField('pl_col'),
            autre=feature.GetField('autre'),
            nb_etage=feature.GetField('nb_etage'),
            sect_col=feature.GetField('sect_col'),
            long_col=feature.GetField('long_col'),
            marq_coff=feature.GetField('marq_coff'),
            nb_compt=feature.GetField('nb_compt'),
            x_32632=feature.GetField('x_32632'),
            y_32632=feature.GetField('y_32632'),
            geom_point=geos_geometry ,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le=feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            sigt_le=feature.GetField('sigt_le'),
            obs=feature.GetField('obs'),
            code_pt = code_pt_instance )
        
        objet.save()


def run9(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    code_dep_instanes =  {dep.code_dep.strip(): dep for dep in DepartBt.objects.all()}
    code_nda_instances = {nda.code_nod.strip(): nda for nda in NoeudBt.objects.all()}
    code_ndav_instances = {ndav.code_nod.strip(): ndav for ndav in NoeudBt.objects.all()}
    
  
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/derivation_bt.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')
        code_dep_value = feature.GetField('code_dep')
        code_nda_value = feature.GetField('nd_amont')
        code_ndav_value = feature.GetField('nd_aval')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None  
    
        if code_dep_value is not None:
            code_dep_instance = code_dep_instanes.get(str(code_dep_value).strip())
        else:
            code_dep_instance = None  

        if code_nda_value is not None:
            code_nda_instance = code_nda_instances.get(str(code_nda_value).strip())
        else:
            code_nda_instance = None  

        if code_ndav_value is not None:
            code_ndav_instance = code_ndav_instances.get(str(code_ndav_value).strip())
        else:
            code_ndav_instance = None  

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = DerivationBt(
            id_der=feature.GetField('id_der'),
            code_der=feature.GetField('code_der'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            nat_cond=feature.GetField('nat_cond'),
            nat_res_bt=feature.GetField('nat_res_bt'),
            type_tronc=feature.GetField('type_tronc'),
            sect_ph=feature.GetField('sect_ph'),
            sect_n=feature.GetField('sect_n'),
            metal_cond=feature.GetField('metal_cond'),
            type_cond = feature.GetField('type_cond'),
            long_m=feature.GetField('long_m'),
            geom_line=geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le=feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            sigt_le=feature.GetField('sigt_le'),
            obs=feature.GetField('obs'),
            code_pt = code_pt_instance ,
            code_dep = code_dep_instance ,
            nd_amont = code_nda_instance ,
            nd_aval = code_ndav_instance )
        objet.save()


def run10(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    code_dep_instanes =  {dep.code_dep.strip(): dep for dep in DepartBt.objects.all()}
    code_der_instances = {der.code_der.strip(): der for der in DerivationBt.objects.all()}
    code_nda_instances = {nda.code_nod.strip(): nda for nda in NoeudBt.objects.all()}
    code_ndav_instances = {ndav.code_nod.strip(): ndav for ndav in NoeudBt.objects.all()}
    
  
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/branchement_bt.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')
        code_dep_value = feature.GetField('code_dep')
        code_der_value = feature.GetField('code_der')
        code_nda_value = feature.GetField('nd_amont')
        code_ndav_value = feature.GetField('nd_aval')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None  
    
        if code_der_value is not None:
            code_der_instance = code_der_instances.get(str(code_der_value).strip())
        else:
            code_der_instance = None 
 
        if code_dep_value is not None:
            code_dep_instance = code_dep_instanes.get(str(code_dep_value).strip())
        else:
            code_dep_instance = None  

        if code_nda_value is not None:
            code_nda_instance = code_nda_instances.get(str(code_nda_value).strip())
        else:
            code_nda_instance = None  

        if code_ndav_value is not None:
            code_ndav_instance = code_ndav_instances.get(str(code_ndav_value).strip())
        else:
            code_ndav_instance = None  

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = BranchementBt(
            id_bra=feature.GetField('id_bri'),
            code_bra=feature.GetField('code_bri'),
            num_aff=feature.GetField('num_aff'),
            type_bra=feature.GetField('type_bra'),
            nat_cond=feature.GetField('nat_cond'),
            nat_res=feature.GetField('nat_res_bt'),
            type_tronc=feature.GetField('type_tronc'),
            sect_ph=feature.GetField('sect_ph'),
            sect_n=feature.GetField('sect_n'),
            type_cond=feature.GetField('type_cond'),
            metal_cond=feature.GetField('metal_cond'),
            dms=feature.GetField('dms'),
            long_m=feature.GetField('long_m'),
            geom_line = geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le=feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            sigt_le=feature.GetField('sigt_le'),
            obs=feature.GetField('obs'),
            code_pt = code_pt_instance ,
            code_dep = code_dep_instance ,
            code_der = code_der_instance,
            nd_amont = code_nda_instance ,
            nd_aval = code_ndav_instance )
        objet.save()    


def run11(verbose=True):
    
    code_dep_instanes =  {dep.code_dep.strip(): dep for dep in DepartBt.objects.all()}
    code_der_instances = {der.code_der.strip(): der for der in DerivationBt.objects.all()}
    code_bra_instances= {bra.code_bra.strip(): bra for bra in BranchementBt.objects.all()}
  
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/point_ancrage_bt.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        
        code_dep_value = feature.GetField('code_dep')
        code_der_value = feature.GetField('code_der')
        code_bra_value = feature.GetField('code_bri')

        if code_bra_value is not None:
            code_bra_instance = code_bra_instances.get(str(code_bra_value).strip())
        else:
            code_bra_instance = None  
    
        if code_der_value is not None:
            code_der_instance = code_der_instances.get(str(code_der_value).strip())
        else:
            code_der_instance = None 
 
        if code_dep_value is not None:
            code_dep_instance = code_dep_instanes.get(str(code_dep_value).strip())
        else:
            code_dep_instance = None  

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = PointAncrageBt(
            id_anc=feature.GetField('id_pta'),
            code_anc=feature.GetField('code_pta'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            localite=feature.GetField('localite'),
            type_ancr=feature.GetField('type_anc'),
            nb_der=feature.GetField('nb_der'),
            nb_br=feature.GetField('nb_br'),
            x_32632=feature.GetField('x_32632'),
            y_32632=feature.GetField('y_32632'),
            geom_point = geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le=feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            sigt_le=feature.GetField('sigt_le'),
            obs=feature.GetField('obs'),
            code_bra = code_bra_instance ,
            code_dep = code_dep_instance ,
            code_der = code_der_instance)
        objet.save() 


def run12(verbose=True):
    code_dep_instanes =  {dep.code_dep.strip(): dep for dep in DepartBt.objects.all()}
    code_der_instances = {der.code_der.strip(): der for der in DerivationBt.objects.all()}
    code_bra_instances= {bra.code_bra.strip(): bra for bra in BranchementBt.objects.all()}
  
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/support_bt.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_dep_value = feature.GetField('code_dep')
        code_der_value = feature.GetField('code_der')
        code_bra_value = feature.GetField('code_bri')

        if code_bra_value is not None:
            code_bra_instance = code_bra_instances.get(str(code_bra_value).strip())
        else:
            code_bra_instance = None  
    
        if code_der_value is not None:
            code_der_instance = code_der_instances.get(str(code_der_value).strip())
        else:
            code_der_instance = None 
 
        if code_dep_value is not None:
            code_dep_instance = code_dep_instanes.get(str(code_dep_value).strip())
        else:
            code_dep_instance = None  

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = SupportBt(
            id_sup=feature.GetField('id_sup'),
            code_sup=feature.GetField('code_sup'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            localite=feature.GetField('localite'),
            nb_dep=feature.GetField('nb_dep'),
            nb_der=feature.GetField('nb_der'),
            nb_br=feature.GetField('nb_bri'),
            typ_sup=feature.GetField('type_sup'),
            etat_sup=feature.GetField('etat_sup'),
            access_sup = feature.GetField('access_sup'),
            mise_terre=feature.GetField('mise_terre'),
            ecl_public=feature.GetField('ecl_public'),
            ancr_fo=feature.GetField('anc_fo'),
            photo=feature.GetField('photo'),
            x_32632=feature.GetField('x_32632'),
            y_32632=feature.GetField('y_32632'),
            geom_point=geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par =feature.GetField('dist_par'),
            dist_le = feature.GetField('dist_le'),
            ddsf_par =feature.GetField('ddsf_par'),
            ddsf_le =feature.GetField('ddsf_le'),
            sigt_par = feature.GetField('sigt_par'),
            sigt_le = feature.GetField('sigt_le'),
            obs = feature.GetField('obs'),
            code_bra = code_bra_instance,
            code_der = code_der_instance,
            code_dep = code_dep_instance )
        objet.save() 


def run13(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    code_dep_instanes =  {dep.code_dep.strip(): dep for dep in DepartBt.objects.all()}
    code_der_instances = {der.code_der.strip(): der for der in DerivationBt.objects.all()}
    code_bra_instances = {bra.code_bra.strip(): bra for bra in BranchementBt.objects.all()}
    code_nod_instances = {nod.code_nod.strip(): nod for nod in NoeudBt.objects.all()}
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/tableau_comptage.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')
        code_dep_value = feature.GetField('code_dep')
        code_der_value = feature.GetField('code_der')
        code_bra_value = feature.GetField('code_br')
        code_nod_value = feature.GetField('code_nod')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None 

        if code_bra_value is not None:
            code_bra_instance = code_bra_instances.get(str(code_bra_value).strip())
        else:
            code_bra_instance = None  
    
        if code_der_value is not None:
            code_der_instance = code_der_instances.get(str(code_der_value).strip())
        else:
            code_der_instance = None 
 
        if code_dep_value is not None:
            code_dep_instance = code_dep_instanes.get(str(code_dep_value).strip())
        else:
            code_dep_instance = None  

        if code_nod_value is not None:
            code_nod_instance = code_nod_instances.get(str(code_nod_value).strip())
        else:
            code_nod_instance = None          

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

    # Créer un objet de modèle avec les champs du feature
        objet = TableauComptage(
            id_tc=feature.GetField('id_tc'),
            code_tc=feature.GetField('code_tc'),
            ur=feature.GetField('ur'),
            uf=feature.GetField('uf'),
            ut=feature.GetField('ut'),
            gouv=feature.GetField('gouv'),
            deleg=feature.GetField('deleg'),
            localite=feature.GetField('localite'),
            nom_dep=feature.GetField('nom_dep'),
            client=feature.GetField('client'),
            ref_client=feature.GetField('ref_client'),
            usage_tc=feature.GetField('usage_tc'),
            emplac_tc=feature.GetField('empla_tc'),
            acces_tc = feature.GetField('acces_tc'),
            adresse=feature.GetField('adresse'),
            type_tc=feature.GetField('type_tc'),
            marque_ctr=feature.GetField('marq_ctr'),
            num_serie=feature.GetField('num_serie'),
            tech_ctr=feature.GetField('tech_ctr'),
            nat_res=feature.GetField('nat_res'),
            phase_racc=feature.GetField('phase_racc'),
            type_br=feature.GetField('type_br'),
            rapport_tc_bt_et_mt_field=feature.GetField('rapport_tc'),
            rapport_tp_mt_field=feature.GetField('rapport_tp'),
            type_ctr=feature.GetField('type_ctr'),
            etat_ctr =feature.GetField('etat_ctr'),
            marq_disj = feature.GetField('marq_disj'),
            calib_disj =feature.GetField('calib_disj'),
            num_etage =feature.GetField('num_etage'),
            sect_col = feature.GetField('sect_col'),
            long_col = feature.GetField('long_col'),
            type_coff = feature.GetField('type_coff'),
            sect_desc =  feature.GetField('sect_desc'),
            long_desc =  feature.GetField('long_desc'),
            date_f_ctr =  feature.GetField('date_f_ctr'),
            dms_ctr = feature.GetField('dms_ctr'),
            x_32632 = feature.GetField('x_32632'),
            y_32632 = feature.GetField('y_32632'),
            geom_point = geometry,
            photo = feature.GetField('photo'),
            cree_par = feature.GetField('cree_par'),
            cree_le = feature.GetField('cree_le'),
            maj_par = feature.GetField('maj_par'),
            maj_le = feature.GetField('maj_le'),
            dist_par = feature.GetField('dist_par'),
            dist_le = feature.GetField('dist_le'),
            ddsf_par = feature.GetField('ddsf_par'),
            ddsf_le = feature.GetField('ddsf_le'),
            sigt_par = feature.GetField('sigt_par'),
            sigt_le = feature.GetField('sigt_le'),
            obs = feature.GetField('obs'),
            code_pt = code_pt_instance,
            code_dep = code_dep_instance,
            code_bra = code_bra_instance,
            code_der = code_der_instance,
            code_nod = code_nod_instance)
        objet.save() 



def run14(verbose=True):
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    
    shapefile = ogr.Open('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/terrain_poste.shp') 
    layer = shapefile.GetLayer()
    for feature in layer:
        code_pt_value = feature.GetField('code_pt')

        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None           

        geometry = GEOSGeometry(feature.GetGeometryRef().ExportToWkt())

        # Créer un objet de modèle avec les champs du feature
        objet = TerrainPoste(
            id_ter=feature.GetField('id_ter'),
            code_ter=feature.GetField('code_ter'),
            titre_fonc=feature.GetField('titre_fonc'),
            etat_fonc=feature.GetField('etat_fonc'),
            surf_ter=feature.GetField('surf_m2'),
            x_cent=feature.GetField('x_cent'),
            y_cent=feature.GetField('y_cent'),
            geom_poly= geometry,
            cree_par=feature.GetField('cree_par'),
            cree_le=feature.GetField('cree_le'),
            maj_par=feature.GetField('maj_par'),
            maj_le=feature.GetField('maj_le'),
            dist_par=feature.GetField('dist_par'),
            dist_le = feature.GetField('dist_le'),
            ddsf_par=feature.GetField('ddsf_par'),
            ddsf_le=feature.GetField('ddsf_le'),
            sigt_par=feature.GetField('sigt_par'),
            obs=feature.GetField('obs'),
            code_pt=code_pt_instance)
        objet.save() 

def run15():# Charger les données depuis le fichier Excel dans un dataframe Pandas
    df = pd.read_excel('C:/Users/MSI/Desktop/ressources_pfe/Livraison_MAHRES/installation_pv.xlsx')
    code_pt_instances = {pt.code_pt.strip(): pt for pt in PosteHtaBt.objects.all()}
    code_tc_instances = {tc.code_tc.strip(): tc for tc in TableauComptage.objects.all()}
# Itérer sur chaque ligne du dataframe et créer un objet MyModel pour chaque ligne
    for index, row in df.iterrows():
        code_pt_value = row['code_pt']
        code_tc_value = row['code_tc']
        if code_pt_value is not None:
            code_pt_instance = code_pt_instances.get(str(code_pt_value).strip())
        else:
            code_pt_instance = None
        

        if code_tc_value is not None:
            code_tc_instance = code_tc_instances.get(str(code_tc_value).strip())
        else:
            code_tc_instance = None
        
        my_model = InstallationPv(
            id_pv=row['id_pv'],
            code_ipv = row['code_ipv'],
            code_pt = code_pt_instance,
            ur=row['ur'],
            uf=row['uf'],
            ut=row['ut'],
            gouv=row['gouv'],
            deleg=row['deleg'],
            localite=row['localite'],
            puiss_inst=row['puiss_inst'],
            marq_ond=row['marq_ond'],
            sup_panel=row['sup_panel'],
            stockage=row['stockage'],
            cree_par=row['cree_par'],
            cree_le=row['cree_le'],
            maj_par=row['maj_par'],
            maj_le=row['maj_le'],
            dist_par=row['dist_par'],
            dist_le=row['dist_le'],
            ddsf_par=row['ddsf_par'],
            ddsf_le=row['ddsf_le'],
            sigt_par=row['sigt_par'],
            sigt_le=row['sigt_le'],
            obs=row['obs'],
            code_tc = code_tc_instance)
        my_model.save()