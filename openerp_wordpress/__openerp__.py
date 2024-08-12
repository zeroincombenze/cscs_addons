# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#   #########################################################################
#   Developed by: carlosecv74@hotmail.com
#   #########################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Wordpress site integration",
    "version" : "1.1",
    "author" : "Carlos Contreras <carlosecv74@hotmail.com>",
    "category" : "Customization",
    "depends" : ["base"],
    "description": """
Module to integrate a Wordpress site into OpenERP.
========================================================================
   Developed by: Carlos Enrique Contreras Vara
  
    You can use it for:
        Quality Manual over OpenERP
        Set a Blog inside the organization
        or a News Site with multimedia content 
        
        See doc/README.TXT for fast customization
    """,
    "init_xml" : [
                ],
    "demo_xml" : [],
    "update_xml" : [ 
                     "view/wordpress_view.xml",                  
                    ],
    'application': True,
    "installable": True,
    "active": False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
