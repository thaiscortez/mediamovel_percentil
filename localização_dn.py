# -*- coding: utf-8 -*-
"""loc_DN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WNAA7eoEViPaiSXUoGspadWF1W386gtQ
"""

# Instação cartopy e proplot:
!pip install cartopy==0.18.0
!pip uninstall -y shapely
!pip install shapely --no-binary shapely
!wget https://raw.githubusercontent.com/SciTools/cartopy/master/tools/cartopy_feature_download.py
!python cartopy_feature_download.py physical

!pip install proplot

# Intalando pacote para mascarar shapefile
!pip install salem
!pip install geopandas
!pip install pyproj
!pip install rasterio

# Baixa paleta de cores
!wget -c https://www.dropbox.com/s/t7b8x2i3gnsq8gv/cpt_convert.py

# Baixando os arquivos de shapefile dos estados do Sudeste
!wget -q -c https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/MG/mg_unidades_da_federacao.zip
!wget -q -c https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/ES/es_unidades_da_federacao.zip
!wget -q -c https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/RJ/rj_unidades_da_federacao.zip
!wget -q -c https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/SP/sp_unidades_da_federacao.zip

#BAHIA
!wget -q -c https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/BA/ba_unidades_da_federacao.zip

!unzip -o /content/mg_unidades_da_federacao.zip
!unzip -o /content/es_unidades_da_federacao.zip
!unzip -o /content/rj_unidades_da_federacao.zip
!unzip -o /content/sp_unidades_da_federacao.zip
!unzip -o /content/ba_unidades_da_federacao.zip

##############################################
import matplotlib
matplotlib.rcParams.update({'font.size':22})
from matplotlib import pyplot as plt
#from cpt_convert import loadCPT # Importando a função CPT convert
from matplotlib.colors import LinearSegmentedColormap # interpolação linear para as cores dos mapas
##############################################
import proplot as plot
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
##############################################
import numpy as np
import glob
##############################################
import salem
import xarray as xr
import pandas as pd
##############################################
import warnings
warnings.filterwarnings('ignore')
##############################################
import numpy as np
import plotly.figure_factory as ff
##############################################
# acessando o drive
from google.colab import drive
drive.mount('/content/drive', force_remount=False)
##############################################

path = f'/content/drive/MyDrive/mestrado/Dados/CEMADEN/'

#-----------------------------------------------------------------------------------
# Função que plota por Estado
#-----------------------------------------------------------------------------------
def evm_plot_by_state():
    shapefile = list(shpreader.Reader('/content/ES_UF_2019.shp').geometries()) ; ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='none', linewidth=1.7)
    shapefile = list(shpreader.Reader('/content/MG_UF_2019.shp').geometries()) ; ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='none', linewidth=1.7)
    shapefile = list(shpreader.Reader('/content/RJ_UF_2019.shp').geometries()) ; ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='none', linewidth=1.7)
    shapefile = list(shpreader.Reader('/content/SP_UF_2019.shp').geometries()) ; ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='none', linewidth=1.7)
    shapefile = list(shpreader.Reader('/content/BA_UF_2019.shp').geometries()) ; ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='none', linewidth=1.7)

latN = -7
latS = -25
lonW = -55
lonE = -30

df = pd.ExcelFile(f'{path}/Ocorrencias.Bahia.122021.xlsx')

from proplot.internals.rcsetup import LINEWIDTH
# Plotando a figura de pnmm+jatos+espessura

matplotlib.rcParams.update({'font.size':22})

fig, ax = plot.subplots(nrows=3, ncols=2,  figsize=(20,20), tight=True, proj='pcarree',hspace=10, wspace=2.5)
ax.format(coast=True, borders=True, innerborders=False, labels=True, latlines=5, lonlines=5,
          latlim=(latN, latS), lonlim=(lonW, lonE))

