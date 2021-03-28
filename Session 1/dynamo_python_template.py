# Load the Python Standard and DesignScript Libraries
import clr

clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
from Autodesk.Revit.DB.Structure import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *

clr.AddReference("System")
from System.Collections.Generic import List

clr.AddReference("RevitNodes")
import Revit

clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Preparing input from dynamo to revit

# Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

OUT = 0

TransactionManager.Instance.TransactionTaskDone()