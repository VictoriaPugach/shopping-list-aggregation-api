# Product scenarios

1. A person selects several recipes for the week and receives one shopping list with duplicate ingredients merged.
2. A person changes the number of servings and receives recalculated quantities.
3. A person marks pantry items as available and receives a list reduced by those quantities.
4. The mobile client sends Recipe objects to this service and uses the response to render shopping tasks.

The first MVP focuses on the API boundary and predictable aggregation rules. Store integration, price comparison, and barcode scanning are outside its scope.