################################################################################
#FIGURA 1
ax[0].format(title='2021-12-23',abc=True, abcstyle='a)', abcsize=20)
#MG
map1 = ax[0].scatter(-44.01, -19.84, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Belo Horizonte')
map1 = ax[0].scatter(-41.58, -17.17, s=30, marker='s',color='pink', zorder=20, transform=ccrs.PlateCarree(), label = 'Caraí')
map1 = ax[0].scatter(-41.64, -18.58, s=30, marker='s',color='purple', zorder=20, transform=ccrs.PlateCarree(), label = 'Jampruca')
map1 = ax[0].scatter(-43.92, -16.61, s=30, marker='s',color='blue', zorder=20, transform=ccrs.PlateCarree(), label = 'Montes Claros')
map1 = ax[0].scatter(-41.96, -18.78, s=30, marker='s',color='green', zorder=20, transform=ccrs.PlateCarree(), label = 'Governador Valadares')
map1 = ax[0].scatter(-40.76, -17.70, s=30, marker='s',color='yellow', zorder=20, transform=ccrs.PlateCarree(), label = 'Carlos Chagas 2')
map1 = ax[0].scatter(-43.77, -19.85, s=30, marker='s',color='black', zorder=20, transform=ccrs.PlateCarree(), label = 'Sabará')

#Legenda
ax[0].legend(ncol=1, prop={'size':10}, loc= 'lower right')


################################################################################
#FIGURA 2
ax[1].format(title='2021-12-24',abc=True, abcstyle='a)', abcsize=20)
#BA
map1 = ax[1].scatter(-39.50, -13.22, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Mutuípe 2')
map1 = ax[1].scatter(-39.07, -16.43, s=30, marker='s',color='pink', zorder=20, transform=ccrs.PlateCarree(), label = 'Porto Seguro')
map1 = ax[1].scatter(-39.32, -14.84, s=30, marker='s',color='purple', zorder=20, transform=ccrs.PlateCarree(), label = 'Itabuna')
map1 = ax[1].scatter(-40.83, -14.89, s=30, marker='s',color='blue', zorder=20, transform=ccrs.PlateCarree(), label = 'Vitória da Conquista')
map1 = ax[1].scatter(-40.28, -17.36, s=30, marker='s',color='green', zorder=20, transform=ccrs.PlateCarree(), label = 'Medeiros Neto')
#MG
map1 = ax[1].scatter(-40.76, -17.70, s=30, marker='s',color='yellow', zorder=20, transform=ccrs.PlateCarree(), label = 'Carlos Chagas')
map1 = ax[1].scatter(-46.89, -16.36, s=30, marker='s',color='black', zorder=20, transform=ccrs.PlateCarree(), label = 'Unaí')

#Legenda
ax[1].legend(ncol=1, prop={'size':10}, loc= 'lower right')

################################################################################
#FIGURA 3
ax[2].format(title='2021-12-25',abc=True, abcstyle='a)', abcsize=20)
#BA
map1 = ax[2].scatter(-39.50, -13.22, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Mutuípe')
map1 = ax[2].scatter(-39.48, -13.74, s=30, marker='s',color='pink', zorder=20, transform=ccrs.PlateCarree(), label = 'Gandu 3')
map1 = ax[2].scatter(-39.32, -14.84, s=30, marker='s',color='purple', zorder=20, transform=ccrs.PlateCarree(), label = 'Itabuna 2')
map1 = ax[2].scatter(-39.19, -14.74, s=30, marker='s',color='blue', zorder=20, transform=ccrs.PlateCarree(), label = 'Ilheús')
map1 = ax[2].scatter(-39.15, -14.36, s=30, marker='s',color='green', zorder=20, transform=ccrs.PlateCarree(), label = 'Itacaré')
map1 = ax[2].scatter(-40.05, -15.30, s=30, marker='s',color='yellow', zorder=20, transform=ccrs.PlateCarree(), label = 'Itapetinga')
map1 = ax[2].scatter(-38.45, -12.84, s=30, marker='s',color='black', zorder=20, transform=ccrs.PlateCarree(), label = 'Salvador 2')

#Legenda
ax[1].legend(ncol=1, prop={'size':10}, loc= 'lower right')

################################################################################
#FIGURA 4
ax[3].format(title='2021-12-26',abc=True, abcstyle='a)', abcsize=20)
#MG
map1 = ax[3].scatter(-39.96, -13.52, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Jaguaquara 3')

#Legenda
ax[3].legend(ncol=1, prop={'size':10}, loc= 'lower right')


################################################################################
#FIGURA 5
ax[4].format(title='2021-12-27',abc=True, abcstyle='a)', abcsize=20)
#BA
map1 = ax[4].scatter(-43.81, -16.71, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Montes Claros')
map1 = ax[4].scatter(-43.35, -21.75, s=30, marker='s',color='pink', zorder=20, transform=ccrs.PlateCarree(), label = 'Juiz de Fora')

#Legenda
ax[4].legend(ncol=1, prop={'size':10}, loc= 'lower right')
# plota contornos dos Estados
evm_plot_by_state()

################################################################################
#FIGURA 6
ax[5].format(title='2021-12-23',abc=True, abcstyle='a)', abcsize=20)
#MG
map1 = ax[5].scatter(-44.01, -19.84, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Belo Horizonte')
map1 = ax[5].scatter(-41.58, -17.17, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Caraí')
map1 = ax[5].scatter(-41.64, -18.58, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Jampruca')
map1 = ax[5].scatter(-43.92, -16.61, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Montes Claros 2')
map1 = ax[5].scatter(-41.96, -18.78, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Governador Valadares')
map1 = ax[5].scatter(-40.76, -17.70, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Carlos Chagas 3')
map1 = ax[5].scatter(-43.77, -19.85, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Sabará')
map1 = ax[5].scatter(-39.50, -13.22, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Mutuípe 3')
map1 = ax[5].scatter(-39.07, -16.43, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Porto Seguro')
map1 = ax[5].scatter(-39.32, -14.84, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Itabuna 3')
map1 = ax[5].scatter(-40.83, -14.89, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Vitória da Conquista')
map1 = ax[5].scatter(-40.28, -17.36, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Medeiros Neto')
map1 = ax[5].scatter(-46.89, -16.36, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Unaí')
map1 = ax[5].scatter(-39.48, -13.74, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Gandu 3')
map1 = ax[5].scatter(-39.19, -14.74, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Ilheús')
map1 = ax[5].scatter(-39.15, -14.36, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Itacaré')
map1 = ax[5].scatter(-40.05, -15.30, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Itapetinga')
map1 = ax[5].scatter(-38.45, -12.84, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Salvador 2')
map1 = ax[5].scatter(-39.96, -13.52, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Jaguaquara 3')
map1 = ax[5].scatter(-43.35, -21.75, s=30, marker='s',color='red', zorder=20, transform=ccrs.PlateCarree(), label = 'Juiz de Fora')

fig.savefig(f'{path}/loc3.png', dpi=300)

