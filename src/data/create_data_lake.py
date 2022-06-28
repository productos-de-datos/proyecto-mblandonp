def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    # importing os module 
    import os
  
    # mkdir(path): Create a directory named data_lake.
    os.mkdir('./data_lake')
    # Parent Directory path
    parent_dir = "data_lake"

    carpetas = ['landing', 'raw', 'cleansed', 'business']
    [os.mkdir(os.path.join(parent_dir, c)) for c in carpetas]
        
    parent_dir = "data_lake/business"

    carpetas = ['reports', 'features', 'forecasts']
    [os.mkdir(os.path.join(parent_dir, c)) for c in carpetas]

    # Parent Directory path
    parent_dir = "data_lake/business/reports"

    # Directory
    directory = "figures"

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    os.mkdir(path)
    #raise NotImplementedError("Implementar esta función")    
#    return

if __name__ == "__main__":

    import doctest
    doctest.testmod()
    create_data_lake()

