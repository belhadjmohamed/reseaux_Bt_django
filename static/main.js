window.onload = init ;

function init(){

    // basemaps
    const basemap = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}) 

    const Stadia_Outdoors = L.tileLayer('https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });    

    const Stadia_AlidadeSmoothDark = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });
 
    var OpenTopoMap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });


    //leaflet map object

    const mymap = L.map('mapid', {
        center : [35,11],
        zoom :  10,
        layers: [basemap]        
    })

    //base maps object
    const baseLayers = {
        'openstreetmap' : basemap,
        'stadiamap' : Stadia_Outdoors,
        'Stadia_AlidadeSmoothDark' : Stadia_AlidadeSmoothDark,
        'OpenTopoMap' : OpenTopoMap
    }

    //overlay 
    const images = './data.png';
    
    const imagesbounds = [[35.64489084423065, 8.349386360370678],[37.49217532312882, 11.524045755094672]]

    const ovelayimages = L.imageOverlay(images,imagesbounds)
    
    //overlay object 
    const overlayers = {
        'images1' : ovelayimages,
    }
   	
    

    // map control
    const layercontrol = L.control.layers(baseLayers,overlayers,{}, {position : 'topright'}).addTo(mymap) 

    // les supports 
    var markersDataElement = document.getElementById('markers-data');
    var markers = JSON.parse(markersDataElement.textContent);
    utm_zone = 32;
    const utmProj = '+proj=utm +zone=32 +datum=WGS84 +units=m +no_defs';
    const geoProj = '+proj=longlat +datum=WGS84 +no_defs';
    

    
    for (var i = 0; i < markers.length; i++) {
        var utmCoords = [markers[i].lon, markers[i].lat];
        var geographicCoords = proj4(utmProj, geoProj, utmCoords);
        var marker = L.circle(geographicCoords.reverse(),{
            color: 'green', 
            fillColor: 'green',  
            fillOpacity: 1, 
            radius: 3
        }).addTo(mymap);
        marker.bindPopup(markers[i].name);
    }

    // les lignes branchements

    var linesDataElement = document.getElementById('lines-data');
    var lines = JSON.parse(linesDataElement.textContent);
    const utmProj1 = '+proj=utm +zone=32 +datum=WGS84 +units=m +no_defs';
    const geoProj1 = '+proj=longlat +datum=WGS84 +no_defs';
    
    for (var k =0 ; k < lines.length; k++){
        var jsonObject = JSON.parse(lines[k].coord);
        var coordinates = jsonObject.coordinates;
        liste_coord_line=[];
        for (var p=0; p < coordinates.length;p++){
            utmCoordss = [coordinates[p][0] ,  coordinates[p][1]]; 
            geocoords =  proj4(utmProj1, geoProj1, utmCoordss); 
            a = geocoords.reverse();     
            liste_coord_line.push(a);    
        }
        var polyline = L.polyline(liste_coord_line, {color: 'orange'}).addTo(mymap);
        polyline.bindPopup(lines[k].name);
    }

    // le poste

    var postedata  = document.getElementById('poste-data');
    var postes = JSON.parse(postedata.textContent);
    const utmProj2 = '+proj=utm +zone=32 +datum=WGS84 +units=m +no_defs';
    const geoProj2 = '+proj=longlat +datum=WGS84 +no_defs';
    
    for (var x =0 ; x < postes.length; x++){
        var POSTEcoord = JSON.parse(postes[x].coord);
        var coord_poste = POSTEcoord.coordinates;
        postes_coord_p=[];
        for (var z=0; z < coord_poste[0].length; z++){
            utm_Coords = [coord_poste[0][z][0] ,  coord_poste[0][z][1]];
            geo_poste_coords =  proj4(utmProj2, geoProj2, utm_Coords); 
            b = geo_poste_coords.reverse();     
            postes_coord_p.push(b);    
        }

        var polygonOptions = {
            color: 'rgba(0, 255, 255)',   // Couleur rouge
            weight: 7,      // Épaisseur de la ligne
            fillColor: 'rgba(0, 255, 255)',  // Remplissage rouge
            fillOpacity:1   // Opacité du remplissage
        };

        var postes_leaflet = L.polygon(postes_coord_p, polygonOptions).addTo(mymap);
        postes_leaflet.bindPopup(postes[x].name);
    }

    //les lignes depart 
    var departdata = document.getElementById('depart_data');
    var depart = JSON.parse(departdata.textContent)
    const utmProj3 = '+proj=utm +zone=32 +datum=WGS84 +units=m +no_defs';
    const geoProj3 = '+proj=longlat +datum=WGS84 +no_defs';

    for (var dep = 0 ; dep < depart.length; dep++){
        var depcoord = JSON.parse(depart[dep].coord);
        var coord_dep = depcoord.coordinates;
        dep_coord_p=[];
        for (var depp= 0 ; depp < coord_dep.length; depp++){
            utm_Coords_dep = [coord_dep[depp][0] , coord_dep[depp][1]];
            geo_dep_coords =  proj4(utmProj3, geoProj3, utm_Coords_dep); 
            dep2 = geo_dep_coords.reverse();     
            dep_coord_p.push(dep2); 
        }
        var ligne_depart = L.polyline(dep_coord_p, {color: 'red'}).addTo(mymap);
        ligne_depart.bindPopup(depart[dep].name);

    }

    // les lignes derivation 
    var derivationdata = document.getElementById('derivation_data');
    var derivation = JSON.parse(derivationdata.textContent)

    for (var der = 0 ; der < derivation.length; der++){
        var dercoord = JSON.parse(derivation[der].coord);
        var coord_der = dercoord.coordinates;
        der_coord_p=[];
        for (var derr= 0 ; derr < coord_der.length; derr++){
            utm_Coords_der = [coord_der[derr][0] , coord_der[derr][1]];
            geo_der_coords =  proj4(utmProj3, geoProj3, utm_Coords_der); 
            der2 = geo_der_coords.reverse();     
            der_coord_p.push(der2); 
        }
        var ligne_derivation = L.polyline(der_coord_p, {color: 'blue'}).addTo(mymap);
        ligne_derivation.bindPopup(derivation[der].name);
    }

    // les points d'ancrage 

    var ancrageDataElement = document.getElementById('ancrages-data');
    var ancrages = JSON.parse(ancrageDataElement.textContent);
    for (var anc = 0; anc < ancrages.length; anc++) {
        var utmCoords_anc = [ancrages[anc].lon_anc, ancrages[anc].lat_anc];
        var geographicCoords_ancr = proj4(utmProj, geoProj, utmCoords_anc);
        var ancrage = L.circle(geographicCoords_ancr.reverse(),{
            color: 'blue', 
            fillColor: 'blue',  
            fillOpacity: 1, 
            radius: 3
        }).addTo(mymap);
        ancrage.bindPopup(ancrages[i].name);
    }

    //les tableaux de comptages 
    
    var comptageDataElement = document.getElementById('comptage-data');
    var comptages = JSON.parse(comptageDataElement.textContent);
    for (var com = 0; com < comptages.length; com++) {
        var utmCoords_com = [comptages[com].lon_com, comptages[com].lat_com];
        console.log(utmCoords_com)
        var geographicCoords_com = proj4(utmProj, geoProj, utmCoords_com);
        var comptage = L.circle(geographicCoords_com.reverse(),{
            color: 'red', 
            fillColor: 'red',  
            fillOpacity: 1, 
            radius: 1
        }).addTo(mymap);
        comptage.bindPopup(comptages[i].name);
    }

}

