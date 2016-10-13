{
# The human-readable name of your module, displayed in the interface
        'name' : "Humen_resource_cost" ,
# A more extensive description
        'description' : """
        """ ,
# Which modules must be installed for this one to work
        'depends' : ['base'],
# data files which are always installed
        'data': [
                'ir.model.access.csv',
                'views/resource_cost_view.xml',
                'views/resource_cost_menu.xml',
                ],
# data files which are only installed in "demonstration mode"
        'demo': ['demo.xml',
        ],

}
