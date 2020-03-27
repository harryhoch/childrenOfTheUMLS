# childrenOfTheUMLS

Use the UMLS API to retrieve "NB" relations of a starting CUI.

Usage:
```
Umlsapi = UmlsApi("<username>", "<password>")
cuis = {}
umlsApi.getRelatedCuis("C0015967", cuis)
```
