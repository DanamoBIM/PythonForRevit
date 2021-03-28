"""Create worksets from a list and set defautl visibility"""
from Autodesk.Revit import DB


def set_workset_default_visiblity(d, workset, state):
    wdvs = DB.WorksetDefaultVisibilitySettings.GetWorksetDefaultVisibilitySettings(d)
    wdvs.SetWorksetVisibility(workset.Id, state)


def create_workset(d, name):
    return DB.Workset.Create(d, name)


workset_names = ["Interior_FFE", "Life_Safety", "Interior_Hidden"]


if doc.IsWorkshared:
    t = DB.Transaction(doc, "Create Worksets")
    t.Start()

    # make your model changes here
    for name in workset_names:
        ws = create_workset(doc, name)
        if "Hidden" in name:
            set_workset_default_visiblity(doc, ws, False)

    t.Commit()