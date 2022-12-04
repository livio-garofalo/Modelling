import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def EXTRA_plot_4_models(models, models_names):
    """
    Function to plot four (and only four!) climate models in a subplot. Using  Plate-Carrée Porjections

    Keyword arguments:
    models -- dictionairy of the the model values and model names. Model value should be in global dimension lon/lat and contain
              only Temperature as variable in Kelvin
    models_name -- should be models_names = list(models.keys())
    
    Additional Info:
    ax --Prepare 4 axes for subplots. Setting  Plate-Carrée Porjections
    axes -- preparing list of axes for iterating
    index -- indices for iterating 
    
    Iterating for each subplot seperatly.
    i -- axes
    j -- index
    data -- save model data
    plot coastlines
    plot colormesh
    
    gl. ... --set x/y label in Degreees on bottom and left axes
    """
    fig = plt.figure(figsize = (18,9))
    ax0 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax1 = plt.subplot2grid((2, 2), (0, 1), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    axes = [ax0, ax1, ax2, ax3]
    index = [0,1,2,3]
    for i,j in zip(axes, index):
        data = models[models_names[j]]
        i.coastlines()
        data.plot.pcolormesh(ax = i, cmap ='coolwarm', robust = True, label = "Temperatur", cbar_kwargs={'label': "Temperature in K"})
        i.coastlines()
        i.set_extent([-160, 160, -90, 90])
        gl = i.gridlines(draw_labels = True)
        gl.xlabel_style = dict(fontsize = 9)
        gl.ylabel_style = dict(fontsize = 9, rotation = 90, va = 'bottom', ha = 'center')
        gl.top_labels = False
        gl.right_labels = False
        i.set_title("1970-2014 mean temperature {}".format(models_names[j]), fontsize = 16)
        
def EXTRA_diffs_to_era5(models, era5_mean, models_names):
    """
    Function to plot four (and only four!) climate models and their differences to the era5 mean in a subplot. 
    Using  Plate-Carrée Porjections

    Keyword arguments:
    models -- dictionairy of the the model values and model names. Model value should be in global dimension lon/lat and contain
              only Temperature as variable in Kelvin
    models_name -- should be models_names = list(models.keys())
    era5_mean -- 
    
    Additional Info:
    ax --Prepare 4 axes for subplots. Setting  Plate-Carrée Porjections
    axes -- preparing list of axes for iterating
    index -- indices for iterating 
    
    Iterating for each subplot seperatly.
    i -- axes
    j -- index
    data -- save differnce of era5 to model data
    plot coastlines
    plot colormesh
    
    gl. ... --set x/y label in Degreees on bottom and left axes
    
    """
    fig = plt.figure(figsize = (18,9))
    ax0 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax1 = plt.subplot2grid((2, 2), (0, 1), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1, projection=ccrs.PlateCarree())
    axes = [ax0, ax1, ax2, ax3]
    index = [0,1,2,3]
    for i,j in zip(axes, index):
        data =  era5_mean - models[models_names[j]]
        i.coastlines()
        data.plot.pcolormesh(ax = i, cmap ='coolwarm', robust = True, cbar_kwargs={'label': "Temperature difference in K"})
        i.coastlines()
        i.set_extent([-160, 160, -90, 90])
        gl = i.gridlines(draw_labels = True)
        gl.xlabel_style = dict(fontsize = 9)
        gl.ylabel_style = dict(fontsize = 9, rotation = 90, va = 'bottom', ha = 'center')
        gl.top_labels = False
        gl.right_labels = False
        i.set_title("1970-2014 Diffs Temp: of {} to ERA5".format(models_names[j]), fontsize = 13)
        




