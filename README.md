# childrenOfTheUMLS

Use the UMLS API to retrieve "NB" relations of a starting CUI.

Usage:

umlsApi = UmlsApi("<username>", "<password>")
cuis = {}
umlsApi.getRelatedCuis("C0015967", cuis)
