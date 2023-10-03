# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class BranchementBt(models.Model):
    id_bra = models.BigIntegerField(blank=True, null=True)
    code_bra = models.CharField(primary_key=True, max_length=50)
    num_aff = models.CharField(max_length=50, blank=True, null=True)
    type_bra = models.CharField(max_length=50, blank=True, null=True)
    nat_cond = models.CharField(max_length=50, blank=True, null=True)
    nat_res = models.CharField(max_length=50, blank=True, null=True)
    type_tronc = models.CharField(max_length=50, blank=True, null=True)
    sect_ph = models.BigIntegerField(blank=True, null=True)
    sect_n = models.BigIntegerField(blank=True, null=True)
    type_cond = models.CharField(max_length=50, blank=True, null=True)
    metal_cond = models.CharField(max_length=50, blank=True, null=True)
    dms = models.CharField(max_length=50, blank=True, null=True)
    long_m = models.BigIntegerField(blank=True, null=True)
    geom_line = models.LineStringField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=30, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=30, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=30, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_dep = models.ForeignKey('DepartBt', models.DO_NOTHING, db_column='code_dep', blank=True, null=True)
    code_der = models.ForeignKey('DerivationBt', models.DO_NOTHING, db_column='code_der', blank=True, null=True)
    nd_amont = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_amont', blank=True, null=True,related_name='nd_amont_branchements')
    nd_aval = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_aval', blank=True, null=True,related_name='nd_aval_branchements')

    class Meta:
        managed = False
        db_table = 'branchement_bt'


class CoffretDisjoncteurBt(models.Model):
    id_cdb = models.BigIntegerField(blank=True, null=True)
    code_cdb = models.CharField(primary_key=True, max_length=50)
    type_coff = models.CharField(max_length=50, blank=True, null=True)
    nb_dep_bt = models.SmallIntegerField(blank=True, null=True)
    marq_disj = models.CharField(max_length=50, blank=True, null=True)
    type_disj = models.CharField(max_length=50, blank=True, null=True)
    calib_disj = models.BigIntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_leb = models.ForeignKey('LiaisonBt', models.DO_NOTHING, db_column='code_leb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coffret_disjoncteur_bt'


class DepartBt(models.Model):
    id_dep = models.BigIntegerField(blank=True, null=True)
    code_dep = models.CharField(primary_key=True, max_length=50)
    nom_dep = models.CharField(max_length=50, blank=True, null=True)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    nat_res_bt = models.CharField(max_length=50, blank=True, null=True)
    type_tronc = models.CharField(max_length=50, blank=True, null=True)
    nat_cond = models.CharField(max_length=50, blank=True, null=True)
    sect_ph = models.BigIntegerField(blank=True, null=True)
    sect_n = models.BigIntegerField(blank=True, null=True)
    metal_cond = models.CharField(max_length=50, blank=True, null=True)
    type_cond = models.CharField(max_length=50, blank=True, null=True)
    long_m = models.BigIntegerField(blank=True, null=True)
    geom_line = models.LineStringField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_tdb = models.ForeignKey('TableauDistributionBt', models.SET_NULL, db_column='code_tdb', blank=True, null=True)
    code_cdb = models.ForeignKey(CoffretDisjoncteurBt, models.DO_NOTHING, db_column='code_cdb', blank=True, null=True)
    nd_amont = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_amont', blank=True, null=True,related_name='nd_amont_depart')
    nd_aval = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_aval', blank=True, null=True,related_name='nd_aval_depart')

    class Meta:
        managed = False
        db_table = 'depart_bt'


class DerivationBt(models.Model):
    id_der = models.BigIntegerField(blank=True, null=True)
    code_der = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    nat_cond = models.CharField(max_length=50, blank=True, null=True)
    nat_res_bt = models.CharField(max_length=50, blank=True, null=True)
    type_tronc = models.CharField(max_length=50, blank=True, null=True)
    sect_ph = models.BigIntegerField(blank=True, null=True)
    sect_n = models.BigIntegerField(blank=True, null=True)
    metal_cond = models.CharField(max_length=50, blank=True, null=True)
    type_cond = models.CharField(max_length=50, blank=True, null=True)
    long_m = models.BigIntegerField(blank=True, null=True)
    geom_line = models.LineStringField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_dep = models.ForeignKey(DepartBt, models.DO_NOTHING, db_column='code_dep', blank=True, null=True)
    nd_amont = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_amont', blank=True, null=True,related_name='nd_amont_derivation')
    nd_aval = models.ForeignKey('NoeudBt', models.DO_NOTHING, db_column='nd_aval', blank=True, null=True,related_name='nd_val_derivation')

    class Meta:
        managed = False
        db_table = 'derivation_bt'


class InstallationPv(models.Model):
    id_pv = models.BigIntegerField(blank=True, null=True)
    code_ipv = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    puiss_inst = models.BigIntegerField(blank=True, null=True)
    marq_ond = models.CharField(max_length=50, blank=True, null=True)
    sup_panel = models.BigIntegerField(blank=True, null=True)
    stockage = models.CharField(max_length=50, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_tc = models.ForeignKey('TableauComptage', models.DO_NOTHING, db_column='code_tc', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'installation_pv'


class LiaisonBt(models.Model):
    id_leb = models.BigIntegerField(blank=True, null=True)
    code_leb = models.CharField(primary_key=True, max_length=50)
    nat_cond1 = models.CharField(max_length=50, blank=True, null=True)
    nat_cond2 = models.CharField(max_length=50, blank=True, null=True)
    nat_cond3 = models.CharField(max_length=50, blank=True, null=True)
    nat_cond4 = models.CharField(max_length=50, blank=True, null=True)
    sect_ph = models.CharField(max_length=50, blank=True, null=True)
    sect_n = models.CharField(max_length=50, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_tra = models.ForeignKey('TransfoHtaBt', models.DO_NOTHING, db_column='code_tra', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liaison_bt'


class LiaisonHta(models.Model):
    id_leh = models.BigIntegerField(blank=True, null=True)
    code_leh = models.CharField(primary_key=True, max_length=50)
    sect_ph = models.BigIntegerField(blank=True, null=True)
    sect_n = models.BigIntegerField(blank=True, null=True)
    type_cond = models.CharField(max_length=50, blank=True, null=True)
    metal_cond = models.CharField(max_length=50, blank=True, null=True)
    long_m = models.BigIntegerField(blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_tdh = models.ForeignKey('TableauDistributionHta', models.DO_NOTHING, db_column='code_tdh', blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liaison_hta'


class NoeudBt(models.Model):
    id_nod = models.BigIntegerField(blank=True, null=True)
    code_nod = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    eqt_nod = models.CharField(max_length=50, blank=True, null=True)
    cal_fus = models.CharField(max_length=50, blank=True, null=True)
    sortie_pt = models.CharField(max_length=50, blank=True, null=True)
    derivation = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    chgt_carac = models.CharField(max_length=50, blank=True, null=True)
    bout_res = models.CharField(max_length=50, blank=True, null=True)
    aero_st = models.CharField(max_length=50, blank=True, null=True)
    limit_dist = models.CharField(max_length=50, blank=True, null=True)
    pl_ind = models.CharField(max_length=50, blank=True, null=True)
    pl_col = models.CharField(max_length=50, blank=True, null=True)
    autre = models.CharField(max_length=50, blank=True, null=True)
    nb_etage = models.SmallIntegerField(blank=True, null=True)
    sect_col = models.CharField(max_length=50, blank=True, null=True)
    long_col = models.BigIntegerField(blank=True, null=True)
    marq_coff = models.BigIntegerField(blank=True, null=True)
    nb_compt = models.SmallIntegerField(blank=True, null=True)
    x_32632 = models.BigIntegerField(blank=True, null=True)
    y_32632 = models.BigIntegerField(blank=True, null=True)
    geom_point = models.PointField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey('PosteHtaBt', models.DO_NOTHING, db_column='code_pt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noeud_bt'


class PointAncrageBt(models.Model):
    id_anc = models.BigIntegerField(blank=True, null=True)
    code_anc = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    type_ancr = models.CharField(max_length=50, blank=True, null=True)
    nb_der = models.SmallIntegerField(blank=True, null=True)
    nb_br = models.SmallIntegerField(blank=True, null=True)
    x_32632 = models.BigIntegerField(blank=True, null=True)
    y_32632 = models.BigIntegerField(blank=True, null=True)
    geom_point = models.PointField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_bra = models.ForeignKey(BranchementBt, models.DO_NOTHING, db_column='code_bra', blank=True, null=True)
    code_der = models.ForeignKey(DerivationBt, models.DO_NOTHING, db_column='code_der', blank=True, null=True)
    code_dep = models.ForeignKey(DepartBt, models.DO_NOTHING, db_column='code_dep', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'point_ancrage_bt'


class PosteHtaBt(models.Model):
    id_pt = models.BigIntegerField(blank=True, null=True)
    code_pt = models.CharField(primary_key=True, max_length=50)
    nom_pt = models.CharField(max_length=50, blank=True, null=True)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    gto_pt = models.CharField(max_length=50, blank=True, null=True)
    dep_hta = models.CharField(max_length=50, blank=True, null=True)
    gto_dep = models.CharField(max_length=50, blank=True, null=True)
    deriv_prin = models.CharField(max_length=50, blank=True, null=True)
    fonct_pt = models.CharField(max_length=50, blank=True, null=True)
    etat_pt = models.CharField(max_length=50, blank=True, null=True)
    type_pt = models.CharField(max_length=50, blank=True, null=True)
    phase_racc = models.CharField(max_length=50, blank=True, null=True)
    struct_pt = models.CharField(max_length=50, blank=True, null=True)
    u_prim = models.BigIntegerField(blank=True, null=True)
    u_sec = models.SmallIntegerField(blank=True, null=True)
    mod_racc = models.CharField(max_length=50, blank=True, null=True)
    nb_transf = models.SmallIntegerField(blank=True, null=True)
    pui_kva = models.SmallIntegerField(blank=True, null=True)
    nb_dep_tot = models.SmallIntegerField(blank=True, null=True)
    sect_fusib = models.CharField(max_length=50, blank=True, null=True)
    type_paraf = models.CharField(max_length=50, blank=True, null=True)
    telecomm = models.CharField(max_length=50, blank=True, null=True)
    racc_bcc = models.CharField(max_length=50, blank=True, null=True)
    pre_ild = models.CharField(max_length=50, blank=True, null=True)
    type_comp = models.CharField(max_length=50, blank=True, null=True)
    milieu = models.CharField(max_length=50, blank=True, null=True)
    dms = models.BigIntegerField(blank=True, null=True)
    sch_unif = models.CharField(max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    surf_pt = models.BigIntegerField(blank=True, null=True)
    x_cent = models.BigIntegerField(blank=True, null=True)
    y_cent = models.BigIntegerField(blank=True, null=True)
    geom_pt = models.PolygonField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poste_hta_bt'


class SupportBt(models.Model):
    id_sup = models.BigIntegerField(blank=True, null=True)
    code_sup = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    nb_dep = models.SmallIntegerField(blank=True, null=True)
    nb_der = models.SmallIntegerField(blank=True, null=True)
    nb_br = models.SmallIntegerField(blank=True, null=True)
    typ_sup = models.CharField(max_length=50, blank=True, null=True)
    etat_sup = models.CharField(max_length=50, blank=True, null=True)
    access_sup = models.CharField(max_length=50, blank=True, null=True)
    mise_terre = models.CharField(max_length=50, blank=True, null=True)
    ecl_public = models.CharField(max_length=50, blank=True, null=True)
    ancr_fo = models.CharField(max_length=50, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    x_32632 = models.BigIntegerField(blank=True, null=True)
    y_32632 = models.BigIntegerField(blank=True, null=True)
    geom_point = models.PointField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_bra = models.ForeignKey(BranchementBt, models.DO_NOTHING, db_column='code_bra', blank=True, null=True)
    code_der = models.ForeignKey(DerivationBt, models.DO_NOTHING, db_column='code_der', blank=True, null=True)
    code_dep = models.ForeignKey(DepartBt, models.DO_NOTHING, db_column='code_dep', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_bt'


class TableauComptage(models.Model):
    id_tc = models.BigIntegerField(blank=True, null=True)
    code_tc = models.CharField(primary_key=True, max_length=50)
    ur = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    ut = models.CharField(max_length=50, blank=True, null=True)
    gouv = models.CharField(max_length=50, blank=True, null=True)
    deleg = models.CharField(max_length=50, blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    nom_dep = models.CharField(max_length=50, blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    ref_client = models.CharField(max_length=50, blank=True, null=True)
    usage_tc = models.CharField(max_length=50, blank=True, null=True)
    emplac_tc = models.CharField(max_length=50, blank=True, null=True)
    acces_tc = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    type_tc = models.CharField(max_length=50, blank=True, null=True)
    marque_ctr = models.CharField(max_length=50, blank=True, null=True)
    num_serie = models.CharField(max_length=50, blank=True, null=True)
    tech_ctr = models.CharField(max_length=50, blank=True, null=True)
    nat_res = models.CharField(max_length=50, blank=True, null=True)
    phase_racc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    type_br = models.CharField(max_length=50, blank=True, null=True)
    rapport_tc_bt_et_mt_field = models.CharField(db_column='rapport_tc (BT et MT)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rapport_tp_mt_field = models.CharField(db_column='rapport_tp (MT)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_ctr = models.CharField(max_length=50, blank=True, null=True)
    etat_ctr = models.CharField(max_length=50, blank=True, null=True)
    marq_disj = models.CharField(max_length=50, blank=True, null=True)
    calib_disj = models.CharField(max_length=50, blank=True, null=True)
    num_etage = models.SmallIntegerField(blank=True, null=True)
    sect_col = models.CharField(max_length=50, blank=True, null=True)
    long_col = models.BigIntegerField(blank=True, null=True)
    type_coff = models.CharField(max_length=50, blank=True, null=True)
    sect_desc = models.CharField(max_length=50, blank=True, null=True)
    long_desc = models.BigIntegerField(blank=True, null=True)
    date_f_ctr = models.CharField(max_length=50, blank=True, null=True)
    dms_ctr = models.CharField(max_length=50, blank=True, null=True)
    x_32632 = models.BigIntegerField(blank=True, null=True)
    y_32632 = models.BigIntegerField(blank=True, null=True)
    geom_point = models.PointField(srid=0, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey(PosteHtaBt, models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_dep = models.ForeignKey(DepartBt, models.DO_NOTHING, db_column='code_dep', blank=True, null=True)
    code_bra = models.ForeignKey(BranchementBt, models.DO_NOTHING, db_column='code_bra', blank=True, null=True)
    code_der = models.ForeignKey(DerivationBt, models.DO_NOTHING, db_column='code_der', blank=True, null=True)
    code_nod = models.ForeignKey(NoeudBt, models.DO_NOTHING, db_column='code_nod', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tableau_comptage'


class TableauDistributionBt(models.Model):
    id_tdb = models.BigIntegerField(blank=True, null=True)
    code_tdb = models.CharField(primary_key=True, max_length=50)
    type_tdb = models.CharField(max_length=50, blank=True, null=True)
    nb_dep_tot = models.SmallIntegerField(blank=True, null=True)
    nb_dep_aff = models.SmallIntegerField(blank=True, null=True)
    marque_tdb = models.CharField(max_length=50, blank=True, null=True)
    num_serie = models.CharField(max_length=50, blank=True, null=True)
    annee_fab = models.CharField(max_length=50, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey(PosteHtaBt, models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_leb = models.ForeignKey(LiaisonBt, models.DO_NOTHING, db_column='code_leb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tableau_distribution_bt'


class TableauDistributionHta(models.Model):
    id_tdh = models.BigIntegerField(blank=True, null=True)
    code_tdh = models.CharField(primary_key=True, max_length=15)
    code_pt = models.ForeignKey(PosteHtaBt, models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    type_tdh = models.CharField(max_length=50, blank=True, null=True)
    config_tdh = models.CharField(max_length=50, blank=True, null=True)
    marque_tdh = models.CharField(max_length=30, blank=True, null=True)
    ref_tdh = models.CharField(max_length=50, blank=True, null=True)
    isol_jdb = models.CharField(max_length=50, blank=True, null=True)
    type_cell = models.CharField(max_length=50, blank=True, null=True)
    cmd_cell = models.CharField(max_length=50, blank=True, null=True)
    mq_inters = models.CharField(max_length=50, blank=True, null=True)
    sect_jdb = models.BigIntegerField(blank=True, null=True)
    isola_jdb = models.TextField(blank=True, null=True)  # This field type is a guess.
    num_serie1 = models.CharField(max_length=50, blank=True, null=True)
    num_serie2 = models.CharField(max_length=50, blank=True, null=True)
    num_serie3 = models.CharField(max_length=50, blank=True, null=True)
    num_serie4 = models.CharField(max_length=50, blank=True, null=True)
    num_serie5 = models.CharField(max_length=50, blank=True, null=True)
    num_serie6 = models.CharField(max_length=50, blank=True, null=True)
    annee_fab = models.SmallIntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tableau_distribution_hta'


class TerrainPoste(models.Model):
    id_ter = models.BigIntegerField(blank=True, null=True)
    code_ter = models.CharField(primary_key=True, max_length=50)
    titre_fonc = models.CharField(max_length=50, blank=True, null=True)
    etat_fonc = models.CharField(max_length=50, blank=True, null=True)
    surf_ter = models.BigIntegerField(blank=True, null=True)
    x_cent = models.BigIntegerField(blank=True, null=True)
    y_cent = models.BigIntegerField(blank=True, null=True)
    geom_poly = models.PolygonField(srid=0, blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    obs = models.CharField(max_length=50, blank=True, null=True)
    code_pt = models.ForeignKey(PosteHtaBt, models.DO_NOTHING, db_column='code_pt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrain_poste'


class TransfoHtaBt(models.Model):
    id_tra = models.BigIntegerField(blank=True, null=True)
    code_tra = models.CharField(primary_key=True, max_length=50)
    pui_kva = models.BigIntegerField(blank=True, null=True)
    type_tra = models.CharField(max_length=50, blank=True, null=True)
    marque_tra = models.CharField(max_length=50, blank=True, null=True)
    n_serie_tra = models.CharField(max_length=50, blank=True, null=True)
    annee_fab = models.SmallIntegerField(blank=True, null=True)
    racc_hta = models.CharField(max_length=50, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    cree_par = models.CharField(max_length=50, blank=True, null=True)
    cree_le = models.CharField(max_length=50, blank=True, null=True)
    maj_par = models.CharField(max_length=50, blank=True, null=True)
    maj_le = models.CharField(max_length=50, blank=True, null=True)
    dist_par = models.CharField(max_length=50, blank=True, null=True)
    dist_le = models.CharField(max_length=50, blank=True, null=True)
    ddsf_par = models.CharField(max_length=50, blank=True, null=True)
    ddsf_le = models.CharField(max_length=50, blank=True, null=True)
    sigt_par = models.CharField(max_length=50, blank=True, null=True)
    sigt_le = models.CharField(max_length=50, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    code_pt = models.ForeignKey(PosteHtaBt, models.DO_NOTHING, db_column='code_pt', blank=True, null=True)
    code_leh = models.ForeignKey(LiaisonHta, models.DO_NOTHING, db_column='code_leh', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfo_hta_bt'
